from tools.github_tool import search_repositories
from tools.weather_tool import get_weather
from utils.log import logger


def execute_plan(plan: dict):
    """
    Executor Agent:
    Executes each step from planner output.
    """

    logger.info("Execution started")

    if not isinstance(plan, dict) or "steps" not in plan:
        logger.error("Invalid plan structure")
        return {
            "execution_results": [],
            "error": "Invalid plan structure"
        }

    results = []

    for step in plan.get("steps", []):
        tool = step.get("tool")
        action = step.get("action")
        parameters = step.get("parameters", {})

        logger.info(f"Executing tool: {tool}.{action}")

        if tool == "github" and action == "search_repositories":
            output = search_repositories(
                query=parameters.get("query"),
                top_k=parameters.get("top_k", 3)
            )

            results.append({
                "tool": "github",
                "result": output
            })

        elif tool == "weather" and action == "get_weather":
            output = get_weather(
                city=parameters.get("city")
            )

            results.append({
                "tool": "weather",
                "result": output
            })

        else:
            logger.warning(f"Unknown tool/action: {tool}.{action}")
            results.append({
                "tool": tool,
                "error": "Unknown tool or action"
            })

    logger.info("Execution completed")

    return {
        "execution_results": results
    }