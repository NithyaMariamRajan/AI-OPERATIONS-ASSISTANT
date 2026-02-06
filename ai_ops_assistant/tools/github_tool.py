import requests
from utils.log import logger

# Simple in-memory cache
_CACHE = {}


def search_repositories(query: str, top_k: int = 3):
    """
    Search GitHub repositories sorted by stars.
    Returns top_k repositories for the given query.
    """

    cache_key = f"{query}_{top_k}"

    # -----------------------------
    # CACHE CHECK
    # -----------------------------
    if cache_key in _CACHE:
        logger.info("GitHub cache hit")
        return _CACHE[cache_key]

    logger.info("Calling GitHub API")

    url = "https://api.github.com/search/repositories"

    params = {
        "q": query,
        "sort": "stars",
        "order": "desc",
        "per_page": top_k
    }

    try:
        response = requests.get(url, params=params, timeout=10)

        if response.status_code == 403:
            return {
                "success": False,
                "error": "GitHub rate limit exceeded. Try again later."
            }

        response.raise_for_status()

    except requests.RequestException as e:
        logger.error("GitHub API failed")
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

    final_result = {
        "success": True,
        "data": results
    }

    # -----------------------------
    # SAVE TO CACHE
    # -----------------------------
    _CACHE[cache_key] = final_result

    logger.info("GitHub call successful")

    return final_result