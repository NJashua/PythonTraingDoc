from flask import Flask, request, jsonify, redirect
from flask_sqlalchemy import SQLAlchemy
my_product = Flask(__name__)
my_product.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///empdb.db'

db = SQLAlchemy(my_product)

class Product(db.Model):
    Product_id = db.Column(db.Integer, primary_key = True)
    Product_name = db.Column(db.String(100))
    Product_price = db.Column(db.Integer)
    Product_delivery_date = db.Column(db.String)

    def to_dict(self):
        return {
            'Product_id':self.Product_id,
            'Product_name': self.Product_name,
            'Product_price': self.Product_price,
            'Product_delivery_date': self.Product_delivery_date
        }

@my_product.before_request
def create_tables():
    db.create_all()

@my_product.route('/get_all_products', methods = ['GET'])
def get_all_products():
    try:
        data = Product.query.all()
        return jsonify([product.to_dict() for product in data])
    except Exception as msg:
        print("No products found in the table", msg)

@my_product.route("/add_product", methods = ['POST'])
def add_product_data():
    try:
        data = request.get_json()
        new_product = Product(
            Product_id=data['Product_id'],
            Product_name=data['Product_name'],
            Product_price=data['Product_price'],
            Product_delivery_date=data['Product_delivery_date']
        )
        db.session.add(new_product)
        db.session.commit()
        return {"Message": "New product added into the table, have a look!"}, 200
    except Exception as msg:
        print("Getting error in connection", msg)
        return {"Message": "Error adding product"}, 500
@my_product.route("/delete_product", methods = ['DELETE'])
def delete_product_data():
    try:
        data = request.get_json()
        product_id = data.get('Product_id')
        product = Product.query.get(product_id)
        if product:
            db.session.delete(product)
            db.session.commit()
            return jsonify({"message": "Product deleted "}), 200
        else:
            return jsonify({'message' : "Product not found"}), 404
    except Exception as message:
        print("Getting error in the try block have a look on that", message)

if __name__ == "__main__":
    my_product.run(debug=True)