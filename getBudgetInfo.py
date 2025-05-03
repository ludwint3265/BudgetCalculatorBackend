

def validate_budget_and_category(budget_str, category_str):
    try:
        budget = float(budget_str)
        if budget <= 0:
            return None, "Budget must be greater than 0"
    except ValueError:
        return None, "Invalid budget format"

    catDict = {
        "Travel": 1,
        "Food": 2,
        "Education / Courses": 3,
        "Housing / Rent Rate": 4,
        "Save & Grow It": 5,
        "Fitness and Wellness": 6,
        "Social Impact & Charity": 7,
        "Entertainment": 8,
        "Emergency Fund": 9,
        "Subscriptions and Memberships": 10
    }

    if category_str not in catDict:
        return None, "Invalid category"

    return {"budget": budget, "category": category_str}, None