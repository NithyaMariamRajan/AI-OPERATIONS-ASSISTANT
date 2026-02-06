import requests
from ai_ops_assistant.utils.log import logger


def search_repositories(query: str, top_k: int = 3):
    """
    Search GitHub repositories sorted by stars.
    Returns top_k repositories for the given query.
    """

    logger.info(f"Searching GitHub for: {query}")

    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": top_k
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
    except requests.RequestException as e:
        logger.error(f"GitHub API failed: {str(e)}")
        return {
            "success": False,
            "error": f"GitHub API request failed: {str(e)}"
        }

    data = response.json()
    items = data.get("items", [])

    results = []

    for repo in items[:top_k]:
        results.append({
            "name": repo.get("name"),
            "full_name": repo.get("full_name"),
            "stars": repo.get("stargazers_count"),
            "url": repo.get("html_url"),
            "description": repo.get("description")
        })

    logger.info("GitHub search completed")

    return {
        "success": True,
        "data": results
    }
