from tree_sitter import Parser
from tree_sitter_language_pack import get_language
import re
import json
from typing import Tuple, List, Dict, Any

class CodeParser:
    """Handles code analysis using tree-sitter with prebuilt language definitions"""
    
    def __init__(self):
        # Initialize parsers with prebuilt language definitions
        self.parsers = {}
        self.supported_languages = {
            "python": get_language("python"),
            "javascript": get_language("javascript"),
            "typescript": get_language("typescript"),
            # "jsx": get_language("javascript"),  # Use JS parser for JSX
            # "tsx": get_language("typescript"),  # Use TS parser for TSX
            "go": get_language("go"),
            # "ruby": get_language("ruby"),
            # "rust": get_language("rust"),
            # "java": get_language("java"),
            # "c": get_language("c"),
            # "cpp": get_language("cpp"),
            # "php": get_language("php"),
            "scala": get_language("scala"),
            "sql": get_language("sql"),
            # "dockerfile": get_language("dockerfile"),
            # "yaml": get_language("yaml"),
            "markdown": get_language("markdown"),
            # "html": get_language("html"),
            # "css": get_language("css"),
            # "bash": get_language("bash"),
            # Note: Jupyter notebooks will use the Python parser
        }
        
        # Create parsers for each language
        for lang, language_obj in self.supported_languages.items():
            parser = Parser(language_obj)
            self.parsers[lang] = parser
        
        print(f"Initialized parsers for {len(self.parsers)} languages")
    
    def get_language_for_file(self, filename):
        """Determine the language based on file extension or name"""
        if not filename:
            return None
            
        # Match by exact filename for special files
        basename = filename.split("/")[-1].lower()
        if basename == "dockerfile":
            return "dockerfile"
        if basename == "makefile":
            return "make"
        
        # Match by extension
        ext = filename.split(".")[-1].lower() if "." in filename else ""
        
        # Map file extensions to tree-sitter languages
        extension_map = {
            "py": "python",
            "ipynb": "jupyter",  # Special handling for Jupyter notebooks
            "js": "javascript",
            "jsx": "jsx",
            "ts": "typescript",
            "tsx": "tsx",
            "go": "go",
            "rb": "ruby",
            "rs": "rust",
            "java": "java",
            "c": "c",
            "cpp": "cpp",
            "cc": "cpp",
            "h": "c",
            "hpp": "cpp",
            "cs": "csharp",
            "php": "php",
            "scala": "scala",
            "sql": "sql",
            "yml": "yaml",
            "yaml": "yaml",
            "md": "markdown",
            "html": "html",
            "htm": "html",
            "css": "css",
            "scss": "css",
            "sh": "bash",
            "bash": "bash"
        }
        
        return extension_map.get(ext)
    
    def extract_python_from_notebook(self, notebook_content: str) -> str:
        """Extract Python code from Jupyter notebook JSON"""
        try:
            # Parse the notebook content as JSON
            notebook = json.loads(notebook_content)
            
            # Collect code from all code cells
            python_code = []
            
            # Check if this is a valid notebook with cells
            if not isinstance(notebook, dict) or "cells" not in notebook:
                return ""
            
            # Process each cell
            for cell in notebook.get("cells", []):
                # Check if this is a code cell with Python code
                if cell.get("cell_type") == "code":
                    # Get the source content (might be string or list)
                    source = cell.get("source", "")
                    
                    # Convert list to string if needed
                    if isinstance(source, list):
                        source = "".join(source)
                    
                    # Skip non-Python code cells (e.g., magic commands only)
                    if source.strip().startswith("%") and "\n" not in source:
                        continue
                        
                    # Add a newline between cells for better parsing
                    python_code.append(source)
                    python_code.append("\n\n")
            
            # Combine all code into one string
            return "".join(python_code)
            
        except Exception as e:
            print(f"Error parsing notebook: {str(e)}")
            return ""
    
    def parse_code(self, source_code, language):
        """Parse code using tree-sitter"""
        # Special handling for Jupyter notebooks
        if language == "jupyter":
            python_code = self.extract_python_from_notebook(source_code)
            # Use the Python parser for the extracted code
            language = "python"
            source_code = python_code
            
            # If we couldn't extract any Python code, return None
            if not source_code:
                return None
        
        if not language or language not in self.parsers:
            return None
            
        parser = self.parsers[language]
        if not source_code:
            return None
            
        try:
            tree = parser.parse(bytes(source_code, "utf8"))
            return tree
        except Exception as e:
            print(f"Parsing error for {language}: {str(e)}")
            return None
    
    def analyze_diff(self, old_content, new_content, filename):
        """Analyze the difference between two versions of a file"""
        language = self.get_language_for_file(filename)
        
        # For unsupported languages
        if not language:
            return {
                "language": "unsupported",
                "changes": "File type not supported for structural analysis"
            }
        
        # For Jupyter notebooks, we'll use the Python parser but with special content extraction
        original_language = language
        if language == "jupyter":
            # We'll use the Python parser, but record that it's a Jupyter notebook
            language_for_output = "jupyter-python"
        else:
            language_for_output = language
            
        # Check if we have a parser for this language (after potential Jupyter conversion)
        parser_language = "python" if language == "jupyter" else language
        if parser_language not in self.parsers:
            return {
                "language": language_for_output,
                "changes": "Parser not available for this language"
            }
        
        # Parse both content versions
        old_tree = self.parse_code(old_content, language)
        new_tree = self.parse_code(new_content, language)
        
        # If either parse failed, return early
        if old_tree is None or new_tree is None:
            return {
                "language": language_for_output,
                "changes": "Unable to parse code structure"
            }
        
        # For Jupyter notebooks, we'll analyze as Python code
        language_for_analysis = "python" if language == "jupyter" else language
        
        # Extract functions and classes from both versions
        old_functions = self.extract_functions(old_tree, language_for_analysis)
        new_functions = self.extract_functions(new_tree, language_for_analysis)
        old_classes = self.extract_classes(old_tree, language_for_analysis)
        new_classes = self.extract_classes(new_tree, language_for_analysis)
        
        # Compare to find added, modified, and removed elements
        added_functions = []
        modified_functions = []
        removed_functions = []
        
        # Find added and modified functions
        old_function_names = {f["name"] for f in old_functions}
        for new_func in new_functions:
            if new_func["name"] not in old_function_names:
                added_functions.append(new_func["name"])
            else:
                # Check if implementation changed
                old_func = next((f for f in old_functions if f["name"] == new_func["name"]), None)
                if old_func and (old_func["start_line"] != new_func["start_line"] or 
                                old_func["end_line"] != new_func["end_line"]):
                    modified_functions.append(new_func["name"])
        
        # Find removed functions
        new_function_names = {f["name"] for f in new_functions}
        for old_func in old_functions:
            if old_func["name"] not in new_function_names:
                removed_functions.append(old_func["name"])
        
        # Similar analysis for classes
        added_classes = []
        modified_classes = []
        removed_classes = []
        
        old_class_names = {c["name"] for c in old_classes}
        for new_class in new_classes:
            if new_class["name"] not in old_class_names:
                added_classes.append(new_class["name"])
            else:
                # Check if implementation changed
                old_class = next((c for c in old_classes if c["name"] == new_class["name"]), None)
                if old_class and (old_class["start_line"] != new_class["start_line"] or 
                                old_class["end_line"] != new_class["end_line"]):
                    modified_classes.append(new_class["name"])
        
        new_class_names = {c["name"] for c in new_classes}
        for old_class in old_classes:
            if old_class["name"] not in new_class_names:
                removed_classes.append(old_class["name"])
        
        # Extract function calls in the new version
        function_calls = self.extract_function_calls(new_tree, language_for_analysis)
        
        # For Jupyter notebooks, add additional analysis info
        if original_language == "jupyter":
            notebook_specific = self._analyze_notebook_specific(new_content)
        else:
            notebook_specific = None
        
        result = {
            "language": language_for_output,
            "functions": {
                "added": added_functions,
                "modified": modified_functions,
                "removed": removed_functions,
                "total_count": len(new_functions)
            },
            "classes": {
                "added": added_classes,
                "modified": modified_classes,
                "removed": removed_classes,
                "total_count": len(new_classes)
            },
            "function_calls": [call["name"] for call in function_calls]
        }
        
        # Add notebook-specific info if available
        if notebook_specific:
            result["notebook_specific"] = notebook_specific
            
        return result
    
    def _analyze_notebook_specific(self, notebook_content: str) -> Dict[str, Any]:
        """Analyze notebook-specific features like cell types and markdown content"""
        try:
            # Parse the notebook content
            notebook = json.loads(notebook_content)
            
            # Count different types of cells
            code_cells = 0
            markdown_cells = 0
            raw_cells = 0
            
            # Check for imports and data operations
            has_imports = False
            data_libraries = ["pandas", "numpy", "matplotlib", "seaborn", "sklearn", 
                             "tensorflow", "torch", "keras", "scipy"]
            used_data_libraries = set()
            
            # Collect markdown section titles
            markdown_sections = []
            
            for cell in notebook.get("cells", []):
                cell_type = cell.get("cell_type", "")
                
                if cell_type == "code":
                    code_cells += 1
                    
                    # Check for imports and data libraries
                    source = cell.get("source", "")
                    if isinstance(source, list):
                        source = "".join(source)
                    
                    if "import " in source or "from " in source:
                        has_imports = True
                        
                        # Check for data science libraries
                        for lib in data_libraries:
                            if f"import {lib}" in source or f"from {lib}" in source:
                                used_data_libraries.add(lib)
                
                elif cell_type == "markdown":
                    markdown_cells += 1
                    
                    # Extract markdown headers
                    source = cell.get("source", "")
                    if isinstance(source, list):
                        source = "".join(source)
                    
                    # Find markdown headers (# Header)
                    for line in source.split("\n"):
                        if line.startswith("#"):
                            # Count the heading level
                            level = 0
                            for char in line:
                                if char == '#':
                                    level += 1
                                else:
                                    break
                            
                            title = line[level:].strip()
                            if title:  # Avoid empty headers
                                markdown_sections.append({
                                    "level": level,
                                    "title": title
                                })
                
                elif cell_type == "raw":
                    raw_cells += 1
            
            return {
                "cell_counts": {
                    "code": code_cells,
                    "markdown": markdown_cells,
                    "raw": raw_cells,
                    "total": code_cells + markdown_cells + raw_cells
                },
                "has_imports": has_imports,
                "data_libraries": list(used_data_libraries),
                "markdown_sections": markdown_sections[:10]  # Limit to first 10 sections
            }
            
        except Exception as e:
            print(f"Error analyzing notebook structure: {str(e)}")
            return {}
    
    def extract_functions(self, tree, language):
        """Extract function definitions from the AST"""
        if tree is None:
            return []
        
        functions = []
        query_map = {
            "python": "(function_definition name: (identifier) @name) @function",
            "javascript": [
                "(function_declaration name: (identifier) @name) @function",
                "(method_definition name: (property_identifier) @name) @function",
                "(arrow_function parameters: (formal_parameters) @params) @function"
            ],
            # other languages...
        }
        
        if language not in query_map:
            return []
        
        queries = query_map[language]
        if not isinstance(queries, list):
            queries = [queries]
        
        language_obj = self.supported_languages.get(language)
        if not language_obj:
            return []
            
        for query_string in queries:
            try:
                query = language_obj.query(query_string)
                captures = query.captures(tree.root_node)
                
                # Check if captures is a dictionary (newer API)
                if isinstance(captures, dict):
                    function_nodes = captures.get('function', [])
                    name_nodes = captures.get('name', [])
                    
                    # Create a mapping from function nodes to their names
                    function_to_name = {}
                    for name_node in name_nodes:
                        # Find the parent function node for this name
                        parent = name_node.parent
                        while parent and parent not in function_nodes:
                            parent = parent.parent
                        
                        if parent in function_nodes:
                            function_to_name[parent] = name_node.text.decode('utf8')
                    
                    # Process each function node
                    for function_node in function_nodes:
                        start_point, end_point = function_node.start_point, function_node.end_point
                        name = function_to_name.get(function_node, "anonymous")
                        
                        functions.append({
                            "name": name,
                            "start_line": start_point[0],
                            "end_line": end_point[0],
                            "node": function_node
                        })
                
                # For the original list of tuples API
                else:
                    # Track function nodes and their associated names
                    function_nodes = []
                    node_to_name = {}
                    
                    for node, tag in captures:
                        if tag == "function":
                            function_nodes.append(node)
                        elif tag == "name":
                            # Associate this name with its parent function
                            parent = node.parent
                            while parent:
                                if parent in function_nodes:
                                    node_to_name[parent] = node.text.decode('utf8')
                                    break
                                parent = parent.parent
                    
                    # Create function entries
                    for function_node in function_nodes:
                        start_point, end_point = function_node.start_point, function_node.end_point
                        name = node_to_name.get(function_node, "anonymous")
                        
                        functions.append({
                            "name": name,
                            "start_line": start_point[0],
                            "end_line": end_point[0],
                            "node": function_node
                        })
                        
            except Exception as e:
                print(f"Query error for {language}: {str(e)}")
                    
        return functions
    
    def _is_child(self, potential_child, parent):
        """Check if a node is a child of another node"""
        current = potential_child
        while current:
            if current == parent:
                return True
            current = current.parent
        return False
    
    def extract_classes(self, tree, language):
        """Extract class definitions from the AST"""
        if tree is None:
            return []
            
        classes = []
        query_map = {
            "python": "(class_definition name: (identifier) @name) @class",
            "javascript": "(class_declaration name: (identifier) @name) @class",
            # other languages...
        }
        
        if language not in query_map:
            return []
        
        language_obj = self.supported_languages.get(language)
        if not language_obj:
            return []
            
        try:
            query = language_obj.query(query_map[language])
            captures = query.captures(tree.root_node)
            
            # Check if captures is a dictionary (newer API)
            if isinstance(captures, dict):
                class_nodes = captures.get('class', [])
                name_nodes = captures.get('name', [])
                
                # Create a mapping from class nodes to their names
                class_to_name = {}
                for name_node in name_nodes:
                    # Find the parent class node for this name
                    parent = name_node.parent
                    while parent and parent not in class_nodes:
                        parent = parent.parent
                    
                    if parent in class_nodes:
                        class_to_name[parent] = name_node.text.decode('utf8')
                
                # Process each class node
                for class_node in class_nodes:
                    start_point, end_point = class_node.start_point, class_node.end_point
                    name = class_to_name.get(class_node, "anonymous")
                    
                    classes.append({
                        "name": name,
                        "start_line": start_point[0],
                        "end_line": end_point[0],
                        "node": class_node
                    })
            
            # For the original list of tuples API
            else:
                # Using the original approach for list of tuples
                for node, tag in captures:
                    if tag == "class":
                        # Find the class name node
                        name_nodes = [n for n, t in captures if t == "name" and self._is_child(n, node)]
                        name = name_nodes[0].text.decode('utf8') if name_nodes else "anonymous"
                        
                        start_point, end_point = node.start_point, node.end_point
                        classes.append({
                            "name": name,
                            "start_line": start_point[0],
                            "end_line": end_point[0],
                            "node": node
                        })
                        
        except Exception as e:
            print(f"Class extraction error for {language}: {str(e)}")
            
        return classes
    
    def extract_function_calls(self, tree, language):
        """Extract function calls from the AST"""
        if tree is None:
            return []
            
        calls = []
        query_map = {
            "python": "(call function: (identifier) @function)",
            "javascript": "(call_expression function: (identifier) @function)",
            # other languages...
        }
        
        if language not in query_map:
            return []
        
        language_obj = self.supported_languages.get(language)
        if not language_obj:
            return []
            
        try:
            query = language_obj.query(query_map[language])
            captures = query.captures(tree.root_node)
            
            # Check if captures is a dictionary (newer API)
            if isinstance(captures, dict):
                function_nodes = captures.get('function', [])
                
                # Process each function call node
                for node in function_nodes:
                    calls.append({
                        "name": node.text.decode('utf8'),
                        "line": node.start_point[0],
                    })
            
            # For the original list of tuples API
            else:
                for node, tag in captures:
                    if tag == "function":
                        calls.append({
                            "name": node.text.decode('utf8'),
                            "line": node.start_point[0],
                        })
                        
        except Exception as e:
            print(f"Call extraction error for {language}: {str(e)}")
                
        return calls
        """Extract function calls from the AST"""
        if tree is None:
            return []
            
        calls = []
        query_map = {
            "python": "(call function: (identifier) @function)",
            "javascript": "(call_expression function: (identifier) @function)",
            "java": "(method_invocation name: (identifier) @function)",
            "go": "(call_expression function: (identifier) @function)",
            "ruby": "(call method: (identifier) @function)",
            "rust": "(call_expression function: (identifier) @function)",
            "typescript": "(call_expression function: (identifier) @function)",
            "scala": "(apply function: (identifier) @function)"
        }
        
        if language not in query_map:
            return []
        
        language_obj = self.supported_languages.get(language)
        if not language_obj:
            return []
            
        try:
            query = language_obj.query(query_map[language])
            captures = query.captures(tree.root_node)
            
            for tag, node in captures.items():
                if tag == "function":
                    calls.append({
                        "name": node.text.decode('utf8'),
                        "line": node.start_point[0],
                    })
        except Exception as e:
            print(f"Call extraction error for {language}: {str(e)}")
                
        return calls
    
    def analyze_diff(self, old_content, new_content, filename):
        """Analyze the difference between two versions of a file"""
        language = self.get_language_for_file(filename)
        
        # For unsupported languages
        if not language:
            return {
                "language": "unsupported",
                "changes": "File type not supported for structural analysis"
            }
        
        # For Jupyter notebooks, we'll use the Python parser but with special content extraction
        original_language = language
        if language == "jupyter":
            # We'll use the Python parser, but record that it's a Jupyter notebook
            language_for_output = "jupyter-python"
        else:
            language_for_output = language
            
        # Check if we have a parser for this language (after potential Jupyter conversion)
        parser_language = "python" if language == "jupyter" else language
        if parser_language not in self.parsers:
            return {
                "language": language_for_output,
                "changes": "Parser not available for this language"
            }
        
        # Parse both content versions
        old_tree = None
        new_tree = None
        
        if old_content:
            old_tree = self.parse_code(old_content, language)
            
        if new_content:
            new_tree = self.parse_code(new_content, language)
        
        # Handle the case where both parses failed
        if old_tree is None and new_tree is None:
            return {
                "language": language_for_output,
                "changes": "Unable to parse code structure"
            }
        
        # For Jupyter notebooks, we'll analyze as Python code
        language_for_analysis = "python" if language == "jupyter" else language
        
        # Extract functions and classes from both versions
        old_functions = self.extract_functions(old_tree, language_for_analysis) if old_tree else []
        new_functions = self.extract_functions(new_tree, language_for_analysis) if new_tree else []
        old_classes = self.extract_classes(old_tree, language_for_analysis) if old_tree else []
        new_classes = self.extract_classes(new_tree, language_for_analysis) if new_tree else []
        
        # Compare to find added, modified, and removed elements
        added_functions = []
        modified_functions = []
        removed_functions = []
        
        # If we have a new tree but not an old one, all functions are added
        if old_tree is None and new_tree is not None:
            added_functions = [f["name"] for f in new_functions]
        # If we have an old tree but not a new one, all functions are removed
        elif old_tree is not None and new_tree is None:
            removed_functions = [f["name"] for f in old_functions]
        # If we have both trees, perform detailed comparison
        else:
            # Find added and modified functions
            old_function_names = {f["name"] for f in old_functions}
            for new_func in new_functions:
                if new_func["name"] not in old_function_names:
                    added_functions.append(new_func["name"])
                else:
                    # Check if implementation changed
                    old_func = next((f for f in old_functions if f["name"] == new_func["name"]), None)
                    if old_func and (old_func["start_line"] != new_func["start_line"] or 
                                    old_func["end_line"] != new_func["end_line"]):
                        modified_functions.append(new_func["name"])
            
            # Find removed functions
            new_function_names = {f["name"] for f in new_functions}
            for old_func in old_functions:
                if old_func["name"] not in new_function_names:
                    removed_functions.append(old_func["name"])
        
        # Similar analysis for classes
        added_classes = []
        modified_classes = []
        removed_classes = []
        
        # If we have a new tree but not an old one, all classes are added
        if old_tree is None and new_tree is not None:
            added_classes = [c["name"] for c in new_classes]
        # If we have an old tree but not a new one, all classes are removed
        elif old_tree is not None and new_tree is None:
            removed_classes = [c["name"] for c in old_classes]
        # If we have both trees, perform detailed comparison
        else:
            old_class_names = {c["name"] for c in old_classes}
            for new_class in new_classes:
                if new_class["name"] not in old_class_names:
                    added_classes.append(new_class["name"])
                else:
                    # Check if implementation changed
                    old_class = next((c for c in old_classes if c["name"] == new_class["name"]), None)
                    if old_class and (old_class["start_line"] != new_class["start_line"] or 
                                    old_class["end_line"] != new_class["end_line"]):
                        modified_classes.append(new_class["name"])
            
            new_class_names = {c["name"] for c in new_classes}
            for old_class in old_classes:
                if old_class["name"] not in new_class_names:
                    removed_classes.append(old_class["name"])
        
        # Extract function calls in the new version (if available)
        function_calls = []
        if new_tree is not None:
            function_calls = [call["name"] for call in self.extract_function_calls(new_tree, language_for_analysis)]
        
        # For Jupyter notebooks, add additional analysis info (if new content is available)
        if original_language == "jupyter" and new_content:
            notebook_specific = self._analyze_notebook_specific(new_content)
        else:
            notebook_specific = None
        
        # Determine file status based on tree availability
        if old_tree is None and new_tree is not None:
            file_status = "added"
        elif old_tree is not None and new_tree is None:
            file_status = "removed"
        else:
            file_status = "modified"
        
        result = {
            "language": language_for_output,
            "file_status": file_status,
            "functions": {
                "added": added_functions,
                "modified": modified_functions,
                "removed": removed_functions,
                "total_count": len(new_functions) if new_tree else 0
            },
            "classes": {
                "added": added_classes,
                "modified": modified_classes,
                "removed": removed_classes,
                "total_count": len(new_classes) if new_tree else 0
            },
            #"function_calls": function_calls
        }
        
        # Add notebook-specific info if available
        if notebook_specific:
            result["notebook_specific"] = notebook_specific
            
        return result
    
    def reconstruct_file_from_patch(self, patch, filename):
        """Attempt to reconstruct before/after file content from a patch"""
        if not patch:
            return None, None
            
        # Create empty files for before and after
        old_content = []
        new_content = []
        current_line_old = 0
        current_line_new = 0
        
        # Parse the unified diff
        lines = patch.split('\n')
        
        # Skip the first line (diff header)
        i = 0
        while i < len(lines) and not lines[i].startswith("@@"):
            i += 1
            
        while i < len(lines):
            line = lines[i]
            
            # Parse hunk header
            if line.startswith("@@"):
                match = re.match(r'@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@', line)
                if match:
                    old_start = int(match.group(1))
                    old_count = int(match.group(2) or 1)
                    new_start = int(match.group(3))
                    new_count = int(match.group(4) or 1)
                    
                    # Pad with empty lines if needed
                    while current_line_old < old_start - 1:
                        old_content.append("")
                        current_line_old += 1
                    while current_line_new < new_start - 1:
                        new_content.append("")
                        current_line_new += 1
                i += 1
                continue
                
            # Parse content lines
            if i < len(lines):
                if lines[i].startswith("+"):
                    # Added line (only in new file)
                    new_content.append(lines[i][1:])
                    current_line_new += 1
                elif lines[i].startswith("-"):
                    # Removed line (only in old file)
                    old_content.append(lines[i][1:])
                    current_line_old += 1
                elif lines[i].startswith(" "):
                    # Context line (in both files)
                    old_content.append(lines[i][1:])
                    new_content.append(lines[i][1:])
                    current_line_old += 1
                    current_line_new += 1
            i += 1
        
        # Join content lines
        return "\n".join(old_content), "\n".join(new_content)
    
    def analyze_file_changes(self, file_data):
        """Analyze changes in a single file"""
        filename = file_data.get("filename")
        patch = file_data.get("patch")
        status = file_data.get("status")
        
        # Skip binary files or files without patches
        if not patch and status != "removed":
            return {
                "filename": filename,
                "status": status,
                "changes": "Binary file or no patch available"
            }
        
        # For added files, we only have new content
        if status == "added":
            old_content = ""
            new_content = "\n".join([line[1:] for line in patch.split("\n") 
                                    if line.startswith("+")])
        
        # For removed files, we only have old content
        elif status == "removed":
            old_content = "\n".join([line[1:] for line in patch.split("\n") 
                                    if line.startswith("-")])
            new_content = ""
            
        # For modified files, reconstruct both versions
        else:
            old_content, new_content = self.reconstruct_file_from_patch(patch, filename)
        
        # Analyze the actual code changes
        analysis = self.analyze_diff(old_content, new_content, filename)
        analysis["filename"] = filename
        analysis["status"] = status
        
        return analysis