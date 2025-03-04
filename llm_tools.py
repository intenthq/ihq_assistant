import os
import json
import requests
from openai import OpenAI

# Define the function to create a Linear ticket
def create_linear_ticket(title: str, description: str, priority: int, LINEAR_API_KEY: str) -> dict:
    """
    Creates a new Linear ticket using the given title, description, and priority.

    Args:
        title (str): The title of the Linear ticket.
        description (str): A detailed description of the ticket.
        priority (int): Priority level (0 = No priority, 1 = Low, 2 = Medium, 3 = High, 4 = Urgent).

    Returns:
        dict: A dictionary containing ticket details formatted for Linear API.
    """
    TEAM_ID = '16b9a385-762f-47b0-b5d8-73ece3125bd9'
    API_URL = 'https://api.linear.app/graphql'
    headers = {
        'Authorization': LINEAR_API_KEY,
        'Content-Type': 'application/json'
    }

    issue_data = {
        "title": title,
        "description": description,
        "teamId": TEAM_ID,
        "priority": priority
    }

    # GraphQL mutation for creating an issue
    mutation = """
    mutation CreateIssue($input: IssueCreateInput!) {
      issueCreate(input: $input) {
        success
        issue {
          id
          title
          description
          url
        }
      }
    }
    """

    # Make the API request
    response = requests.post(
        API_URL,
        json={"query": mutation, "variables": {"input": issue_data}},
        headers=headers
    )

    if response.status_code == 200:
        data = response.json()
        if data.get('data', {}).get('issueCreate', {}).get('success'):
            issue = data['data']['issueCreate']['issue']
            return {
                "success": True,
                "issue": {
                    "id": issue['id'],
                    "title": issue['title'],
                    "description": issue['description'],
                    "url": issue['url']
                }
            }
        else:
            return {"success": False, "error": "Issue creation failed."}
    else:
        return {"success": False, "error": response.text}

# Define the function specification for OpenAI
tools = [
    {
        "type": "function",  # Specify the type as 'function'
        "function": {
            "name": "create_linear_ticket",
            "description": "Creates a new Linear ticket with the given title, description, and priority.",
            "parameters": {
                "type": "object",
                "properties": {
                    "title": {
                        "type": "string",
                        "description": "The title of the Linear ticket"
                    },
                    "description": {
                        "type": "string",
                        "description": "A detailed description of the issue or task."
                    },
                    "priority": {
                        "type": "integer",
                        "description": "The priority level of the issue. (0 = No priority, 1 = Low, 2 = Medium, 3 = High, 4 = Urgent)",
                        "enum": [0, 1, 2, 3, 4]
                    }
                },
                "required": ["title", "description", "priority"]
            }
        }
    }
]

