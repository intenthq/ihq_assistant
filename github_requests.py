import os
import requests
import json

# Replace with your GitHub token and repo details
GITHUB_TOKEN = os.environ.get("GITHUB_HACKATHON_API_KEY")  # Your GitHub token
ORG_NAME = "intenthq"  # Your GitHub org name
REPO_NAME = "mle"  # The repository name
PR_NUMBER = 547  # Replace with the PR number you want to fetch

# API base URL
BASE_URL = f"https://api.github.com/repos/{ORG_NAME}/{REPO_NAME}"

# Headers for authentication
headers = {
    "Authorization": f"Bearer {GITHUB_TOKEN}",
    "Accept": "application/vnd.github.v3+json"
}

# Function to fetch PR details
def fetch_pr_details():
    url = f"{BASE_URL}/pulls/{PR_NUMBER}"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Function to fetch PR changed files
def fetch_pr_files():
    url = f"{BASE_URL}/pulls/{PR_NUMBER}/files"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Function to fetch PR comments & reviews
def fetch_pr_reviews():
    url = f"{BASE_URL}/pulls/{PR_NUMBER}/reviews"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Function to fetch issues linked to this PR
def fetch_linked_issues():
    url = f"{BASE_URL}/issues/{PR_NUMBER}"
    response = requests.get(url, headers=headers)
    return response.json() if response.status_code == 200 else None

# Function to fetch repo README for context
import base64

def fetch_repo_readme():
    url = f"{BASE_URL}/readme"
    response = requests.get(url, headers=headers)
    
    if response.status_code == 200:
        content = response.json()["content"]
        
        # Correctly decode Base64 content
        decoded_content = base64.b64decode(content).decode("utf-8")
        
        return decoded_content
    return None

# Fetch all PR details
pr_details = fetch_pr_details()
pr_files = fetch_pr_files()
pr_reviews = fetch_pr_reviews()
linked_issues = fetch_linked_issues()
readme_content = fetch_repo_readme()

# Format extracted data
if pr_details:
    pr_data = {
        "title": pr_details.get("title"),
        "description": pr_details.get("body"),
        "author": pr_details.get("user", {}).get("login"),
        "created_at": pr_details.get("created_at"),
        "changed_files": [
            {"filename": f["filename"], "patch": f.get("patch", "")}
            for f in (pr_files or [])
        ],
        "reviews": [
            {"user": r["user"]["login"], "state": r["state"], "body": r["body"]}
            for r in (pr_reviews or [])
        ],
        "linked_issues": linked_issues.get("title") if linked_issues else "No linked issues",
        "readme": readme_content if readme_content else "No README found"
    }

    # Save to JSON file
    with open(f"PR_{PR_NUMBER}_details.json", "w", encoding="utf-8") as f:
        json.dump(pr_data, f, indent=4)

    print(f"✅ PR details saved as PR_{PR_NUMBER}_details.json")
else:
    print("❌ Failed to fetch PR details.")