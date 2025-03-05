# Output Format
Each PR is saved as a JSON file with this structure:
```json
{
  "id": 123,
  "title": "Add OAuth2 authentication",
  "body": "This PR implements OAuth2 authentication for our API...",
  "author": "username",
  "created_at": "2023-05-20T14:53:02Z",
  "merged_at": "2023-05-23T09:15:43Z",
  "state": "closed",
  "base_branch": "main",
  "head_branch": "feature/oauth",
  "related_issues": ["42", "57"],
  "files": [
    {
      "filename": "auth/oauth.py",
      "status": "added",
      "additions": 120,
      "deletions": 0,
      "changes": 120,
      "patch": "@@ -0,0 +1,45 @@\n+class OAuth2Provider:\n+    def __init__(self, client_id, client_secret):\n+        self.client_id = client_id..."
    }
  ],
  "reviews": [
    {
      "user": {"login": "reviewer"},
      "state": "APPROVED",
      "body": "Looks good! Just a few minor suggestions."
    }
  ],
  "comments": [
    {
      "user": {"login": "teammate"},
      "body": "Should we add rate limiting to prevent abuse?",
      "created_at": "2023-05-21T10:22:15Z"
    }
  ]
}
```

# Usage 
## Basic usage
```bash
python github_pr_downloader.py username repo-name
```

## With GitHub token (recommended to avoid rate limiting)
```bsh
python github_pr_downloader.py username repo-name --token YOUR_TOKEN
```

## Or use environment variable
```bash
export GITHUB_TOKEN=your_token
python github_pr_downloader.py username repo-name
```

## Customize output directory
```bash
python github_pr_downloader.py username repo-name -o ./my_prs
```

## Adjust number of worker threads
```bash
python github_pr_downloader.py username repo-name -w 15
```

# Notes
- GitHub API has a rate limit (60 requests/hour for unauthenticated users, 5000/hour with a token)
- For repos with many PRs or many changed files, downloads may take time
- For very large repos, consider reducing thread count to avoid hitting rate limits
