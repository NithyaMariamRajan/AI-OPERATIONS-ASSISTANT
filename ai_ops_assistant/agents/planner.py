import json
from ai_ops_assistant.llm.llm_client import call_llm
from ai_ops_assistant.utils.log import logger


def create_plan(user_input: str):
    logger.info("Planning started")

    prompt = f"""
You are a strict JSON planning agent.

You MUST return ONLY valid JSON.
Do NOT explain.
Do NOT write paragraphs.
Do NOT write markdown.
Do NOT add extra text.
ONLY return JSON.

Available tools:
1. github.search_repositories(query, top_k)
2. weather.get_weather(city)

Return format EXACTLY like this:

{{
  "steps": [
    {{
      "tool": "github",
      "action": "search_repositories",
      "parameters": {{
        "query": "AI repositories",
        "top_k": 2
      }}
    }},
    {{
      "tool": "weather",
      "action": "get_weather",
      "parameters": {{
        "city": "Bangalore"
      }}
    }}
  ]
}}

User request:
{user_input}
"""

    response = call_llm(prompt)
    cleaned = response.strip()

    # Remove markdown if model still adds it
    if cleaned.startswith("```"):
        cleaned = cleaned.replace("```json", "")
        cleaned = cleaned.replace("```", "").strip()

    try:
        plan = json.loads(cleaned)
        logger.info("Planning successful")
        return plan
    except Exception:
        logger.error("Invalid JSON from planner")
        return {"error": "Invalid JSON from planner", "raw_response": response}
