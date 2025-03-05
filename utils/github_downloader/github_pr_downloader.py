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
class GitHubMinimalPRDownloader:
    def __init__(self, owner, repo, token=None, output_dir="raw_pr_data"):
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
        """Get a batch of PR numbers for the specified page"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls"
        params = {"state": "all", "page": page, "per_page": per_page}
        response = self.session.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        
        # Extract just the PR numbers and essential info
        return [{"number": pr["number"], "title": pr["title"]} for pr in response.json()]
    
    def extract_user_data(self, user_obj):
        """Extract only relevant user data"""
        if not user_obj:
            return None
        return {"login": user_obj.get("login")}
    
    def extract_file_data(self, file_obj):
        """Extract only relevant file data"""
        return {
            "filename": file_obj.get("filename"),
            "status": file_obj.get("status"),
            "additions": file_obj.get("additions"),
            "deletions": file_obj.get("deletions"),
            "changes": file_obj.get("changes"),
            "patch": file_obj.get("patch")
        }
    
    def extract_review_data(self, review_obj):
        """Extract only relevant review data"""
        return {
            "user": self.extract_user_data(review_obj.get("user")),
            "state": review_obj.get("state"),
            "body": review_obj.get("body")
        }
    
    def extract_comment_data(self, comment_obj):
        """Extract only relevant comment data"""
        return {
            "user": self.extract_user_data(comment_obj.get("user")),
            "body": comment_obj.get("body"),
            "created_at": comment_obj.get("created_at")
        }
    
    def extract_commit_data(self, commit_obj):
        """Extract only relevant commit data"""
        return {
            "sha": commit_obj.get("sha"),
            "message": commit_obj.get("commit", {}).get("message"),
            "author": self.extract_user_data(commit_obj.get("author"))
        }
    
    def get_pr_details(self, pr_number):
        """Get essential PR details"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        
        pr_data = response.json()
        
        # Extract only the relevant fields
        return {
            "id": pr_number,
            "title": pr_data.get("title"),
            "body": pr_data.get("body"),
            "user": self.extract_user_data(pr_data.get("user")),
            "created_at": pr_data.get("created_at"),
            "updated_at": pr_data.get("updated_at"),
            "merged_at": pr_data.get("merged_at"),
            "closed_at": pr_data.get("closed_at"),
            "state": pr_data.get("state"),
            "merged": pr_data.get("merged"),
            "base_branch": pr_data.get("base", {}).get("ref"),
            "head_branch": pr_data.get("head", {}).get("ref")
        }
    
    def get_pr_files(self, pr_number):
        """Get files changed in a PR with minimal data"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}/files"
        all_files = []
        page = 1
        
        while True:
            params = {"page": page, "per_page": 100}
            response = self.session.get(url, headers=self.headers, params=params)
            response.raise_for_status()
            
            # Extract only essential file data
            files_batch = [self.extract_file_data(f) for f in response.json()]
            all_files.extend(files_batch)
            
            if len(files_batch) < 100:
                break
            
            page += 1
            time.sleep(0.1)
        
        return all_files
    
    def get_pr_reviews(self, pr_number):
        """Get reviews for a PR with minimal data"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}/reviews"
        response = self.session.get(url, headers=self.headers)
        if response.status_code == 404:
            return []
        response.raise_for_status()
        
        # Extract only essential review data
        return [self.extract_review_data(r) for r in response.json()]
    
    def get_pr_comments(self, pr_number):
        """Get comments on a PR with minimal data"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/issues/{pr_number}/comments"
        response = self.session.get(url, headers=self.headers)
        response.raise_for_status()
        
        # Extract only essential comment data
        return [self.extract_comment_data(c) for c in response.json()]
    
    def extract_issue_numbers(self, text):
        """Extract issue/PR numbers from text"""
        if not text:
            return []
        
        # Common patterns for issue references
        import re
        issue_refs = set()
        
        # Find #XX references
        hash_refs = re.findall(r'#(\d+)', text)
        issue_refs.update(hash_refs)
        
        # Find "fixes/closes/resolves" references
        action_refs = re.findall(r'(?:close[sd]?|fix(?:e[sd])?|resolve[sd]?)\s+#(\d+)', text, re.IGNORECASE)
        issue_refs.update(action_refs)
        
        return list(issue_refs)
    
    def download_pr(self, pr_batch_item):
        """Download a PR with minimal necessary data"""
        try:
            pr_number = pr_batch_item["number"]
            
            # Get PR details
            pr_details = self.get_pr_details(pr_number)
            
            # Get files, reviews, and comments
            pr_files = self.get_pr_files(pr_number)
            pr_reviews = self.get_pr_reviews(pr_number)
            pr_comments = self.get_pr_comments(pr_number)
            
            # Extract related issues from body
            related_issues = self.extract_issue_numbers(pr_details.get("body", ""))
            
            # Combine into the minimal structure
            minimal_pr = {
                "id": pr_number,
                "title": pr_details.get("title"),
                "body": pr_details.get("body"),
                "author": pr_details.get("user", {}).get("login"),
                "created_at": pr_details.get("created_at"),
                "merged_at": pr_details.get("merged_at"),
                "state": pr_details.get("state"),
                "base_branch": pr_details.get("base_branch"),
                "head_branch": pr_details.get("head_branch"),
                "related_issues": related_issues,
                "files": pr_files,
                "reviews": pr_reviews,
                "comments": pr_comments
            }
            
            # Save to file
            filename = os.path.join(self.output_dir, f"raw_pr_{pr_number}.json")
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(minimal_pr, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error downloading PR #{pr_number}: {str(e)}")
            return False
    
    def download_all_prs(self, max_workers=10):
        """Download all PRs using multi-threading with minimal data"""
        # Get all PR numbers first
        pr_batch_items = []
        page = 1
        per_page = 100
        
        print(f"Collecting PR numbers from {self.owner}/{self.repo}...")
        while True:
            batch = self.get_pr_batch(page, per_page)
            if not batch:
                break
                
            pr_batch_items.extend(batch)
            if len(batch) < per_page:
                break
                
            page += 1
            time.sleep(0.1)
        
        total_prs = len(pr_batch_items)
        print(f"Found {total_prs} pull requests. Downloading minimal data...")
        
        # Download PRs in parallel using ThreadPoolExecutor
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(tqdm(
                executor.map(self.download_pr, pr_batch_items),
                total=total_prs,
                desc="Downloading PRs",
                unit="PR"
            ))
        
        # Report results
        successful = results.count(True)
        print(f"Downloaded {successful} of {total_prs} pull requests")
        print(f"PR data saved to {os.path.abspath(self.output_dir)}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Download minimal GitHub PR data")
    parser.add_argument("owner", help="Repository owner/organization")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("--token", "-t", help="GitHub API token")
    parser.add_argument("--output", "-o", default="raw_pr_data", help="Output directory")
    parser.add_argument("--workers", "-w", type=int, default=10, help="Number of worker threads")
    args = parser.parse_args()
    
    # Use environment variable for token if not provided as argument
    token = args.token or os.environ.get("GITHUB_TOKEN")
    
    downloader = GitHubMinimalPRDownloader(
        owner=args.owner,
        repo=args.repo,
        token=token,
        output_dir=args.output
    )
    
    downloader.download_all_prs(max_workers=args.workers)