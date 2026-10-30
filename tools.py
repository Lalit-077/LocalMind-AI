from datetime import datetime
from ddgs import DDGS
import geocoder
import requests


def get_user_city():
    result = geocoder.ip("me")
    return result

def get_current_time():
    return datetime.now().strftime("%Y-%m-%d %H:%M:%S")

def get_city_weather(city):
    url = f"https://wttr.in/{city}?format=3"
    response = requests.get(url, timeout=10)
    return response.text

def get_news(topic):
    results = DDGS().news(topic, max_results=6)
    my_list=[]
    for r in results:
        my_list.append(f"{r['title']} ({r['source']})\n{r['url']}")
    return "\n".join(my_list)

TOOLS = [
    {
        "type": "function",
        "function": {
            "name": "get_current_time",
            "description": "Returns the current date and time in YYYY-MM-DD HH:MM:SS format.",
            "parameters": {
                "type": "object",
                "properties": {},
                "required": [],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_city_weather",
            "description": "Returns the live weather of a city.",
            "parameters": {
                "type": "object",
                "properties": {
                    "city": {
                        "type": "string",
                        "description": "City to get the weather for.",
                    }
                },
                "required": ["city"],
            },
        },
    },
    {
        "type": "function",
        "function": {
            "name": "get_news",
            "description": "Searches the web for current news about a given topic.",
            "parameters": {
                "type": "object",
                "properties": {
                    "topic": {
                        "type": "string",
                        "description": "Topic to search for current news about.",
                    }
                },
                "required": ["topic"],
            },
        },
    },
     {
            "type": "function",
            "function": {
                "name": "get_user_city",
                "description": "Search the city of user .",
                "parameters": {
                    "type": "object",
                    "properties": {}
                    
            },
    },
 },
]


FUNCTION_NAME_TO_FUNCTION_MAP = {
    "get_current_time" : get_current_time,
    "get_city_weather" : get_city_weather,
    "get_news": get_news,
    "get_user_city": get_user_city
}