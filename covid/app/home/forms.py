# app/auth/forms.py

from flask_wtf import FlaskForm
from wtforms import PasswordField, StringField, SubmitField, ValidationError, SelectField
from wtforms.validators import DataRequired, Email, EqualTo
from flask_wtf.file import FileField
from wtforms.fields.html5 import DateField
#from ..models import Employee



class File_form(FlaskForm):
    """
    Form for users to login
    """
    email = StringField('Gmail', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    option =  SelectField(label='Choose an Option', choices=['Mail to departments', 'Mail to Primary contacts'])
    file = FileField('Excel file', validators=[DataRequired()])
    submit = SubmitField('Next')