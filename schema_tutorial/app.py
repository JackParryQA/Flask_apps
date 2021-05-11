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

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')


