# Ferret

A simple Python CLI tool to display and explain project directory structures.

## Installation

```sh
pip install .
```

## Usage

List the contents of a directory as a tree:

```sh
project-tree list /path/to/project
```

Explain the project structure (requires OpenAI API key):

```sh
export OPENAI_API_KEY=your-openai-key
project-tree explain /path/to/project
```

## Features
- List files and folders as a tree
- Explain the directory structure using an LLM (OpenAI)

---

Created by Abiks (Abishek Padaki)
