import requests
import json
import os
import time
import argparse
import concurrent.futures
from tqdm import tqdm
from requests.adapters import HTTPAdapter
from urllib3.util.retry import Retry

class GitHubPRDownloader:
    def __init__(self, owner, repo, token=None, output_dir="pr_data", include_diffs=True):
        self.owner = owner
        self.repo = repo
        self.output_dir = output_dir
        self.include_diffs = include_diffs
        
        # Set up headers
        self.headers = {"Accept": "application/vnd.github.v3+json"}
        if include_diffs:
            # Request diffs in the response
            self.diff_headers = {
                "Accept": "application/vnd.github.v3.diff"
            }
        
        if token:
            self.headers["Authorization"] = f"token {token}"
            if include_diffs:
                self.diff_headers["Authorization"] = f"token {token}"
        
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
    
    def get_total_pr_count(self):
        """Get the total number of PRs in the repository"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls"
        params = {"state": "all", "per_page": 1}
        response = self.session.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        
        # Check if Link header exists to get pagination info
        if "Link" in response.headers:
            links = response.headers["Link"]
            last_page_match = [link for link in links.split(",") if 'rel="last"' in link]
            if last_page_match:
                last_page_url = last_page_match[0].split(";")[0].strip("<>")
                last_page = int(last_page_url.split("page=")[1].split("&")[0])
                
                # Get per_page value
                per_page = int(params["per_page"])
                return (last_page - 1) * per_page + len(response.json())
        
        return len(self.get_pr_batch(1, 100))
    
    def get_pr_batch(self, page, per_page=100):
        """Get a batch of PRs for the specified page"""
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls"
        params = {"state": "all", "page": page, "per_page": per_page}
        response = self.session.get(url, headers=self.headers, params=params)
        response.raise_for_status()
        return response.json()
    
    def get_pr_details(self, pr_number):
        """Get detailed information for a specific PR"""
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
    
    def get_pr_diff(self, pr_number):
        """Get the full diff for a PR"""
        if not self.include_diffs:
            return None
            
        url = f"https://api.github.com/repos/{self.owner}/{self.repo}/pulls/{pr_number}"
        response = self.session.get(url, headers=self.diff_headers)
        response.raise_for_status()
        return response.text
    
    def download_pr(self, pr_number):
        """Download a PR and save it as a JSON file with all file changes"""
        try:
            # Get PR metadata
            pr_data = self.get_pr_details(pr_number)
            
            # Get files changed in PR
            pr_files = self.get_pr_files(pr_number)
            
            # Add files to PR data
            pr_data['files'] = pr_files
            
            # Get raw diff if requested
            if self.include_diffs:
                pr_data['raw_diff'] = self.get_pr_diff(pr_number)
            
            # Save to file
            filename = os.path.join(self.output_dir, f"pr_{pr_number}.json")
            with open(filename, 'w', encoding='utf-8') as f:
                json.dump(pr_data, f, indent=2, ensure_ascii=False)
            
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
        print(f"Found {total_prs} pull requests. Downloading with file changes...")
        
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
    parser = argparse.ArgumentParser(description="Download GitHub Pull Requests as JSON files")
    parser.add_argument("owner", help="Repository owner/organization")
    parser.add_argument("repo", help="Repository name")
    parser.add_argument("--token", "-t", help="GitHub API token")
    parser.add_argument("--output", "-o", default="pr_data", help="Output directory")
    parser.add_argument("--workers", "-w", type=int, default=10, help="Number of worker threads")
    parser.add_argument("--no-diffs", action="store_true", help="Skip downloading raw diffs")
    args = parser.parse_args()
    
    # Use environment variable for token if not provided as argument
    token = args.token or os.environ.get("GITHUB_TOKEN")
    
    downloader = GitHubPRDownloader(
        owner=args.owner,
        repo=args.repo,
        token=token,
        output_dir=args.output,
        include_diffs=not args.no_diffs
    )
    
    downloader.download_all_prs(max_workers=args.workers)


if __name__ == "__main__":
    main()