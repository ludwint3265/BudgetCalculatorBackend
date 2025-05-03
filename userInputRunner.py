import json
from getBudgetInfo import validate_budget_and_category
from GeminiAPI import get_gemini_suggestions

def run_pipeline(budget_str, category_str):
    data, error = validate_budget_and_category(budget_str, category_str)
    if error:
        return {"error": error}

    suggestions = get_gemini_suggestions(data)
    result = {
        "input": data,
        "suggestions": suggestions
    }

    with open("output.json", "w") as f:
        json.dump(result, f)

    return result

if __name__ == "__main__":
    # Dev testing only. Not used in real frontend.
    budget_input = input("Enter budget: ")
    category_input = input("Enter category: ")
    print(run_pipeline(budget_input, category_input))