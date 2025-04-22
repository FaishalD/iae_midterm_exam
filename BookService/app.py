from flask import Flask, jsonify

app = Flask(__name__)

# Data Buku Dummy
books = {
    1: {"id": 1, "title": "Atomic Habits", "author": "James Clear", "price": 150000},
    2: {
        "id": 2,
        "title": "Rich Dad Poor Dad",
        "author": "Robert Kiyosaki",
        "price": 120000,
    },
}


@app.route("/books/<int:book_id>", methods=["GET"])
def get_book(book_id):
    book = books.get(book_id)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404


if __name__ == "__main__":
    app.run(port=5002)
