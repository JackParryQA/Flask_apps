from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms.fields.core import StringField
from wtforms.fields.simple import SubmitField
from wtforms.validators import DataRequired, Length, ValidationError
import re

app = Flask(__name__)
app.config['SECRET_KEY']='SOME_KEY'

class UserCheck:
    def __init__(self, banned, message=None):
        self.banned = banned
        if not message:
            message = 'Please choose another username'
        self.message = message
    
    def __call__(self, form, field):
        if field.data.lower() in (word.lower() for word in self.banned):
            raise ValidationError(self.message)

class NoSpecChars:
    def __init__(self, banned, message):
        self.banned=banned
        if not message:
            message = 'Please choose another username'
        self.message = message
        

    def __call__(self, form, field):
        attempted_username = field.data
        if self.banned.search(attempted_username) != None:
            raise ValidationError(self.message)
        


class MyForm(FlaskForm):
    username = StringField('Username', validators=[
        DataRequired(),
        UserCheck(message='custom rejection message', banned=['root','admin','sys']),
        NoSpecChars(message="Please don'tuse special characters i.e [@_!#$%^&*()<>?/\|}{~:]", banned=re.compile('[@_!#$%^&*()<>?/\|}{~:]')),
        Length(min=2,max=15)
    ])
    submit = SubmitField('Sign Up')

@app.route('/', methods=['GET','POST'])
def PostName():
    form = MyForm()
    if form.validate_on_submit():
        username = form.username.data
        return render_template('home.html', form=form, username=username)
    else:
        return render_template('home.html', form=form, username="")

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')