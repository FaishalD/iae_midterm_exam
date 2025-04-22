import requests
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Data Pesanan
orders = []

USER_SERVICE_URL = "http://localhost:5001/users"
BOOK_SERVICE_URL = "http://localhost:5002/books"


@app.route("/orders", methods=["POST"])
def create_order():
    data = request.get_json()
    user_id = data.get("user_id")
    book_id = data.get("book_id")

    # Get user and book data from other services
    user = requests.get(f"{USER_SERVICE_URL}/{user_id}").json()
    book = requests.get(f"{BOOK_SERVICE_URL}/{book_id}").json()

    if "error" in user or "error" in book:
        return jsonify({"error": "User or Book not found"}), 404

    order = {
        "order_id": len(orders) + 1,
        "user": user,
        "book": book,
        "total_price": book["price"],
    }
    orders.append(order)
    return jsonify(order), 200


@app.route("/orders/<int:user_id>", methods=["GET"])
def get_user_orders(user_id):
    user_orders = [order for order in orders if order["user"]["id"] == user_id]
    return jsonify(user_orders)


if __name__ == "__main__":
    app.run(port=5003)
