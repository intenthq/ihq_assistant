import json
import os
import re
import argparse
import concurrent.futures
from tqdm import tqdm
from collections import defaultdict
#import networkx as nx
#import matplotlib.pyplot as plt
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

from code_parser import CodeParser
from llm_integration import LLMAnalyzer

class PRAnalyzer:
    """Analyzes PR data using tree-sitter and LLM"""
    
    def __init__(self, raw_data_dir, output_dir="analyzed_pr_data", use_llm=True, llm_api_key=None):
        self.raw_data_dir = raw_data_dir
        self.output_dir = output_dir
        self.use_llm = use_llm
        
        # Initialize code parser and LLM analyzer
        self.code_parser = CodeParser()
        self.llm = LLMAnalyzer(llm_api_key) if use_llm else None
        
        # Cache for PR relationships
        self.pr_relationships = defaultdict(list)
        
        # Ensure output directory exists
        os.makedirs(self.output_dir, exist_ok=True)
        
        # Build relationships between PRs
        self.build_pr_relationships()
    

    def build_pr_relationships(self):
        """Build a map of relationships between PRs"""
        print("Building PR relationship graph...")
        for filename in os.listdir(self.raw_data_dir):
            if not filename.startswith("raw_pr_") or not filename.endswith(".json"):
                continue
                
            with open(os.path.join(self.raw_data_dir, filename), 'r') as f:
                pr_data = json.load(f)
                
            pr_id = pr_data["id"]
            
            # Add relationships based on related issues
            for related_id_str in pr_data.get("related_issues", []):
                try:
                    related_id = int(related_id_str)
                    self.pr_relationships[pr_id].append(related_id)
                    self.pr_relationships[related_id].append(pr_id)
                except ValueError:
                    pass
        
        # Remove duplicates
        for pr_id in self.pr_relationships:
            self.pr_relationships[pr_id] = list(set(self.pr_relationships[pr_id]))
    
    def extract_development_purpose(self, pr_data):
        """Extract the purpose of the development using heuristics"""
        title = pr_data.get("title", "")
        body = pr_data.get("body", "")
        
        # Start with title as basic purpose
        purpose = title
        
        # Try to extract more detailed purpose from body
        if body:
            # Look for sections like "Purpose:" or "## Description"
            purpose_patterns = [
                r"(?:Purpose|Goal|Objective):\s*(.+?)(?:\n\n|\n#|\Z)",
                r"(?:##?\s*Description|##?\s*Overview)\s*(.+?)(?:\n\n|\n#|\Z)",
                r"(?:This PR|This pull request)\s+(?:adds|implements|fixes|updates)\s+(.+?)(?:\.|\$)"
            ]
            
            for pattern in purpose_patterns:
                matches = re.search(pattern, body, re.IGNORECASE | re.DOTALL)
                if matches:
                    extracted = matches.group(1).strip()
                    if len(extracted) > len(purpose):
                        purpose = extracted
                    break
        
        return purpose
    
    def extract_review_insights(self, reviews, comments):
        """Extract insights from review comments"""
        if not reviews and not comments:
            return {
                "reviewers": [],
                "sentiment": "None",
                "key_points": []
            }
        
        reviewers = list(set(r.get("user", {}).get("login") for r in reviews if r.get("user")))
        
        # Extract review states
        states = [r.get("state") for r in reviews if r.get("state")]
        sentiment = "Positive" if states and all(s == "APPROVED" for s in states) else "Mixed"
        
        # Extract key discussion points using heuristics
        all_comments = []
        for r in reviews:
            if r.get("body"):
                all_comments.append(r.get("body"))
        
        for c in comments:
            if c.get("body"):
                all_comments.append(c.get("body"))
        
        # Find comments that look like important feedback
        key_points = []
        feedback_indicators = [
            "suggest", "should", "could", "would be better", "recommend",
            "instead", "prefer", "what if", "why not", "concern", "issue"
        ]
        
        for comment in all_comments:
            sentences = re.split(r'[.!?]+', comment)
            for sentence in sentences:
                sentence = sentence.strip()
                if any(indicator in sentence.lower() for indicator in feedback_indicators):
                    if len(sentence) > 10:  # Avoid tiny fragments
                        key_points.append(sentence)
        
        return {
            "reviewers": reviewers,
            "sentiment": sentiment,
            "key_points": key_points[:5]  # Limit to top 5 points
        }
    
    # def visualize_code_changes(self, pr_id, code_changes):
    #     """Generate visualization of code changes using NetworkX"""
    #     try:
    #         # Create a graph of function calls
    #         G = nx.DiGraph()
            
    #         # Add nodes for all functions
    #         added_functions = []
    #         modified_functions = []
    #         removed_functions = []
            
    #         for file_change in code_changes:
    #             if "functions" in file_change:
    #                 added_functions.extend(file_change["functions"].get("added", []))
    #                 modified_functions.extend(file_change["functions"].get("modified", []))
    #                 removed_functions.extend(file_change["functions"].get("removed", []))
            
    #         # Add nodes with different colors
    #         for func in added_functions:
    #             G.add_node(func, color="green")
    #         for func in modified_functions:
    #             G.add_node(func, color="orange")
    #         for func in removed_functions:
    #             G.add_node(func, color="red")
            
    #         # Add edges based on function calls
    #         for file_change in code_changes:
    #             if "function_calls" in file_change:
    #                 for call in file_change.get("function_calls", []):
    #                     # Find if this call corresponds to a function we know about
    #                     for func in G.nodes():
    #                         if call == func:
    #                             # Add edges from all modified functions to this call
    #                             for source_func in modified_functions:
    #                                 if source_func != call:
    #                                     G.add_edge(source_func, call)
            
    #         # If graph is too small, don't bother visualizing
    #         if len(G.nodes()) <= 1:
    #             return None
                
    #         # Generate the visualization
    #         plt.figure(figsize=(10, 8))
    #         pos = nx.spring_layout(G)
            
    #         # Draw nodes with different colors
    #         node_colors = [G.nodes[n].get("color", "blue") for n in G.nodes()]
    #         nx.draw_networkx_nodes(G, pos, node_color=node_colors, alpha=0.8)
    #         nx.draw_networkx_edges(G, pos, edge_color="gray", alpha=0.5)
    #         nx.draw_networkx_labels(G, pos, font_size=10)
            
    #         plt.title(f"Code Structure Changes in PR #{pr_id}")
    #         plt.axis("off")
            
    #         # Save figure
    #         viz_dir = os.path.join(self.output_dir, "visualizations")
    #         os.makedirs(viz_dir, exist_ok=True)
    #         viz_path = os.path.join(viz_dir, f"pr_{pr_id}_code_graph.png")
    #         plt.savefig(viz_path)
    #         plt.close()
            
    #         return viz_path
    #     except Exception as e:
    #         print(f"Visualization error: {str(e)}")
    #         return None
    
    def analyze_pr(self, pr_file):
        """Analyze a single PR from its raw data file"""
        try:
            with open(os.path.join(self.raw_data_dir, pr_file), 'r') as f:
                raw_pr = json.load(f)
            
            pr_id = raw_pr["id"]
            
            # Analyze code changes using tree-sitter
            code_change_analysis = []
            for file_data in raw_pr.get("files", []):
                # Skip very large files or certain types of files
                if file_data.get("changes", 0) > 10000 or file_data.get("filename", "").endswith((".lock", ".min.js")):
                    code_change_analysis.append({
                        "filename": file_data.get("filename"),
                        "status": file_data.get("status"),
                        "changes": "File too large for detailed analysis"
                    })
                    continue
                
                # Perform structural code analysis
                analysis = self.code_parser.analyze_file_changes(file_data)
                code_change_analysis.append(analysis)
            
            # Group changes by language
            language_changes = defaultdict(lambda: {
                "files": [],
                "added_functions": [],
                "modified_functions": [],
                "removed_functions": [],
                "added_classes": [],
                "modified_classes": [],
                "removed_classes": []
            })
            
            for change in code_change_analysis:
                lang = change.get("language", "unknown")
                language_changes[lang]["files"].append(change.get("filename"))
                
                if "functions" in change:
                    language_changes[lang]["added_functions"].extend(change["functions"].get("added", []))
                    language_changes[lang]["modified_functions"].extend(change["functions"].get("modified", []))
                    language_changes[lang]["removed_functions"].extend(change["functions"].get("removed", []))
                
                if "classes" in change:
                    language_changes[lang]["added_classes"].extend(change["classes"].get("added", []))
                    language_changes[lang]["modified_classes"].extend(change["classes"].get("modified", []))
                    language_changes[lang]["removed_classes"].extend(change["classes"].get("removed", []))
            
            # Generate visualization of code changes
            # visualization_path = self.visualize_code_changes(pr_id, code_change_analysis)
            
            # Traditional analysis
            development_purpose = self.extract_development_purpose(raw_pr)
            review_insights = self.extract_review_insights(
                raw_pr.get("reviews", []), 
                raw_pr.get("comments", [])
            )
            
            # Prepare a summary for LLM analysis
            pr_summary = {
                "id": pr_id,
                "title": raw_pr.get("title"),
                "description": raw_pr.get("body"),
                "code_changes_summary": {
                    lang: {
                        "file_count": len(changes["files"]),
                        "added_functions": changes["added_functions"],
                        "modified_functions": changes["modified_functions"],
                        "removed_functions": changes["removed_functions"],
                        "added_classes": changes["added_classes"],
                        "modified_classes": changes["modified_classes"],
                        "removed_classes": changes["removed_classes"]
                    }
                    for lang, changes in language_changes.items() 
                    if lang != "unknown"
                }
            }
            
            # LLM-based analysis if enabled
            llm_insights = self.llm.analyze_pr(pr_summary) if self.use_llm and self.llm else {}
            
            # Combine all insights into the final structure
            analyzed_pr = {
                "id": pr_id,
                "title": raw_pr.get("title"),
                "author": raw_pr.get("author"),
                "created_at": raw_pr.get("created_at"),
                "merged_at": raw_pr.get("merged_at"),
                "state": raw_pr.get("state"),
                
                "development_context": {
                    "purpose": development_purpose,
                    "branches": {
                        "base": raw_pr.get("base_branch"),
                        "head": raw_pr.get("head_branch")
                    },
                    "related_prs": self.pr_relationships.get(pr_id, []),
                },
                
                "code_analysis": {
                    "languages": [lang for lang in language_changes.keys() if lang != "unknown"],
                    "language_breakdown": {
                        lang: len(changes["files"]) 
                        for lang, changes in language_changes.items()
                        if lang != "unknown"
                    },
                    "structural_changes": {
                        lang: {
                            "added_functions": list(set(changes["added_functions"])),
                            "modified_functions": list(set(changes["modified_functions"])),
                            "removed_functions": list(set(changes["removed_functions"])),
                            "added_classes": list(set(changes["added_classes"])),
                            "modified_classes": list(set(changes["modified_classes"])),
                            "removed_classes": list(set(changes["removed_classes"]))
                        }
                        for lang, changes in language_changes.items()
                        if lang != "unknown"
                    },
                    #"visualization": os.path.basename(visualization_path) if visualization_path else None,
                    "detailed_file_analysis": code_change_analysis[:10]  # Limit to 10 files
                },
                
                "review_context": review_insights,
                
                "llm_insights": llm_insights
            }
            
            # Save analyzed PR
            output_file = os.path.join(self.output_dir, f"analyzed_pr_{pr_id}.json")
            with open(output_file, 'w', encoding='utf-8') as f:
                json.dump(analyzed_pr, f, indent=2, ensure_ascii=False)
            
            return True
        except Exception as e:
            print(f"Error analyzing PR file {pr_file}: {str(e)}")
            return False
    
    def analyze_all(self, max_workers=4):
        """Analyze all raw PR data files"""
        raw_files = [f for f in os.listdir(self.raw_data_dir) 
                    if f.startswith("raw_pr_") and f.endswith(".json")]
        
        print(f"Analyzing {len(raw_files)} PRs with tree-sitter code structure analysis...")
        
        # Use ThreadPoolExecutor instead of ProcessPoolExecutor
        # This avoids pickle errors since threads share memory
        with concurrent.futures.ThreadPoolExecutor(max_workers=max_workers) as executor:
            results = list(tqdm(
                executor.map(self.analyze_pr, raw_files),
                total=len(raw_files),
                desc="Analyzing PRs",
                unit="PR"
            ))
        
        successful = results.count(True)
        print(f"Successfully analyzed {successful} of {len(raw_files)} PRs")
        print(f"Analyzed PR data saved to {os.path.abspath(self.output_dir)}")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Analyze GitHub PR data with tree-sitter")
    parser.add_argument("--input", "-i", default="raw_pr_data", help="Directory with raw PR data")
    parser.add_argument("--output", "-o", default="analyzed_pr_data", help="Output directory")
    parser.add_argument("--workers", "-w", type=int, default=4, help="Number of worker processes")
    parser.add_argument("--no-llm", action="store_true", help="Disable LLM-based analysis")
    parser.add_argument("--llm-key", help="API key for LLM provider")
    args = parser.parse_args()
    
    analyzer = PRAnalyzer(
        raw_data_dir=args.input,
        output_dir=args.output,
        use_llm=not args.no_llm,
        llm_api_key=args.llm_key
    )
    
    analyzer.analyze_all(max_workers=args.workers)