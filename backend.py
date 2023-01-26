import requests

API_KEY = "3c0836b806ff47e77c284d14eb100c3d"


def get_data(place, forecast_days, kind):
    url = f"http://api.openweathermap.org/data/2.5/forecast?q={place}&appid={API_KEY}"
    response = requests.get(url)
    data = response.json()
    filtered_data = data['list'][:8*forecast_days]
    if kind == "Temperature":
        filtered_data = [item['main']['temp'] for item in filtered_data]
    elif kind == "Sky":
        filtered_data = [item['weather'][0]['main'] for item in filtered_data]
    return filtered_data
