from flask import Flask, request, jsonify
from flask_cors import CORS
import GeminiAPI

# makes it so that we can get input from the front end and not just the terminal. 
app = Flask(__name__)
CORS(app)  

@app.route('/getSuggestions', methods=['POST'])
def get_suggestions():
    data = request.get_json()
    budget = data.get('budget')
    category = data.get('category')

    try:
        budget = float(budget)
        if budget <= 0:
            raise ValueError
    except:
        return jsonify({"error": "Invalid budget format"}), 400

    try:
        suggestions = GeminiAPI.get_response(budget, category)
        return jsonify({"suggestions": suggestions})
    except Exception as e:
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    app.run(debug=True)
