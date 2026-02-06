def generate_response(user_input: str, execution_results: dict):
    results = execution_results.get("execution_results", [])

    github_data = []
    weather_data = {}

    for item in results:
        if item["tool"] == "github" and item["result"]["success"]:
            github_data = item["result"]["data"]
        elif item["tool"] == "weather" and item["result"]["success"]:
            weather_data = item["result"]["data"]

    response = []

    response.append("Top Repositories\n")

    for idx, repo in enumerate(github_data, start=1):
        response.append(f"{idx}. {repo['name']}")
        response.append(f"   Stars: {repo['stars']}")
        response.append(f"   URL: {repo['url']}")
        response.append(f"   Summary: {repo['description']}\n")

    if weather_data:
        response.append("Weather Update\n")
        response.append(f"City: {weather_data['city']}")
        response.append(f"Temperature: {weather_data['temperature']}°C")
        response.append(f"Humidity: {weather_data['humidity']}%")
        response.append(f"Condition: {weather_data['description']}")

    return "\n".join(response)
