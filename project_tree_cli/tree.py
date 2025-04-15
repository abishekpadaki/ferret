import os

def list_directory_tree(path: str, prefix: str = "") -> str:
    """
    Recursively lists files and folders in a directory as a tree structure.
    Returns a string representation of the tree.
    """
    entries = sorted(os.listdir(path))
    tree_str = ""
    for idx, entry in enumerate(entries):
        full_path = os.path.join(path, entry)
        connector = "└── " if idx == len(entries) - 1 else "├── "
        tree_str += f"{prefix}{connector}{entry}\n"
        if os.path.isdir(full_path):
            extension = "    " if idx == len(entries) - 1 else "│   "
            tree_str += list_directory_tree(full_path, prefix + extension)
    return tree_str
