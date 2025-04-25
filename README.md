# Ferret

<img src="assets/ferret.png" width="300" height="400">

A simple Python CLI tool to display and explain project directory structures.

## Installation

```sh
pip install .
```

## Usage

List the contents of a directory as a tree:

```sh
ferret list /path/to/project
```

Explain the project structure (requires OpenAI API key):

```sh
export OPENAI_API_KEY=your-openai-key
ferret explain /path/to/project
```

Generate a Mermaid import graph for a codebase:

```sh
ferret graph /path/to/project
```

## Features
- List files and folders as a tree
- Explain the directory structure using an LLM (OpenAI)
- Generate module import dependency graph as a Mermaid chart

---

Created by Abiks (Abishek Padaki)

[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
