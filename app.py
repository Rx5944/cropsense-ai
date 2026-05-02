import streamlit as st
import pandas as pd
import pickle

from utils.profitability import get_profitability
from utils.weather import get_weather
from utils.fertilizer import recommend_fertilizer
from utils.alerts import risk_alerts
from utils.llm_assistant import ask_ai

# -------------------------------------------------
# PAGE CONFIG
# -------------------------------------------------
st.set_page_config(
    page_title="CropSense AI Pro",
    page_icon="🌱",
    layout="wide"
)

# -------------------------------------------------
# SESSION STATE
# -------------------------------------------------
if "weather" not in st.session_state:
    st.session_state.weather = None

# -------------------------------------------------
# LOAD MODEL
# -------------------------------------------------
with open("model/crop_model.pkl", "rb") as f:
    model = pickle.load(f)

with open("model/label_encoder.pkl", "rb") as f:
    encoder = pickle.load(f)

# -------------------------------------------------
# HEADER
# -------------------------------------------------
st.title("🌱 CropSense AI Pro")
st.caption("AI-Powered Precision Agriculture Decision Support Platform")

# -------------------------------------------------
# SIDEBAR
# -------------------------------------------------
st.sidebar.header("🌾 Farm Inputs")

city = st.sidebar.selectbox(
    "Region",
    ["Chennai", "Coimbatore", "Madurai", "Punjab", "Bangalore"]
)

# Default values
temp = 25.0
humidity = 70.0

# -------------------------------------------------
# WEATHER FETCH
# -------------------------------------------------
if st.sidebar.button("🌦 Fetch Live Weather"):
    st.session_state.weather = get_weather(city)

weather = st.session_state.weather

if weather:
    temp = float(weather["temp"])
    humidity = float(weather["humidity"])

    st.sidebar.success("Live Weather Loaded")
    st.sidebar.metric("Temperature", f"{temp} °C")
    st.sidebar.metric("Humidity", f"{humidity} %")

    if "condition" in weather:
        st.sidebar.write(f"Condition: {weather['condition']}")

# -------------------------------------------------
# INPUT FIELDS
# -------------------------------------------------
N = st.sidebar.number_input("Nitrogen", 0, 150, 90)
P = st.sidebar.number_input("Phosphorus", 0, 150, 40)
K = st.sidebar.number_input("Potassium", 0, 150, 40)

temp = st.sidebar.number_input(
    "Temperature (°C)",
    0.0, 50.0, float(temp)
)

humidity = st.sidebar.number_input(
    "Humidity (%)",
    0.0, 100.0, float(humidity)
)

ph = st.sidebar.number_input(
    "pH",
    0.0, 14.0, 6.5
)

rainfall = st.sidebar.number_input(
    "Rainfall (mm)",
    0.0, 500.0, 120.0
)

# -------------------------------------------------
# PREDICT BUTTON
# -------------------------------------------------
if st.button("🚀 Predict Crop"):

    if ph < 3 or ph > 10:
        st.warning("Entered pH is uncommon. Please verify.")

    with st.spinner("Analyzing farm conditions..."):

        input_data = [[
            N, P, K,
            temp,
            humidity,
            ph,
            rainfall
        ]]

        probs = model.predict_proba(input_data)[0]
        classes = encoder.inverse_transform(
            range(len(probs))
        )

        result = pd.DataFrame({
            "crop": classes,
            "probability": probs
        })

        result = result.sort_values(
            by="probability",
            ascending=False
        ).head(5)

        final = get_profitability(result)

        best_crop = result.iloc[0]["crop"]
        best_profit = final.iloc[0]["crop"]
        confidence = round(
            result.iloc[0]["probability"] * 100,
            2
        )

    # ---------------------------------------------
    # KPI CARDS
    # ---------------------------------------------
    c1, c2, c3 = st.columns(3)

    c1.metric("🌾 Best Crop", best_crop)
    c2.metric("📈 Confidence", f"{confidence}%")
    c3.metric("💰 Most Profitable", best_profit)

    if confidence < 60:
        st.warning(
            "Prediction confidence is low. "
            "Try refining inputs."
        )

    # ---------------------------------------------
    # CHARTS
    # ---------------------------------------------
    st.subheader("📊 Top Suitable Crops")
    st.bar_chart(
        result.set_index("crop")["probability"]
    )

    st.subheader("💰 Profitability Ranking")
    st.bar_chart(
        final.set_index("crop")["profit_score"]
    )

    # ---------------------------------------------
    # DOWNLOAD REPORT
    # ---------------------------------------------
    csv = final.to_csv(index=False).encode("utf-8")

    st.download_button(
        "📥 Download Report",
        csv,
        "crop_report.csv",
        "text/csv"
    )

    # ---------------------------------------------
    # FERTILIZER
    # ---------------------------------------------
    st.subheader("🧪 Fertilizer Advice")

    for item in recommend_fertilizer(
        N, P, K, ph
    ):
        st.info(item)

    # ---------------------------------------------
    # ALERTS
    # ---------------------------------------------
    st.subheader("⚠ Risk Alerts")

    alerts = risk_alerts(
        temp,
        humidity,
        rainfall,
        ph
    )

    if alerts:
        for a in alerts:
            st.warning(a)
    else:
        st.success(
            "No major risks detected."
        )

    # ---------------------------------------------
    # SMART RECOMMENDATION
    # ---------------------------------------------
    st.subheader("🤖 AI Recommendation")

    st.success(
        f"{best_profit} is recommended for "
        f"{city} because soil conditions are "
        f"suitable and current weather "
        f"({temp}°C, {humidity}%) supports "
        f"healthy growth."
    )

# -------------------------------------------------
# AI ASSISTANT
# -------------------------------------------------
st.divider()

st.subheader("🤖 Ask CropSense AI Expert")

question = st.text_input(
    "Ask about crops, fertilizers, irrigation..."
)

if st.button("Ask AI"):
    if question.strip():

        with st.spinner("Thinking..."):
            answer = ask_ai(question)

        st.success(answer)

# -------------------------------------------------
# FOOTER
# -------------------------------------------------
st.caption(
    "Built with AI for Precision Agriculture 🌱"
)