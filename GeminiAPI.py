from google import genai
from google.genai import types
import privconfig as p

def get_gemini_suggestions(budget_info):
    client = genai.Client(api_key=p.API_Key)

    price = str(budget_info["budget"])
    area = budget_info["category"]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are a financial advisor..."
        ),
        contents=f"What are three ways I can spend a budget of {price} on {area}, in a way that will stay within my means of living?"
    )

    return response.text