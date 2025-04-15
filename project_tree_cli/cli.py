import click
import os
from .tree import list_directory_tree
from .llm import explain_project_structure

@click.group()
def cli():
    """A CLI tool to display and explain project directory structures."""
    pass

@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
def list(path):
    """List the contents of a directory as a tree."""
    tree_str = list_directory_tree(path)
    click.echo(tree_str)

@cli.command()
@click.argument('path', type=click.Path(exists=True, file_okay=False))
def explain(path):
    """Explain the project structure using an LLM (OpenAI API key required)."""
    tree_str = list_directory_tree(path)
    click.echo("Project Tree:\n" + tree_str)
    click.echo("\nRequesting explanation from LLM...\n")
    try:
        explanation = explain_project_structure(tree_str)
        click.echo(explanation)
    except Exception as e:
        click.echo(f"Error: {e}")

if __name__ == "__main__":
    cli()
