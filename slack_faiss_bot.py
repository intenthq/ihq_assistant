import os
import json
import numpy as np
import openai
from slack_bolt import App
from slack_bolt.adapter.socket_mode import SocketModeHandler
from dotenv import load_dotenv
import logging
from collections import deque


from openai import OpenAI
from llm_tools import create_linear_ticket, tools
from rag_util_functions import query_all_sources 

# Load environment variables from .env file
load_dotenv()

print("SLACK_BOT_TOKEN:", os.getenv("SLACK_BOT_TOKEN"))
print("SLACK_APP_TOKEN:", os.getenv("SLACK_APP_TOKEN"))
print("OPENAI_API_KEY:", os.getenv("OPENAI_API_KEY"))

# Define API Keys and Tokens from environment variables
SLACK_BOT_TOKEN = os.getenv("SLACK_BOT_TOKEN")
SLACK_APP_TOKEN = os.getenv("SLACK_APP_TOKEN")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
LINEAR_API_KEY = os.environ.get("LINEAR_API_KEY")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")

# Configure OpenAI API Key
openai.api_key = OPENAI_API_KEY
client = OpenAI()

# Enable debug logging
logging.basicConfig(level=logging.DEBUG)

# Memory storage for last 5 mentions
mention_memory = {}  # Key: channel_id, Value: deque of last 5 mentions

# Generate OpenAI embeddings for documents
def get_embedding(text):
    response = openai.embeddings.create(
        input=text, model="text-embedding-ada-002"
    )
    return np.array(response.data[0].embedding, dtype=np.float32)

# Initialize Slack App
app = App(token=SLACK_BOT_TOKEN)

def parse_chat_history(chat_history_raw):
    chat_history = []
    for message in chat_history_raw:
        chat_history.append({"role": "user", "content": message})
    return chat_history

def get_prompt_messages(chat_history, question, context):
    system_prompt = """
        You are a helpful assistant for Intent HQ, an expert on the company's projects, processes, and tools. Your role is to assist employees by providing answers and guidance on various tasks and projects. We operate in an agile environment, following the Shape Up framework.

        You will be provided with context from several key data sources:

        - **Coda**: Our documentation hub, which contains detailed information about ongoing projects, including Shape Up documents.
        - **Linear**: A task and project management tool that tracks project progress. You'll receive task descriptions, assignees, and related metadata.
        - **GitHub**: The source code repository, where you can find details about the codebase, including pull requests and code changes.

        Please use this information to help employees efficiently and effectively with their questions.
    """
    # Start with system message
    messages = [
        {"role": "system", "content": system_prompt},
    ]

    # Add user chat history (must be strings)
    for msg in chat_history:
        messages.append({"role": "user", "content": str(msg)})  # Ensure content is a string

    # Add context
    messages.append({"role": "system", "content": f"This is the relevant context for you to answer the user's query: {context}"})
    
    # Add user question
    messages.append({"role": "user", "content": str(question)})  # Ensure content is a string

    return messages

def chat_openai(messages, tools=None, model="gpt-4o", temperature=0.1):
    # Send request to OpenAI API
    response = client.chat.completions.create(
        model=model,
        messages=messages,
        temperature=temperature,
        tools=tools if tools else []  # Pass an empty list if no tools
    )
    # Return the full response object, not just the message content
    return response.choices[0].message  # Return the full response to access `tool_calls`

def implement_linear_function(function_args):
    function_args = json.loads(function_args)
    result = create_linear_ticket(
        title=function_args.get("title"),
        description=function_args.get("description"),
        priority=int(function_args.get("priority")),
        linear_api_key=LINEAR_API_KEY
    )
    second_message = f"A ticket as been created here: {result['issue']['url']}"
    return second_message

# Function to search FAISS
def search_faiss(query, channel_id, tools):
    docs_content = query_all_sources(query, model="gpt-4o", k=3)

    # Retrieve last 5 messages from memory for this channel
    chat_history = mention_memory.get(channel_id, [])
    chat_history = parse_chat_history(chat_history)
    logging.debug(f"🔹 Chat History for channel {channel_id}: {chat_history}")

    messages = get_prompt_messages(chat_history, query, docs_content)
    response = chat_openai(messages, tools)

    # Check if the response has tool calls and process accordingly
    if hasattr(response, 'tool_calls') and response.tool_calls:
        function_name = response.tool_calls[0].function.name
        function_args = response.tool_calls[0].function.arguments
        if function_name == "create_linear_ticket":
            try:
                response = implement_linear_function(function_args)
            except Exception as e:
                logging.error(f"Error creating ticket: {e}")
                response = "Sorry, failed to create a ticket (still learning!) - can you ask again?"
    else:
        response = response.content
    return response

# Function to store last 5 mentions per channel
def store_mention(channel_id, mention_text):
    if channel_id not in mention_memory:
        mention_memory[channel_id] = deque(maxlen=10)
    mention_memory[channel_id].append(mention_text)
    logging.debug(f"🔹 Updated memory for channel {channel_id}: {list(mention_memory[channel_id])}")

# Slack bot listens for messages that mention it
@app.event("app_mention")
def handle_mention(event, say):
    logging.debug(f"🔹 Received mention event: {event}")  # Debugging log
    user_query = event["text"]
    channel_id = event["channel"]
    
    store_mention(channel_id, user_query)  # Store the mention
    best_match = search_faiss(user_query, channel_id, tools)
    logging.debug(f"🔹 Best FAISS match: {best_match}")
    
    say(f"{best_match}")

# Start the Slack bot using Socket Mode
if __name__ == "__main__":
    handler = SocketModeHandler(app, SLACK_APP_TOKEN)
    handler.start()
