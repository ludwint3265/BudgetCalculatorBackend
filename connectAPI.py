from flask import Flask, request, jsonify
from userInputRunner import run_pipeline

app = Flask(__name__)

@app.route("/get-suggestions", methods=["POST"])
def get_suggestions():
    data = request.json
    budget = data.get("budget")
    category = data.get("category")

    result = run_pipeline(budget, category)
    return jsonify(result)

if __name__ == "__main__":
    app.run(debug=True)