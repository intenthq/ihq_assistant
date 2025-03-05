# Output Format
Each PR is saved as a JSON file with this structure:
```
{
  // PR metadata (title, description, author, etc.)
  ...
  "files": [
    {
      "sha": "abc123...",
      "filename": "path/to/file.py",
      "status": "modified",
      "additions": 10,
      "deletions": 5,
      "changes": 15,
      "patch": "@@ -50,7 +50,12 @@ class Example:\n     def method(self):\n-        return 42\n+        # New implementation\n+        return 84"
    },
    ...
  ],
  "raw_diff": "diff --git a/file1.py b/file1.py\nindex abc..def 100644\n..."
}
```

# Usage 
## Basic usage
python github_pr_downloader.py username repo-name

## With GitHub token (recommended to avoid rate limiting)
python github_pr_downloader.py username repo-name --token YOUR_TOKEN

## Or use environment variable
export GITHUB_TOKEN=your_token
python github_pr_downloader.py username repo-name

## Customize output directory
python github_pr_downloader.py username repo-name -o ./my_prs

## Adjust number of worker threads
python github_pr_downloader.py username repo-name -w 15

# Notes
    - GitHub API has a rate limit (60 requests/hour for unauthenticated users, 5000/hour with a token)
    - For repos with many PRs or many changed files, downloads may take time
    - For very large repos, consider reducing thread count to avoid hitting rate limits
    - Using `--no-diffs` can significantly speed up downloads if the raw diff text is not needed
