from flask import Flask, jsonify

app = Flask(__name__)

# Data User Dummy
users = {
    1: {"id": 1, "name": "Faishal D", "email": "fai@example.com"},
    2: {"id": 2, "name": "Wafiq J", "email": "waf@example.com"},
    3: {"id": 3, "name": "Yasmin A", "email": "yas@example.com"},
    4: {"id": 4, "name": "Arya D", "email": "ary@example.com"},
    5: {"id": 5, "name": "Benito", "email": "ben@example.com"},
}


@app.route("/users/<int:user_id>", methods=["GET"])
def get_user(user_id):
    user = users.get(user_id)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


if __name__ == "__main__":
    app.run(port=5001)
