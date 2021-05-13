from flask_wtf.form import FlaskForm
from wtforms.fields.core import RadioField, StringField
from wtforms.fields.simple import SubmitField

class AddForm(FlaskForm):
    task = StringField('Task')
    complete = RadioField('Complete', choices=[('not_done', 'Not Done'), ('done', 'Done')], default='not_done')
    submit = SubmitField('Add Todo')

class UpdForm(FlaskForm):
    task = StringField('Task')
    submit = SubmitField('Update')

