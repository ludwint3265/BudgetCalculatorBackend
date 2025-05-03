from google import genai
from google.genai import types
from dotenv import load_dotenv
import os

# loading the key from the .env file instead of the privconfig.py
load_dotenv()

def get_response(budget, category):
    api_key = os.getenv("GEMINI_API_KEY")
    
    if not api_key:
        raise ValueError("GEMINI_API_KEY not found in environment variables.")

    client = genai.Client(api_key=api_key)

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You're a helpful financial advisor. Suggest 3 concise, practical ways to spend a given budget in a chosen category."
        ),
        contents=f"What are three ways I can spend ${budget} on {category} while staying within my means?"
    )

    return response.text





