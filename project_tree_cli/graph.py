import os
import ast

def generate_mermaid_chart(path: str) -> str:
    """
    Generate a Mermaid graph of local module import relationships.
    """
    base = path
    modules = {}
    # collect all python modules
    for root, _, files in os.walk(base):
        for file in files:
            if file.endswith(".py"):
                full = os.path.join(root, file)
                rel = os.path.relpath(full, base)
                mod_name = rel[:-3].replace(os.sep, ".")
                modules[mod_name] = full

    edges = set()
    # parse imports
    for mod_name, full in modules.items():
        try:
            with open(full, "r") as f:
                source = f.read()
            tree = ast.parse(source)
        except Exception:
            continue
        for node in ast.walk(tree):
            if isinstance(node, ast.Import):
                for alias in node.names:
                    imported = alias.name
                    if imported in modules:
                        edges.add((mod_name, imported))
            elif isinstance(node, ast.ImportFrom):
                module = node.module
                # resolve relative imports
                if node.level > 0:
                    parts = mod_name.split(".")
                    parent = parts[: len(parts) - node.level]
                    if module:
                        imported = ".".join(parent + [module])
                    else:
                        imported = ".".join(parent)
                else:
                    imported = module
                if imported in modules:
                    edges.add((mod_name, imported))

    # build mermaid chart
    lines = ["```mermaid", "graph TD"]
    for src, dst in sorted(edges):
        lines.append(f'    "{src}" --> "{dst}"')
    lines.append("```")
    return "\n".join(lines)
