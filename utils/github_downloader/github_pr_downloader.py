import requests
import json
import os
import time
import argparse
import concurrent.futures
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry
from dotenv import load_dotenv
load_dotenv()

class GitHubPRDownloader:
    def __init__(self, owner, repo, token=None, output_dir="pr_data"):
        self.owner = owner
        self.repo = repo
        self.output_dir = output_dir
        
        # Set up headers
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        
        if token:
            self.headers["Authorization"] = f"token {token}"
        
        # Create a session with retry capability
        self.session = requests.Session()
        retry_strategy = Retry(
            total=5,
            backoff_factor=0.5,
            status_forcelist=[429, 500, 502, 503, 504],
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        self.session.mount("https://", adapter)
        self.session.mount("http://", adapter)
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
    
    def get_pr_batch(self, page, per_page=100):
        """Get a batch of PRs for the specified page"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls"
        params = {"state": "all", "page": page, "per_page": per_page}
        response = self.session.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_pr_details(self, pr_number):
        """Get minimal PR details"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        return response.json()
    
    def get_pr_files(self, pr_number):
        """Get list of files changed in a PR"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}/files"
        all_files = []
        page = 1
        
        while True:
            params = {"page": page, "per_page": 100}
            response = self.session.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            files_batch = response.json()
            all_files.extend(files_batch)
            
            # Check if we've got all files
            if len(files_batch) < 100:
                break
            
            page += 1
            time.sleep(0.1)  # Respect rate limits
            
        return all_files
    
    def get_pr_reviews(self, pr_number):
        """Get reviews for a PR"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}/reviews"
        response = self.session.get(url, headers=self.headers)
        if response.status_code == 404:
            return []
        response.raise_for_status()
        return response.json()
    
    def get_linked_issue(self, pr_details):
        """Get linked issue if available"""
        issue_number = None
        body = pr_details.get("body", "")
        
        # Check for linked issues in the body
        if body:
            # Look for common formats like "Fixes #123" or "Closes #123"
            import re
            issue_patterns = [
                r"(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)",
                r"(?:issue|#)(\d+)"
            ]
            
            for pattern in issue_patterns:
                matches = re.findall(pattern, body, re.IGNORECASE)
                if matches:
                    issue_number = matches[0]
                    break
        
        if issue_number:
            try:
                url = f"https://api.github.com/repos/{self.owner}/{self.repo}/issues/{issue_number}"
                response = self.session.get(url, headers=self.headers)
                if response.status_code == 200:
                    return response.json()
            except Exception:
                pass
        
        return None
    
    def get_readme(self):
        """Get repository README content"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/readme"
        try:
            response = self.session.get(url, headers=self.headers)
            if response.status_code == 200:
                content_base64 = response.json().get("content", "")
                import base64
                return base64.b64decode(content_base64).decode('utf-8')
        except Exception:
            pass
        return None
    
    def download_pr(self, pr_number):
        """Download a PR and save only the specified fields"""
        try:
            # Get PR basic details
            pr_details = self.get_pr_details(pr_number)
            
            # Get files changed in PR
            pr_files = self.get_pr_files(pr_number)
            
            # Get reviews
            pr_reviews = self.get_pr_reviews(pr_number)
            
            # Get linked issues
            linked_issues = self.get_linked_issue(pr_details)
            
            # Get README once and reuse for all PRs
            if not hasattr(self, 'readme_content'):
                self.readme_content = self.get_readme()
            
            # Create simplified PR data structure with only required fields
            simplified_pr = {
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
                "readme": self.readme_content if self.readme_content else "No README found"
            }
            
            # Save to file
            filename = os.path.join(self.output_dir, f"pr_{pr_number}.json")
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(simplified_pr, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error downloading PR #{pr_number}: {str(e)}")
            return False
    
    def download_all_prs(self, max_workers=10):
        """Download all PRs using multi-threading"""
        # Get all PR numbers first
        pr_numbers = []
        page = 1
        per_page = 100
        
        print(f"Collecting PR numbers from {self.owner}/{self.repo}...")
        while True:
            batch = self.get_pr_batch(page, per_page)
            if not batch:
                break
                
            pr_numbers.extend(pr["number"] for pr in batch)
            if len(batch) < per_page:
                break
                
            page += 1
            # Respect GitHub API rate limits
            time.sleep(0.1)
        
        total_prs = len(pr_numbers)
        print(f"Found {total_prs} pull requests. Downloading with selected fields...")
        
        # Download PRs in parallel using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            # Create a progress bar
            results = list(tqdm(
                executor.map(self.download_pr, pr_numbers),
                total=total_prs,
                desc="Downloading PRs",
                unit="PR"
            ))
        
        # Report results
        successful = results.count(True)
        print(f"Downloaded {successful} of {total_prs} pull requests")
        if successful < total_prs:
            print(f"Failed to download {total_prs - successful} pull requests")
        
        print(f"PR data saved to {os.path.abspath(self.output_dir)}")


def main():
    parser = argparse.ArgumentParser(description="Download GitHub Pull Requests with selected fields")
    parser.add_argument("owner", help="Repository owner/organization")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("--token", "-t", help="GitHub API token")
    parser.add_argument("--output", "-o", default="pr_data", help="Output directory")
    parser.add_argument("--workers", "-w", type=int, default=10, help="Number of worker threads")
    args = parser.parse_args()
    
    # Use environment variable for token if not provided as argument
    token = args.token or os.environ.get("GITHUB_TOKEN")
    
    downloader = GitHubPRDownloader(
        owner=args.owner,
        repo=args.repo,
        token=token,
        output_dir=args.output
    )
    
    downloader.download_all_prs(max_workers=args.workers)


if __name__ == "__main__":
    main()