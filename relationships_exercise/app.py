from re import T
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app=Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.31.25:3306/relationships' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

class Customers(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)

class Products(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    name=db.Column(db.String(100), nullable=False)
    price=db.Column(db.Float(10,2), nullable=False, default=0.00)
    chosen_item=db.relationship('Chosen_Items', backref='product')

class Orders(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    customer_id=db.Column(db.Integer, db.ForeignKey('customers.id'), nullable=False)
    price=db.Column(db.Float(10,2), nullable=False)
    chosen_item=db.relationship('Chosen_Items', backref='order')

class Chosen_Items(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    product_id=db.Column(db.Integer, db.ForeignKey('products.id'), nullable=False)
    order_id=db.Column(db.Integer, db.ForeignKey('orders.id'), nullable=False)
    

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')