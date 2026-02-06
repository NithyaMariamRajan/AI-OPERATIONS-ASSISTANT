import json
from llm.llm_client import call_llm

def generate_response(user_input: str, execution_results: dict):
    prompt = f"""
You are a professional AI Operations Assistant.

Generate a structured, clean, and readable response.

Strict Rules:
- Use plain text only (NO emojis).
- Do NOT use asterisks (*) anywhere.
- Use clear section headings.
- Use numbered points for repositories.
- Use bullet points for repository details.
- Keep weather in a separate section.
- Be concise and professional.
- Do NOT mention internal tools.
- Do NOT explain system logic.

User Request:
{user_input}

Execution Results:
{json.dumps(execution_results, indent=2)}

Format EXACTLY like this:

Top Repositories

1. Repository Name
   - Stars:
   - URL:
   - Description:

2. Repository Name
   - Stars:
   - URL:
   - Description:

Weather Update

- City:
- Temperature:
- Humidity:
- Condition:
"""

    return call_llm(prompt)
