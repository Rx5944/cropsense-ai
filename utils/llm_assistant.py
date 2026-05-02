import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

API_KEY = os.getenv("GROQ_API_KEY")
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
Keep answers concise and useful.
"""
                },
                {
                    "role": "user",
                    "content": question
                }
            ]
        )

        return response.choices[0].message.content

    except Exception as e:
        return str(e)