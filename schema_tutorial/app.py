from enum import unique
from flask import Flask # Import Flask class
from flask_sqlalchemy import SQLAlchemy # Import SQLAlchemy class

app = Flask(__name__) # create Flask object

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.31.25:3306/mydb' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app) 

class Users(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    firstname=db.Column(db.String(100), nullable=False)
    surname=db.Column(db.String(100), nullable=False)

# schema exercise -- these tables will be used in my project
# class Customers(db.Model):
#     customer_id=db.Column(db.Integer, primary_key=True)
#     firstname=db.Column(db.String(100), nullable=False)
#     surname=db.Column(db.String(100), nullable=False)
#     email=db.Column(db.String(50), nullable=False, unique=True)
#     phone_num=db.Column(db.String(20), nullable=False, unique=True)
#     address=db.Column(db.String(200), nullable=False)
#     postcode=db.Column(db.String(10), nullable=False)


class Job(db.Model):
    job_id=db.Column(db.Integer, primary_key=True)
    customer_id=db.Column(db.Integer, nullable=False)
    description=db.Column(db.String(200), nullable=False)
    price=db.Column(db.Float(10,2), nullable=False, default=0.00)

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')


