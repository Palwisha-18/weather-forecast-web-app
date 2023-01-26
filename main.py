import plotly.express as ps
import streamlit as st

from backend import get_data

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [item['main']['temp'] for item in filtered_data]
        dates = [item['dt_txt'] for item in filtered_data]
        figure = ps.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
        st.plotly_chart(figure)

    elif option == "Sky":
        weather_conditions = [item['weather'][0]['main'] for item in filtered_data]
        dates = [item['dt_txt'] for item in filtered_data]
        images = {
            "Clear": "images/clear.png",
            "Clouds": "images/cloud.png",
            "Rain": "images/rain.png",
            "Snow": "images/snow.png"
        }
        image_paths = [images[condition] for condition in weather_conditions]
        st.image(image_paths, width=115)
