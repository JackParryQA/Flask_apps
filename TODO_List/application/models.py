from application import db

class TODO_list(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    task=db.Column(db.String(100), nullable=False)
    complete=db.Column(db.Boolean, default=False, nullable=False)