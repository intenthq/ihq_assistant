import argparse
import json
import os
import time
from pathlib import Path
from typing import List, Dict, Any
import logging
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
from pydantic import BaseModel, Field

# Set up logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')
logger = logging.getLogger(__name__)

# Define Pydantic model for validation
class TicketKeywords(BaseModel):
    keywords: List[str] = Field(description="List of keywords extracted from the ticket")

def parse_args() -> argparse.Namespace:
    """Parse command line arguments."""
    parser = argparse.ArgumentParser(description="Extract keywords from Linear tickets using OpenAI's Batch API")
    parser.add_argument("--input", required=True, help="Directory containing Linear ticket JSON files")
    parser.add_argument("--output", required=True, help="Directory to save enriched Linear tickets")
    parser.add_argument("--model", default="gpt-4o", help="OpenAI model to use (default: gpt-4o)")
    parser.add_argument("--max-tickets", type=int, help="Maximum number of tickets to process (for testing)")
    parser.add_argument("--api-key", help="OpenAI API key (defaults to OPENAI_API_KEY environment variable)")
    parser.add_argument("--direct", action="store_true", help="Use direct API calls instead of batch API")
    return parser.parse_args()

def load_tickets(input_dir: str, max_tickets: int = None) -> List[Dict[str, Any]]:
    """Load Linear tickets from JSON files in the input directory."""
    input_path = Path(input_dir)
    if not input_path.exists() or not input_path.is_dir():
        raise ValueError(f"Input directory does not exist: {input_dir}")
    
    tickets = []
    for file_path in input_path.glob("*.json"):
        try:
            with open(file_path, "r") as f:
                ticket = json.load(f)
                tickets.append(ticket)
                logger.debug(f"Loaded ticket: {ticket.get('id', 'unknown')} - {ticket.get('title', 'untitled')}")
        except json.JSONDecodeError:
            logger.error(f"Failed to parse JSON from {file_path}")
        except Exception as e:
            logger.error(f"Error loading {file_path}: {str(e)}")
            
        if max_tickets and len(tickets) >= max_tickets:
            break
    
    logger.info(f"Loaded {len(tickets)} tickets from {input_dir}")
    return tickets

def create_batch_tasks(tickets: List[Dict[str, Any]], model: str) -> str:
    """Create batch tasks file for OpenAI's Batch API."""
    # Define the schema manually to ensure it has the correct format
    schema = {
        "type": "json_schema",
        "json_schema": {
            "name": "TicketKeywords",
            "strict": True,
            "schema": {
                "type": "object",
                "properties": {
                    "keywords": {
                        "type": "array",
                        "items": {"type": "string"},
                        "description": "List of keywords extracted from the ticket"
                    }
                },
                "required": ["keywords"],
                "additionalProperties": False
            }
        }
    }
    
    batch_file = Path("linear_tickets_batch.jsonl")
    with open(batch_file, "w") as file:
        for ticket in tickets:
            # Create meaningful content from ticket data
            ticket_content = f"Ticket Title: {ticket.get('title', 'No title')}\n\n"
            ticket_content += f"Description: {ticket.get('description', 'No description')}"
            
            task = {
                "custom_id": f"ticket-{ticket.get('id', '')}",
                "method": "POST",
                "url": "/v1/chat/completions",
                "body": {
                    "model": model,
                    "messages": [
                        {
                            "role": "system",
                            "content": "Extract the most important technical keywords from the Linear ticket. Return only the keywords as a list of strings."
                        },
                        {"role": "user", "content": ticket_content}
                    ],
                    "response_format": schema
                }
            }
            file.write(json.dumps(task) + "\n")
    
    logger.info(f"Created batch tasks file with {len(tickets)} tasks")
    return str(batch_file)

