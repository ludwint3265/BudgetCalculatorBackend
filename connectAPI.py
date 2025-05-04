from flask import Flask, request, jsonify
from flask_cors import CORS
from userInputRunner import run_pipeline

app = Flask(__name__)
CORS(app)

@app.route("/")
def home():
    return "WE LIVE BABY"

@app.route("/get-suggestions", methods=["POST"])
def get_suggestions():
    data = request.json
    budget = data.get("budget")
    category = data.get("category")

    try:
        result = run_pipeline(budget, category)
        return jsonify(result)
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
