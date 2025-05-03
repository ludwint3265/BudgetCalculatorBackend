from google import genai
from google.genai import types
import os
from dotenv import load_dotenv

load_dotenv()

def get_gemini_suggestions(budget_info):
    client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

    price = str(budget_info["budget"])
    area = budget_info["category"]

    response = client.models.generate_content(
        model="gemini-2.0-flash",
        config=types.GenerateContentConfig(
            system_instruction="You are an expert travel, lifestyle assistant and financial advisor. Given a user's budget and selected category (e.g., travel, food experiences, fitness, education), generate 3 realistic, achievable options they can do. Each option must be 1 to 2 sentences, concise, and have an example with a real places, foods, activities, or services that the user could actually look up online. Make the suggestions feel exciting, personal, and within the given budget. Return only the list — no intro, no explanations, no numbering. Format the output as a list of strings separated by '`'. Example of a suggestion: '3 - 4 Day City Escape: Explore Lisbon, Portugal or Mexico City. Enjoy affordable flights, boutique hotels, and authentic local food — all within budget.'"
        ),
        contents=f"What are three ways I can spend a budget of {price} on {area}, in a way that will stay within my means of living?"

    )

    return response.text