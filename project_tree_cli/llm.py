import os
import requests

def explain_project_structure(tree_str: str, api_key: str = None, provider_url: str = None) -> str:
    """
    Sends the tree string to an LLM provider (e.g., OpenAI) and returns the explanation.
    """
    api_key = api_key or os.getenv("OPENAI_API_KEY")
    provider_url = provider_url or "https://api.openai.com/v1/chat/completions"
    if not api_key:
        raise ValueError("No API key provided for LLM provider.")
    headers = {"Authorization": f"Bearer {api_key}", "Content-Type": "application/json"}
    data = {
        "model": "gpt-4.1-nano",
        "messages": [
            {"role": "system", "content": "You are a helpful assistant that explains project directory structures."},
            {"role": "user", "content": f"Explain the following project structure to a beginner developer.\n\n{tree_str}"}
        ]
    }
    response = requests.post(provider_url, headers=headers, json=data, timeout=30)
    response.raise_for_status()
    return response.json()["choices"][0]["message"]["content"]
