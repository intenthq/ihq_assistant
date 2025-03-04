import os
import json
import requests

# Set your API token
API_KEY = os.environ.get("LINEAR_API_KEY")
API_URL = "https://api.linear.app/graphql"

output_folder = "documents/linear"
# PROJECT_ID="5aab670f-1457-43cf-b606-8bcb3ebd55ff"
PROJECT_ID="1c3bfefd-de6d-4fbe-a39d-ba3a4e35bb8c"

# GraphQL query to fetch all issues in the project
query = """
query {
  project(id: "%s") {
    issues(first: 100) {
      nodes {
        id
        title
        description
        state {
          name
        }
        assignee {
          name
        }
        createdAt
        updatedAt
        url
      }
    }
  }
}
""" % PROJECT_ID

# Set headers
headers = {
    "Authorization": API_KEY,
    "Content-Type": "application/json"
}

# Make the API request
response = requests.post(API_URL, json={"query": query}, headers=headers)

# Parse and save each issue in a separate file
if response.status_code == 200:
    issues_data = response.json()["data"]["project"]["issues"]["nodes"]
    
    for issue in issues_data:
        issue_id = issue["id"]
        file_path = os.path.join(output_folder, f"{issue_id}.json")
        
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(issue, f, indent=4)

    print(f"✅ Successfully saved {len(issues_data)} issues as separate JSON files in '{output_folder}/'")
else:
    print("❌ Error:", response.status_code, response.text)