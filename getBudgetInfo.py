

def validate_user_input(budget_str, category_str, location_str):
    try:
        budget = float(budget_str)
        if budget < 0:
            return None, "Budget must be greater than or equal to 0"
    except ValueError:
        return None, "Invalid budget format"

    if not category_str.strip():
        return None, "Invalid category"

    if not location_str.strip():
        return None, "Invalid location"

    return {"budget": budget, "category": category_str, "location": location_str}, None
