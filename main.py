import streamlit as st
import plotly.express as ps

st.title("Weather Forecast for the Next Days")

place = st.text_input("Place: ")
days = st.slider("Forecast Days", min_value=1, max_value=5, help="Select the number of forecasted days")
option = st.selectbox("Select data to view", ("Temperature", "Sky"))
st.subheader(f"{option} for the next {days} days in {place}")


def get_data(days):
    dates = ["2022-25-10", "2022-26-10", "2022-27-10"]
    temperatures = [10, 11, 15]
    temperatures = [days * i for i in temperatures]
    return dates, temperatures


dates, temperatures = get_data(days)
figure = ps.line(x=dates, y=temperatures, labels={'x': 'Date', 'y': 'Temperature (C)'})
st.plotly_chart(figure)
