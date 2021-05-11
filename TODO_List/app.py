from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.orm import query

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://root:root@35.246.31.25:3306/todo' 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False 
db = SQLAlchemy(app)

@app.route('/')
def index():
    return "THIS IS A TODO LIST"

class TODO_list(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    task=db.Column(db.String(100), nullable=False)
    complete=db.Column(db.Boolean, default=False, nullable=False)

# (stretch task)
@app.route('/Todos')
def Todos():
    all_todos=TODO_list.query.all()
    todo=""
    for i in all_todos:
        todo+=f"id = {i.id}  ||  task = {i.task}  ||  complete = {i.complete}<br/>"
    return todo

if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')
