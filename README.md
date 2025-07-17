# 🍬 Kata Sweet Shop Management System

A full-featured Sweet Shop Management System developed in **Python** using **Flask** for the web frontend and **Pytest** for testing, following **Test-Driven Development (TDD)** principles.

## 📌 Project Overview

This system is designed to simulate a real-world sweet shop management workflow, allowing users to:
- Add, delete, restock, and purchase sweets
- View, sort, and search sweets by name, category, and price range
- Use a modern, responsive web interface
- Generate automated test reports using `pytest-html`

---

## 🛠️ Tech Stack

| Layer         | Tools Used                  |
|---------------|-----------------------------|
| Backend       | Python 3, Flask             |
| Frontend      | HTML, CSS, JavaScript       |
| Testing       | Pytest, pytest-html         |
| Version Control | Git & GitHub              |

---

## 🎯 Features

✅ Add new sweets to the inventory  
✅ Delete sweets by ID  
✅ Purchase sweets with quantity validation  
✅ Restock existing sweets  
✅ Search by name and category  
✅ Sort sweets by name and price  
✅ Responsive and attractive UI  
✅ Pytest-based test suite with HTML reports  

---

## 🧪 Run Tests

To run the test suite and generate an HTML report:

```bash
pip install -r requirements.txt
pytest --html=report.html --self-contained-html

