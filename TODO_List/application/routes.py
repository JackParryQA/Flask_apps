from flask import render_template, request, redirect, url_for
from application import app, db
from application.models import TODO_list
from application.forms import AddForm, UpdForm

@app.route('/')
def index():
    return "THIS IS A TODO LIST"

@app.route('/read')
def Todos():
    all_todos=TODO_list.query.all()
    # todo=""
    # for i in all_todos:
    #     todo+=f"id = {i.id}  ||  task = {i.task}  ||  complete = {i.complete}<br/>"
    # return todo
    return render_template('index.html', todos=all_todos)

@app.route('/add', methods=['GET', 'POST'])
def add():
    # new_todo = TODO_list(task="New Todo")
    # db.session.add(new_todo)
    # db.session.commit()
    # return "Added new todo to database"
    error=''
    form = AddForm()

    if request.method == 'POST':
        task = form.task.data
        if form.complete.data=='done':
            complete = True
        else:
            complete = False
    
        if len(task)==0:
            error-'Please enter task'
        else:
            new_todo = TODO_list(task = task, complete = complete)
            db.session.add(new_todo)
            db.session.commit()
            # return f"You've added a todo:<br>{new_todo.task}<br>{new_todo.complete}"
            return redirect(url_for('Todos'))

    return render_template('add.html', form=form, message=error)

@app.route('/complete/<int:num>')
def complete(num):
    todo = TODO_list.query.filter_by(id=num).first()
    todo.complete = True
    db.session.commit()
    # return f"Completed Todo!<br><br>Updated record: <br>{todo.id}<br>{todo.task}<br>{todo.complete}"
    return redirect(url_for('Todos'))

@app.route('/uncomplete/<int:num>')
def uncomplete(num):
    todo = TODO_list.query.filter_by(id=num).first()
    todo.complete = False
    db.session.commit()
    # return f"Todo is no longer complete!<br><br>Updated record: <br>{todo.id}<br>{todo.task}<br>{todo.complete}"
    return redirect(url_for('Todos'))

@app.route('/delete/<int:num>')
def delete(num):
    todo = TODO_list.query.filter_by(id=num).first()
    db.session.delete(todo)
    db.session.commit()
    # return f"TODO with id {num} has been successfully deleted"
    return redirect(url_for('Todos'))


@app.route('/update/<int:num>', methods=['GET', 'POST'])
def update(num):
    error=''
    form = UpdForm()

    todo = TODO_list.query.filter_by(id=num).first()
    # form.task.data = todo.task
    if request.method == 'POST':
        task = form.task.data
        if len(task)==0:
            error-'Please enter valid task'
        else:
            todo.task=task
            db.session.commit()
            # return f"You've added a todo:<br>{new_todo.task}<br>{new_todo.complete}"
            return redirect(url_for('Todos'))
    return render_template('update.html', form=form, message=error, task=todo)
