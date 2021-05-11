from app import db, TODO_list

db.drop_all()
db.create_all()

todo1=TODO_list(task='clean dishes', complete=True)
todo2=TODO_list(task='take out bins', complete=False)
todo3=TODO_list(task='complete TODO list taske', complete=True)

db.session.add(todo1)
db.session.add(todo2)
db.session.add(todo3)
db.session.commit()
