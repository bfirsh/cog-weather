import requests
from typing import Any
from cog import Input

def weather(location: str = Input(description="Name of a city")) -> Any:
    url = f"http://wttr.in/{location}?format=j1"
    response = requests.get(url)
    response.raise_for_status()
    return response.json()["current_condition"]
