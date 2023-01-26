import requests

API_KEY = "3c0836b806ff47e77c284d14eb100c3d"


def get_data(place, forecast_days):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:8*forecast_days]

    return filtered_data
