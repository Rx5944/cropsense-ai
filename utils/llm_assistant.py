import os
import streamlit as st
from dotenv import load_dotenv
from groq import Groq

# Load local .env
load_dotenv()

# First try local env, then Streamlit secrets
API_KEY = os.getenv("GROQ_API_KEY")

if not API_KEY:
    API_KEY = st.secrets["GROQ_API_KEY"]


def ask_ai(question):
    try:
        client = Groq(api_key=API_KEY)

        response = client.chat.completions.create(
            model="openai/gpt-oss-120b",
            messages=[
                {
                    "role": "system",
                    "content": """
You are an expert agriculture advisor for Indian farmers.
Give practical advice on crops, fertilizers, irrigation, pests.
Keep answers concise, practical, and useful.
Prefer advice suitable for Indian climate and farming conditions.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ],
            temperature=0.4,
            max_tokens=500
        )

        return response.choices[0].message.content

    except Exception as e:
        return f"AI service error: {str(e)}"