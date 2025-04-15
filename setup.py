from setuptools import setup, find_packages

setup(
    name="project-tree-cli",
    version="0.1.0",
    description="A simple CLI to display and explain project directory structures.",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "click",
        "requests"
    ],
    entry_points={
        "console_scripts": [
            "project-tree=project_tree_cli.cli:cli"
        ]
    },
    python_requires=">=3.7",
)
