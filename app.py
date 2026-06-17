from flask import Flask, request, jsonify
from flask_cors import CORS

from products import PRODUCTS
from recommender import (
    get_recommendations,
    search_products,
    get_budget_deals
)

app = Flask(__name__)
CORS(app)


@app.route("/")
def home():
    return "Backend is running 🚀"


@app.route("/api/products")
def get_products():
    category = request.args.get("category", "all")

    if category == "all":
        return jsonify(PRODUCTS)

    return jsonify([
        p for p in PRODUCTS
        if p["category"].lower() == category.lower()
    ])


@app.route("/api/search")
def search():
    query = request.args.get("q", "")
    return jsonify(search_products(query, PRODUCTS))


@app.route("/api/recommend", methods=["POST"])
def recommend():
    data = request.get_json()

    result = get_recommendations(
        data.get("budget", 10000),
        data.get("category", "all"),
        data.get("purpose", ""),
        PRODUCTS
    )

    return jsonify(result)


@app.route("/api/budget-deals")
def deals():
    limit = int(request.args.get("limit", 6))
    return jsonify(get_budget_deals(PRODUCTS, limit))


@app.route("/api/categories")
def categories():
    return jsonify(
        sorted(set(p["category"] for p in PRODUCTS))
    )


if __name__ == "__main__":
    print("Backend running at http://127.0.0.1:5000")

    app.run(
        debug=True,
        host="0.0.0.0",
        port=5000
    )