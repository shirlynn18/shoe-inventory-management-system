# 🥿 Python-Based Inventory Management System

A **text-based inventory system** built using Python for the **CSC1024 Programming Principles** course. This system provides essential inventory and order management features for small businesses.

---

## 📌 Project Overview

This project is designed to simulate a basic inventory system that can:

- Add and manage product data  
- Handle supplier records  
- Place and track orders  
- View current inventory  
- Generate reports (low stock, sales, suppliers)  

The system uses a **menu-driven interface** and stores all records in `.txt` files. It's an efficient solution for understanding core programming concepts like input validation, file handling, and modular function design in Python.

---

## 📁 Features

### 🛍️ Inventory Management
- **Add Product**: Add new product records with ID, name, description, stock quantity, and price.
- **Update Product**: Modify product details with validation to ensure correctness.
- **View Inventory**: View all products in the inventory file.

### 🤝 Supplier Management
- **Add Supplier**: Register suppliers with ID, name, and validated contact number.

### 📦 Order Processing
- **Place Order**: Place orders with product ID, quantity, and order date.
- **Order Validation**: Ensure ordered product exists before confirming order.

### 📊 Reporting
- **Low Stock Report**: List items with stock below a certain threshold.
- **Sales Report**: Calculate revenue per product from orders.
- **Supplier Report**: Display all registered suppliers.

### 🚪 Exit
- Clean exit from the system with data-saving confirmation.

---

## 🧠 System Design

- Written in **Python**
- Data stored in `.txt` files (`products.txt`, `suppliers.txt`, `orders.txt`)
- Uses **regular expressions**, **error handling**, and **file I/O**
- Modular function-based design for each system feature

---

## 🛠 How to Run

1. Make sure you have **Python 3.x** installed.
2. Clone this repo or download the files.
3. Run the main script in terminal:

```bash
python System.py
