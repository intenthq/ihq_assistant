
# Output Format
Each PR is saved as a JSON file with this structure:

```json
{
  "id": 6,
  "title": "tidy up execute_query params",
  "author": "cdagraca",
  "created_at": "2025-03-04T16:02:12Z",
  "merged_at": "2025-03-04T16:22:45Z",
  "state": "closed",
  "development_context": {
    "purpose": "tidy up execute_query params",
    "branches": {
      "base": "main",
      "head": "function_param_types"
    },
    "related_prs": []
  },
  "code_analysis": {
    "languages": [
      "python"
    ],
    "language_breakdown": {
      "python": 2
    },
    "structural_changes": {
      "python": {
        "added_functions": [],
        "modified_functions": [],
        "removed_functions": [],
        "added_classes": [],
        "modified_classes": [],
        "removed_classes": []
      }
    },
    "detailed_file_analysis": [
      {
        "filename": "db/linear_embeddings.db/index.faiss",
        "status": "added",
        "changes": "Binary file or no patch available"
      },
      {
        "filename": "db/linear_embeddings.db/index.pkl",
        "status": "added",
        "changes": "Binary file or no patch available"
      },
      {
        "language": "python",
        "functions": {
          "added": [],
          "modified": [],
          "removed": [],
          "total_count": 0
        },
        "classes": {
          "added": [],
          "modified": [],
          "removed": [],
          "total_count": 0
        },
        "function_calls": [],
        "filename": "load_vector_db.py",
        "status": "modified"
      },
      {
        "language": "python",
        "functions": {
          "added": [],
          "modified": [],
          "removed": [],
          "total_count": 0
        },
        "classes": {
          "added": [],
          "modified": [],
          "removed": [],
          "total_count": 0
        },
        "function_calls": [],
        "filename": "vectorise_data.py",
        "status": "modified"
      }
    ]
  },
  "review_context": {
    "reviewers": [
      "javierpedreira"
    ],
    "sentiment": "Positive",
    "key_points": []
  },
  "llm_insights": {
    "purpose": "The primary purpose of this PR is to clean up and possibly refactor the parameters used in the 'execute_query' function to improve code readability and maintainability.",
    "technical_approach": "The technical approach likely involves refactoring the function signature of 'execute_query' to streamline its parameters, possibly by consolidating them or removing unnecessary ones.",
    "potential_impact": "These changes could improve the readability and maintainability of the code, making it easier for future developers to understand and work with the 'execute_query' function. However, if not handled carefully, it might introduce bugs if the refactoring affects how the function is called elsewhere in the codebase.",
    "suggested_improvements": [
      "Ensure thorough testing is conducted to verify that the refactored parameters do not break existing functionality.",
      "Update any documentation or comments to reflect the changes made to the function parameters.",
      "Consider adding type hints to the function signature for better clarity and type safety."
    ],
    "key_concepts": [
      "Refactoring",
      "Code readability",
      "Function parameter management"
    ]
  }
}
```

```bash
python github_pr_analyzer.py --input raw_pr_data --output analyzed_pr_data 
```