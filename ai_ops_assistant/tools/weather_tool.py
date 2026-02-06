import requests
import os
from dotenv import load_dotenv

load_dotenv()

def get_weather(city: str):
    api_key = os.getenv("OPENWEATHER_API_KEY")

    if not api_key:
        return {
            "success": True,
            "data": {
                "city": city,
                "temperature": "Unavailable",
                "humidity": "Unavailable",
                "description": "API key missing"
            }
        }

    url = "https://api.openweathermap.org/data/2.5/weather"

    params = {
        "q": city,
        "appid": api_key,
        "units": "metric"
    }

    try:
        response = requests.get(url, params=params, timeout=10)
        data = response.json()

        if response.status_code != 200:
            return {
                "success": True,
                "data": {
                    "city": city,
                    "temperature": "Unavailable",
                    "humidity": "Unavailable",
                    "description": "API error"
                }
            }

        return {
            "success": True,
            "data": {
                "city": city,
                "temperature": data["main"]["temp"],
                "humidity": data["main"]["humidity"],
                "description": data["weather"][0]["description"]
            }
        }

    except requests.RequestException:
        return {
            "success": True,
            "data": {
                "city": city,
                "temperature": "Unavailable",
                "humidity": "Unavailable",
                "description": "Request failed"
            }
        }