def process_batch(client: OpenAI, batch_file: str) -> Dict[str, List[str]]:
    """Process the batch file using OpenAI's Batch API and return keywords by ticket ID."""
    # Upload the file
    with open(batch_file, "rb") as file:
        file_obj = client.files.create(file=file, purpose="batch")
    file_id = file_obj.id
    logger.info(f"Uploaded file with ID: {file_id}")
    
    # Create batch job
    batch_job = client.batches.create(
        input_file_id=file_id,
        endpoint="/v1/chat/completions",
        completion_window="24h"
    )
    batch_job_id = batch_job.id
    logger.info(f"Created batch job with ID: {batch_job_id}")
    
    # Poll for job completion
    max_attempts = 3000
    polling_interval = 10  # seconds
    for attempt in range(max_attempts):
        batch_job = client.batches.retrieve(batch_job_id)
        status = batch_job.status
        
        logger.info(f"Batch job status: {status} ({attempt+1}/{max_attempts})")
        
        if status == "completed":
            # Add a short delay to ensure output_file_id is available
            time.sleep(2)
            # Retrieve the job again to get the most up-to-date information
            batch_job = client.batches.retrieve(batch_job_id)
            break
        elif status in ["failed", "cancelled"]:
            raise RuntimeError(f"Batch job {batch_job_id} {status}: {batch_job.error}")
        
        if attempt < max_attempts - 1:
            logger.info(f"Waiting {polling_interval} seconds before checking again...")
            time.sleep(polling_interval)
    
    if status != "completed":
        raise RuntimeError(f"Batch job {batch_job_id} did not complete in time")
    
    # Get results
    output_file_id = batch_job.output_file_id
    
    # Additional check for output_file_id
    if output_file_id is None:
        logger.warning("output_file_id is None, trying to find output file by retrying")
        
        # Wait a bit longer to make sure the file is available
        time.sleep(5)
        
        # Try multiple times to get the job details
        for retry in range(3):
            batch_job = client.batches.retrieve(batch_job_id)
            output_file_id = batch_job.output_file_id
            logger.info(f"Retry {retry+1}: output_file_id = {output_file_id}")
            
            if output_file_id is not None:
                break
            
            time.sleep(5)
    
    if output_file_id is None:
        logger.error(f"Failed to get output_file_id for batch job {batch_job_id}")
        raise ValueError(f"Batch job completed but no output_file_id was provided")
    
    logger.info(f"Retrieved output file ID: {output_file_id}")
    output_content = client.files.content(output_file_id)
    output_content_str = output_content.read().decode('utf-8')
    
    # Process results
    keywords_by_id = {}
    for line in output_content_str.strip().split('\n'):
        result = json.loads(line)
        custom_id = result.get('custom_id', '')
        ticket_id = custom_id.replace('ticket-', '')
        
        if result.get('error'):
            logger.error(f"Error processing {custom_id}: {result['error']}")
            continue
        
        response_body = result.get('response', {}).get('body', {})
        if response_body:
            content = response_body.get('choices', [{}])[0].get('message', {}).get('content', '{}')
            try:
                response_data = json.loads(content)
                ticket_keywords = TicketKeywords(**response_data)
                keywords_by_id[ticket_id] = ticket_keywords.keywords
                logger.debug(f"Extracted keywords for {ticket_id}: {ticket_keywords.keywords}")
            except Exception as e:
                logger.error(f"Error parsing response for {ticket_id}: {str(e)}")
    
    # Clean up files
    try:
        client.files.delete(file_id)
        client.files.delete(output_file_id)
    except Exception as e:
        logger.warning(f"Error cleaning up files: {str(e)}")
    
    logger.info(f"Processed {len(keywords_by_id)} tickets successfully")
    
    return keywords_by_id

