from flask import Flask, render_template, request
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.fields.core import DateField, DecimalField, IntegerField, SelectField
from wtforms.widgets.core import Option

app = Flask(__name__)

app.config['SECRET_KEY'] = 'YOUR_SECRET_KEY'

class BasicForm(FlaskForm):
    first_name = StringField('First Name')
    last_name = StringField('Last Name')
    age = IntegerField('Age')
    birthday = DateField('Birthday', format='%d-%m-%Y')
    nationality = SelectField('Nationality', choices=[('wales', 'Wales'), ('scotland', 'Scotland'), ('n-ireland', 'Northern Ireland'), ('england', 'England')])
    decimal = DecimalField('Enter decimal')
    submit = SubmitField('Add Name')

@app.route('/', methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])
def register():
    error = ""
    form = BasicForm()

    if request.method == 'POST':
        first_name = form.first_name.data
        last_name = form.last_name.data
        age = form.age.data
        bday = form.birthday.data
        nationality = form.nationality.data
        dec = form.decimal.data


        if len(first_name) == 0 or len(last_name) == 0 or len(str(age))==0 or len(str(bday))==0 or len(nationality)==0 or len(str(dec))==0:
            error = "Please supply all fields"
        else:
            return f"Thank you {first_name} {last_name}"

    return render_template('home.html', form=form, message=error)

if __name__ == '__main__':
     app.run(debug=True, host='0.0.0.0')