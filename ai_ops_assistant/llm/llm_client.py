import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "phi3"


def call_llm(prompt: str) -> str:
    payload = {
        "model": MODEL_NAME,
        "prompt": prompt,
        "stream": False
    }

    try:
        response = requests.post(OLLAMA_URL, json=payload)

        if response.status_code != 200:
            return f"Ollama Error {response.status_code}: {response.text}"

        data = response.json()
        return data.get("response", "")

    except Exception as e:
        return f"LLM Exception: {str(e)}"