def process_tickets_directly(client: OpenAI, tickets: List[Dict[str, Any]], model: str) -> Dict[str, List[str]]:
    """Process tickets directly without using batch API."""
    logger.info("Using direct API calls instead of batch API")
    
    # Define the schema for direct API calls
    response_format = {
        "type": "json_object",
        "schema": {
            "type": "object",
            "properties": {
                "keywords": {
                    "type": "array",
                    "items": {"type": "string"},
                }
            },
            "required": ["keywords"],
            "additionalProperties": False
        }
    }
    
    keywords_by_id = {}
    for idx, ticket in enumerate(tickets):
        ticket_id = ticket.get('id', '')
        logger.info(f"Processing ticket {idx+1}/{len(tickets)}: {ticket_id}")
        
        # Create ticket content
        ticket_content = f"Ticket Title: {ticket.get('title', 'No title')}\n\n"
        ticket_content += f"Description: {ticket.get('description', 'No description')}"
        
        try:
            # Make direct API call
            response = client.chat.completions.create(
                model=model,
                messages=[
                    {
                        "role": "system",
                        "content": "Extract the most important technical keywords from the Linear ticket. Return only the keywords as a list of strings."
                    },
                    {"role": "user", "content": ticket_content}
                ],
                response_format=response_format
            )
            
            content = response.choices[0].message.content
            response_data = json.loads(content)
            
            keywords_by_id[ticket_id] = response_data["keywords"]
            logger.info(f"Extracted keywords for {ticket_id}: {response_data['keywords']}")
            
            # Add a small delay to avoid rate limits
            time.sleep(0.5)
            
        except Exception as e:
            logger.error(f"Error processing ticket {ticket_id}: {str(e)}")
    
    return keywords_by_id

def save_enriched_tickets(tickets: List[Dict[str, Any]], keywords_by_id: Dict[str, List[str]], output_dir: str):
    """Save enriched tickets (with keywords) to the output directory."""
    output_path = Path(output_dir)
    output_path.mkdir(exist_ok=True, parents=True)
    
    success_count = 0
    for ticket in tickets:
        ticket_id = ticket.get('id', '')
        if ticket_id in keywords_by_id:
            # Create enriched ticket with keywords
            enriched_ticket = ticket.copy()
            enriched_ticket['keywords'] = keywords_by_id[ticket_id]
            
            # Save to output directory
            output_file = output_path / f"{ticket_id}.json"
            with open(output_file, "w") as f:
                json.dump(enriched_ticket, f, indent=2)
            success_count += 1
        else:
            logger.warning(f"No keywords found for ticket {ticket_id}, skipping")
    
    logger.info(f"Saved {success_count} enriched tickets to {output_dir}")

def main():
    """Main function."""
    args = parse_args()
    
    # Initialize OpenAI client
    api_key = args.api_key or os.environ.get("OPENAI_API_KEY")
    if not api_key:
        raise ValueError("OpenAI API key must be provided via --api-key or OPENAI_API_KEY environment variable")
    
    client = OpenAI(api_key=api_key)
    
    try:
        # Load tickets
        tickets = load_tickets(args.input, args.max_tickets)
        if not tickets:
            logger.warning("No tickets found. Exiting.")
            return
        
        keywords_by_id = {}
        
        # Process tickets
        if args.direct:
            # Use direct API calls if specified
            keywords_by_id = process_tickets_directly(client, tickets, args.model)
        else:
            # Try batch processing first, fall back to direct if it fails
            try:
                batch_file = create_batch_tasks(tickets, args.model)
                keywords_by_id = process_batch(client, batch_file)
                # Clean up temporary file
                Path(batch_file).unlink(missing_ok=True)
            except Exception as e:
                logger.error(f"Batch processing failed: {str(e)}")
                logger.info("Falling back to direct API calls...")
                keywords_by_id = process_tickets_directly(client, tickets, args.model)
        
        # Save enriched tickets
        save_enriched_tickets(tickets, keywords_by_id, args.output)
        logger.info("Processing completed successfully")
        
    except Exception as e:
        logger.error(f"Error: {str(e)}")
        raise

if __name__ == "__main__":
    main()