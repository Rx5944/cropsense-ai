import os
import requests
import streamlit as st
from dotenv import load_dotenv

# Load local .env for local machine
load_dotenv()

# First try local env, then Streamlit secrets
API_KEY = os.getenv("OPENWEATHER_API_KEY")

if not API_KEY:
    API_KEY = st.secrets["OPENWEATHER_API_KEY"]


def get_weather(city):
    try:
        url = (
            "https://api.openweathermap.org/data/2.5/weather"
            f"?q={city}&appid={API_KEY}&units=metric"
        )

        response = requests.get(url, timeout=10)
        data = response.json()

        # Optional: API error handling
        if "main" not in data:
            return None

        return {
            "temp": data["main"]["temp"],
            "humidity": data["main"]["humidity"],
            "condition": data["weather"][0]["main"]
        }

    except Exception:
        return None


def weather_alerts(temp, humidity):
    alerts = []

    if temp > 35:
        alerts.append("High temperature may reduce crop yield.")

    if humidity > 85:
        alerts.append("High humidity may increase fungal disease risk.")

    if temp < 15:
        alerts.append("Cold stress may affect tropical crops.")

    return alerts


def irrigation_advice(temp, humidity):
    if temp > 34 and humidity < 60:
        return "High evaporation risk. Irrigation recommended."

    elif temp > 30:
        return "Moderate water need. Monitor soil moisture."

    else:
        return "No urgent irrigation need."