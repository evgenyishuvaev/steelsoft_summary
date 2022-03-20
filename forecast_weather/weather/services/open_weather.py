
import requests
from datetime import datetime


from weather.services.config import load_config


CFG = load_config()


def get_weather(lat: float, lon: float, exclude="hourly,minutly") -> dict:

    payload = {"lat": lat, "lon": lon, "units": "metric","exclude": exclude, "appid": CFG.API_KEY}

    response = requests.get(CFG.API_URL, params=payload)
    resp_json = response.json()

    weather_dict = {
        "city_name": "",
        "temp": str(resp_json["current"]["temp"]),
        "feels_like": str(resp_json["current"]["feels_like"]),
        "datetime": datetime.fromtimestamp(resp_json["current"]["dt"])
    }

    return weather_dict