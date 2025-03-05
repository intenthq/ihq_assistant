# Output Format
Each PR is saved as a JSON file with this structure:
```json
{
  "title": "Feature: Implement new authentication system",
  "description": "This PR adds support for OAuth 2.0 authentication...",
  "author": "username",
  "created_at": "2023-05-20T14:53:02Z",
  "changed_files": [
    {
      "filename": "auth/oauth.py",
      "patch": "@@ -50,7 +50,12 @@ class OAuth:\n     def authenticate(self):\n-        return token\n+        # New implementation\n+        return self.get_token()"
    }
  ],
  "reviews": [
    {
      "user": "reviewer",
      "state": "APPROVED",
      "body": "Looks good to me!"
    }
  ],
  "linked_issues": "Authentication system upgrade",
  "readme": "# Project\nThis is the project README..."
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
