from flask import Flask, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from flask_marshmallow import Marshmallow
import os

# Init app
app = Flask(__name__)
basedir = os.path.abspath(os.path.dirname(__file__))

# database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir,'db.sqlite')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Init DB
db = SQLAlchemy(app)

# Init ma
ma = Marshmallow(app)

# Product Model
class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(100),unique = True)
    description = db.Column(db.String(200))
    price = db.Column(db.Float)
    qty = db.Column(db.Integer)

    def __init__(self, name, description, price, qty):
        self.name = name
        self.description = description
        self.price = price
        self.qty = qty

# Product schema
class ProductSchema(ma.Schema):
    class Meta:
        fields = ('id', 'name', 'description', 'price', 'qty')

# Init schema
product_schema = ProductSchema()
products_schema = ProductSchema(many=True)

# Create a Product
@app.route('/product', methods = ['POST'])
def add_product():
   name = request.json['name']
   description = request.json['description']
   price = request.json['price']
   qty = request.json['qty']   
   
   new_product = Product(name, description, price, qty)

   db.session.add(new_product)
   db.session.commit()

   return product_schema.jsonify(new_product)

# Get all products
@app.route('/product', methods = ['GET'])
def get_products():
   all_products = Product.query.all()
   result = products_schema.dump(all_products)
   return jsonify(result)

# Get Single products
@app.route('/product/<id>', methods = ['GET'])
def get_single_product(id):
   product = Product.query.get(id)   
   return product_schema.jsonify(product)

# Update Product
@app.route('/product/<id>', methods = ['PUT'])
def update_product(id):
   product = Product.query.get(id)   

   name = request.json['name']
   description = request.json['description']
   price = request.json['price']
   qty = request.json['qty']   
   
   product.name = name
   product.description = description
   product.price = price
   product.qty = qty

   db.session.commit()

   return product_schema.jsonify(product)

# Delete product
@app.route('/product/<id>', methods = ['DELETE'])
def delete_single_product(id):
   product = Product.query.get(id)   
   db.session.delete(product)
   db.session.commit()
   return product_schema.jsonify(product)
   
# @app.route('/',methods=['GET'])
# def get():
#     return jsonify({'msg':'Hello world'})

# Run Server
if __name__ == '__main__':
    app.run(debug=True)