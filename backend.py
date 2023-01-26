import os
from os.path import join, dirname

import requests
from dotenv import load_dotenv

dotenv_path = join(dirname(__file__), '.env')
load_dotenv(dotenv_path)

SECRET_KEY = os.environ.get("SECRET_KEY")


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={SECRET_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:8 * forecast_days]

    return filtered_data
