# iae_midterm_exam

Membangun Sistem Terintegrasi Antar Layanan
Studi Kasus: Pemesanan Buku Online

# Link Demo Youtube

https://youtu.be/rMyzh7c4WHg

# Terdiri dari 3 layanan utama:

- UserService (Port 5001)
- BookService (Port 5002)
- OrderService (Port 5003)

# UserService (Port 5001)

Menyediakan data user.

_Endpoint_
GET /users/{user_id}
Mengambil data user berdasarkan ID.

Contoh Response (200 OK):
{
"id": 1,
"name": "Faishal D",
"email": "fai@example.com"
}

Contoh Response (404 Not Found):
{
"error": "User not found"
}

# BookService (Port 5002)

Menyediakan data buku.

_Endpoint_
GET /books
Mengambil semua data buku.

Contoh Response:
[
{
"id": 1,
"title": "Atomic Habits",
"author": "James Clear",
"price": 150000
},
{
"id": 2,
"title": "Rich Dad Poor Dad",
"author": "Robert Kiyosaki",
"price": 120000
}
{
"id": 3,
"title": "Laskar Pelangi",
"author": "Andrea Hirata",
"price": 150000,
},
{
"id": 4,
"title": "Doraemon Vol.03",
"author": "Fujiko F. Fujio",
"price": 50000,
}
{
"id": 5,
"title": "Makanya Mikir!",
"author": "Cania and Abigail",
"price": 160000,
},
]

GET /books/{book_id}
Mengambil detail buku berdasarkan ID.

Contoh Response (200 OK):
{
"id": 1,
"title": "Atomic Habits",
"author": "James Clear",
"price": 150000
}

Contoh Response (404 Not Found):
{
"error": "Book not found"
}

# OrderService (Port 5003)

Mengelola pemesanan buku dari user.

_Endpoint_
POST /orders
Membuat pesanan baru.

Request Body:
{
"user_id": 1,
"book_id": 2
}

Contoh Response (201 Created):
{
"order_id": 1,
"user": {
"id": 1,
"name": "Faishal D",
"email": "fai@example.com"
},
"book": {
"id": 2,
"title": "Rich Dad Poor Dad",
"author": "Robert Kiyosaki",
"price": 120000
},
"total_price": 120000
}

GET /orders/{user_id}
Melihat semua pesanan yang dibuat oleh user tertentu.

Contoh Response:
[
{
"order_id": 1,
"user": {
"id": 1,
"name": "John Doe",
"email": "john@example.com"
},
"book": {
"id": 2,
"title": "Rich Dad Poor Dad",
"author": "Robert Kiyosaki",
"price": 120000
},
"total_price": 120000
}
]

# Run Service

_UserService_
cd UserService
python app.py

_BookService_
cd BookService
python app.py

_OrderService_
cd OrderService
python app.py
