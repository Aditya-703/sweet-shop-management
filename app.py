# Import necessary modules from Flask and your shop logic
from flask import Flask, render_template, request, redirect, url_for
from src.shop import SweetShop, Sweet

# Create Flask app instance
app = Flask(__name__)

# Create an instance of SweetShop and add initial sweets
shop = SweetShop()
shop.add_sweet(Sweet(1001, "Kaju Katli", "Nut-Based", 50, 20))
shop.add_sweet(Sweet(1002, "Gajar Halwa", "Vegetable-Based", 30, 15))
shop.add_sweet(Sweet(1003, "Gulab Jamun", "Milk-Based", 10, 50))


# Route for the homepage displaying all available sweets
@app.route("/")
def home():
    return render_template("index.html", sweets=shop.view_sweets())


# Route to handle adding a new sweet to the shop
@app.route("/add", methods=["POST"])
def add():
    try:
        sweet = Sweet(
            int(request.form["id"]),
            request.form["name"],
            request.form["category"],
            float(request.form["price"]),
            int(request.form["quantity"])
        )
        # Add the new sweet to the shop
        shop.add_sweet(sweet)
    except ValueError as e:
        return str(e)
    return render_template("index.html", sweets=shop.view_sweets(), message="Sweet added successfully!", error=None)


# Route to handle deleting a sweet from the shop
@app.route("/delete", methods=["POST"])
def delete():
    sweet_id = int(request.form["id"])
    shop.delete_sweet(sweet_id)
    return render_template("index.html", sweets=shop.view_sweets(), message="Sweet deleted successfully!", error=None)


# Route to handle purchasing sweets
@app.route("/purchase", methods=["POST"])
def purchase():
    try:
        id = int(request.form["id"])
        quantity = int(request.form["quantity"])
        shop.purchase_sweet(id, quantity)
        return render_template("index.html", sweets=shop.view_sweets(), message="Purchase successful!", error=None)
    except ValueError as e:
        return render_template("index.html", sweets=shop.view_sweets(), message=None, error=str(e))


# Route to handle restocking sweets
@app.route("/restock", methods=["POST"])
def restock():
    try:
        id = int(request.form["id"])
        quantity = int(request.form["quantity"])
        shop.restock_sweet(id, quantity)
        return render_template("index.html", sweets=shop.view_sweets(), message="Restock successful!", error=None)
    except ValueError as e:
        return render_template("index.html", sweets=shop.view_sweets(), message=None, error=str(e))



# Entry point to start the Flask app
if __name__ == "__main__":
    app.run(debug=True)
