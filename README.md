# 🍽️ Restaurant Management System

A complete **Restaurant Management System** built using **Python**, **Tkinter** for GUI, and **MySQL** for the database.

This project includes both **Admin** and **Customer** sides, allowing management of food menu, orders, and table reservations with a user-friendly interface.

---

## 📁 Project Structure

restaurant-management/
├── admin_app.py # Admin panel (Add/Update/Delete food, manage orders)
├── customer_app.py # Customer panel (browse menu, order, reservation)
├── db_setup.py # Optional: SQL setup for creating tables
├── README.md # This file
└── requirements.txt # Python dependencies



---

## 🚀 Features

### 👨‍🍳 Admin Panel (`admin_app.py`)
- Add, delete, and update food items
- View and complete customer orders
- View past delivered orders
- View table reservations

### 🧑‍🍽️ Customer Panel (`customer_app.py`)
- Browse menu and place orders
- Provide delivery address and contact number
- View cart and total bill
- Reserve a table (name, contact, date, time, people)

---

## 🛠️ Installation

### Requirements:
- Python 3.x
- MySQL Server
- Python Modules:
  - `mysql-connector-python`
  - `tkinter` (comes with Python)
  - `re`

Install dependencies:
```bash
pip install mysql-connector-python


🧩 MySQL Setup
1. Create a database:
sql
Copy
Edit
CREATE DATABASE project;

2. Tables to create:
sql
Copy
Edit
CREATE TABLE menu (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dish VARCHAR(255),
    price INT
);

CREATE TABLE reservations (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    phone VARCHAR(15),
    date DATE,
    time TIME,
    people INT
);

CREATE TABLE Order_detail (
    id INT AUTO_INCREMENT PRIMARY KEY,
    dish VARCHAR(255),
    price INT,
    quantity INT,
    phone VARCHAR(15),
    address VARCHAR(255)
);
