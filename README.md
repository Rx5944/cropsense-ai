# 🌱 CropSense AI Pro

AI-powered Precision Agriculture Decision Support Platform built with Python and Streamlit.

CropSense AI Pro helps farmers, agribusiness users, researchers, and students make smarter crop decisions using:

* Soil nutrient data (N, P, K)
* Temperature
* Humidity
* pH level
* Rainfall
* Weather API integration
* Profitability ranking
* Fertilizer recommendations
* Risk alerts
* AI farming assistant



# Live Project Purpose

This project predicts the most suitable crop for a given region using machine learning and enhances the recommendation with real-world intelligence such as weather and profitability.


# ✨ Features

## 🌾 Crop Prediction Engine

Uses a trained machine learning model to predict the best crop based on environmental and soil inputs.(Random Forest Classifier)

## 💰 Profitability Ranking

Ranks suitable crops using market profitability logic.

## 🌦 Live Weather Integration

Fetches real-time weather data for selected regions.(OpenWeather)

* Temperature
* Humidity
* Weather condition

## 🧪 Fertilizer Recommendation Engine

Provides fertilizer suggestions based on soil nutrient deficiencies.(Rule Based)

Examples:

* Low Nitrogen → Urea
* Low Phosphorus → DAP
* Low Potassium → MOP

## ⚠ Risk Alert System
(Rule Based)
Warns users about possible risks:

* Low rainfall
* Heat stress
* High humidity disease risk
* pH imbalance

## 🤖 AI Farming Assistant
(Groq ai)
Integrated LLM assistant for farming questions such as:

* Which crop should I grow this season?
* Best fertilizer for low nitrogen soil?
* Pest prevention tips
* Irrigation guidance

## 📊 Interactive Dashboard

Visual analytics using Streamlit charts and metrics.


# 🧠 Tech Stack

## Frontend / UI

* Python
* Streamlit

## Backend / Logic

* Python

## Machine Learning

* Scikit-learn
* Pandas
* NumPy

## APIs

* OpenWeather API
* Groq LLM API

---

# 📁 Project Structure

cropsense-ai/
│── app.py
│── requirements.txt
│── README.md
│
├── model/
│   ├── train.py
│   ├── crop_model.pkl
│   └── label_encoder.pkl
│
├── data/
│   ├── crop_data.csv
│   └── prices.csv
│
├── utils/
│   ├── profitability.py
│   ├── weather.py
│   ├── fertilizer.py
│   ├── alerts.py
│   └── llm_assistant.py
│


# ⚙ Installation

## 1. Clone Repository

```bash
git clone YOUR_REPOSITORY_URL
cd cropsense-ai
```

## 2. Create Virtual Environment

```bash
python -m venv venv
source venv/bin/activate
```

## 3. Install Requirements

```bash
pip install -r requirements.txt
```

---

# 🔐 Environment Variables

Create a `.env` file in root folder.

```env
OPENWEATHER_API_KEY=your_openweather_key
GROQ_API_KEY=your_groq_key
```

---

# ▶ Run Project

```bash
streamlit run app.py
```

Then open browser:

```text
http://localhost:8501
```

---

# 📌 Input Parameters

Users can enter:

| Parameter   | Description             |
| ----------- | ----------------------- |
| Nitrogen    | Soil nitrogen level     |
| Phosphorus  | Soil phosphorus level   |
| Potassium   | Soil potassium level    |
| Temperature | Ambient temperature     |
| Humidity    | Relative humidity       |
| pH          | Soil acidity/alkalinity |
| Rainfall    | Rainfall in mm          |

---

# 📈 Output

The system provides:

* Best predicted crop
* Confidence score
* Top 5 suitable crops
* Profitability ranking
* Fertilizer advice
* Risk alerts
* AI recommendation

---

# 🤖 Example Use Cases

## Farmer

Find profitable crops for current conditions.

## Agriculture Student

Learn crop-soil relationships.

## Agritech Startup

Use as prototype decision engine.

## Research Demo

Showcase ML + API integration.

---

# 🧪 Model Information

The crop recommendation model is trained using supervised machine learning on agricultural datasets containing:

* Soil nutrients
* Weather factors
* Crop labels

Typical algorithms used:

* Random Forest
* Decision Tree
* Gradient Boosting

(Current implementation depends on training file.)

---

# 🔮 Future Improvements

* Satellite imagery integration
* District-wise crop prediction
* Tamil / regional language support
* Yield estimation
* Pest disease image detection
* 5-day weather forecast planning
* Mobile app version
* Market price live API integration

---

# 🌍 Deployment

Recommended platforms:

* Streamlit Community Cloud
* Render
* Railway

---

# 👨‍💻 Author

Developed as an AI + Agriculture innovation project for smart farming solutions.

---

# 📜 License

This project is open for educational and portfolio use.

---

# ⭐ Final Note

CropSense AI Pro combines Machine Learning, Weather Intelligence, Business Logic, and AI Assistance into one modern agriculture platform.

Built to support smarter farming decisions. 🌱
