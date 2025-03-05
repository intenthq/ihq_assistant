from pydantic import BaseModel, Field
from openai import OpenAI
import os
import json

class PRInsights(BaseModel):
    """Structured output model for PR analysis"""
    purpose: str = Field(
        description="The primary purpose/goal of this PR in 1-2 sentences"
    )
    technical_approach: str = Field(
        description="Brief description of the technical approach used in this PR"
    )
    potential_impact: str = Field(
        description="Assessment of how these changes might impact the codebase or application"
    )
    suggested_improvements: list[str] = Field(
        description="List of potential improvements or suggestions for this code change"
    )
    key_concepts: list[str] = Field(
        description="Key technical concepts or design patterns used in this PR"
    )

class LLMAnalyzer:
    """OpenAI-specific adapter for PR analysis"""
    
    def __init__(self, api_key=None):
        self.api_key = api_key or os.environ.get("OPENAI_API_KEY")
        self.client = OpenAI(api_key=self.api_key) if self.api_key else None
    

    def analyze_pr(self, pr_summary):
        """Use OpenAI to analyze a PR summary and extract insights"""
        if not self.client:
            return {
                "purpose": "OpenAI API key not configured",
                "technical_approach": "Please provide an API key to enable LLM analysis",
                "potential_impact": "N/A",
                "suggested_improvements": ["Configure OpenAI API key"],
                "key_concepts": []
            }
        
        try:
            # Create a summary of the most important aspects for the LLM
            prompt = self._create_prompt(pr_summary)
            
            # Use the parse method with Pydantic model for structured output
            completion = self.client.beta.chat.completions.parse(
                model="gpt-4o-2024-08-06",  # "gpt-4o-2024-11-20" ? "gpt-4o-mini-2024-07-18"?
                messages=[
                    {"role": "system", "content": "You are a code analysis expert. Analyze this PR data and provide structured insights."},
                    {"role": "user", "content": prompt}
                ],
                response_format=PRInsights,
                temperature=0.1,  # Lower temperature for more consistent outputs
            )
            
            # Return the parsed response as a dictionary
            return completion.choices[0].message.parsed.model_dump()
        
        except Exception as e:
            print(f"LLM analysis error: {str(e)}")
            return {
                "purpose": f"Error during analysis: {str(e)}",
                "technical_approach": "Analysis failed",
                "potential_impact": "Unknown due to error",
                "suggested_improvements": ["Check API key configuration"],
                "key_concepts": []
            }
    
    def _create_prompt(self, pr_summary):
        """Create a focused prompt with the most relevant information"""
        # Format the code changes in a more digestible way
        code_changes = []
        if "code_changes_summary" in pr_summary:
            for lang, changes in pr_summary["code_changes_summary"].items():
                code_changes.append(f"\nLanguage: {lang}")
                code_changes.append(f"Files changed: {changes.get('file_count', 0)}")
                
                if changes.get("added_functions"):
                    code_changes.append(f"Added functions: {', '.join(changes['added_functions'])}")
                if changes.get("modified_functions"):
                    code_changes.append(f"Modified functions: {', '.join(changes['modified_functions'])}")
                if changes.get("removed_functions"):
                    code_changes.append(f"Removed functions: {', '.join(changes['removed_functions'])}")
                    
                if changes.get("added_classes"):
                    code_changes.append(f"Added classes: {', '.join(changes['added_classes'])}")
                if changes.get("modified_classes"):
                    code_changes.append(f"Modified classes: {', '.join(changes['modified_classes'])}")
                if changes.get("removed_classes"):
                    code_changes.append(f"Removed classes: {', '.join(changes['removed_classes'])}")
        
        # Create the prompt
        prompt = f"""
PR #{pr_summary.get('id')}: {pr_summary.get('title', 'Untitled PR')}

Description:
{pr_summary.get('description', 'No description provided')}

Code Changes Summary:
{"".join(code_changes)}

Based on this information, analyze the PR to determine its purpose, technical approach, potential impact, suggested improvements, and key technical concepts used.
"""
        return prompt