# Basic usage
python github_pr_downloader.py username repo-name

# With GitHub token (recommended to avoid rate limiting)
python github_pr_downloader.py username repo-name --token YOUR_TOKEN

# Or use environment variable
export GITHUB_TOKEN=your_token
python github_pr_downloader.py username repo-name

# Customize output directory
python github_pr_downloader.py username repo-name -o ./my_prs

# Adjust number of worker threads
python github_pr_downloader.py username repo-name -w 15