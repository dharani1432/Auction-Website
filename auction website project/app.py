from flask import Flask, render_template, request, redirect, url_for
from datetime import datetime

app = Flask(__name__)

# Dummy data for products
products = [
    {'id': 1, 'name': 'Laptop', 'description': 'High-end gaming laptop', 'starting_price': 1000, 'current_bid': 0, 'end_time': '2025-02-28 12:00:00'},
    {'id': 2, 'name': 'Smartphone', 'description': 'Latest model smartphone', 'starting_price': 500, 'current_bid': 0, 'end_time': '2025-02-22 12:00:00'}
    
]

# Route for home page with product listings
@app.route('/')
def index():
    return render_template('index.html', products=products)

# Route to view a specific product
@app.route('/product/<int:product_id>', methods=['GET', 'POST'])
def product(product_id):
    product = next((prod for prod in products if prod['id'] == product_id), None)
    if request.method == 'POST':
        bid_amount = float(request.form['bid'])
        if bid_amount > product['current_bid']:
            product['current_bid'] = bid_amount
            return redirect(url_for('product', product_id=product_id))
    return render_template('product.html', product=product)

# Run the app
if __name__ == '__main__':
    app.run(debug=True)
