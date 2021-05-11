# import sys
# sys.path.append('D:\QA\QA Training\Flask_Apps\CRUD_tutorial')

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"

db = SQLAlchemy(app)

from application import routes