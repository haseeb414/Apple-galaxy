from flask import Flask, render_template, jsonify

app = Flask(__name__)

# Sample products data
products = [
    {"id": 1, "name": "Product 1", "price": 20, "image": "https://via.placeholder.com/150"},
    {"id": 2, "name": "Product 2", "price": 35, "image": "https://via.placeholder.com/150"},
    {"id": 3, "name": "Product 3", "price": 50, "image": "https://via.placeholder.com/150"}
]

@app.route("/")
def homepage():
    return render_template("index.html", products=products)

@app.route("/product/<int:product_id>")
def product_page(product_id):
    product = next((p for p in products if p["id"] == product_id), None)
    return render_template("product.html", product=product)

@app.route("/cart")
def cart_page():
    return render_template("cart.html")

@app.route("/api/products")
def get_products():
    return jsonify(products)

if __name__ == "__main__":
    app.run(debug=True)
