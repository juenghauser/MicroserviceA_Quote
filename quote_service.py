from flask import Flask, jsonify, request
import random
from quote_loader import load_quotes

app = Flask(__name__)

quotes = load_quotes()

@app.route("/")
def index():
    return "Quote Microservice is running!"

@app.route("/quote")
def get_random_quote():
    author = request.args.get("author")
    if author:
        filtered = [q for q in quotes if q["author"].lower() == author.lower()]
        if not filtered:
            return jsonify({
                "success": False,
                "message": f"No quotes found for author: {author}"
            }), 404
        return jsonify(random.choice(filtered))
    else:
        return jsonify(random.choice(quotes))

@app.route("/quotes")
def get_all_quotes():
    return jsonify(quotes)

if __name__ == "__main__":
    app.run(port=7005)
