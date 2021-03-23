from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, SelectField
from wtforms.validators import DataRequired, Email, NumberRange

class UserForm(FlaskForm):
    name = StringField('Name', validators=[InputRequired("Enter Your Name")])
    email = StringField('Email', validators=[DataRequired("Enter Your Email"), Email("This field requires a valid email")])
    year = SelectField('Birth Year', choices=[(year, year) for year in range(1900,2001)], validators=[InputRequired("Enter a year between 1900-2001")])
    color = SelectField('Color', choices=[('red', 'red'), ('green', 'green'), ('orange', 'orange'), ('blue', 'blue')], validators={InputRequired("Available options are red, green, orange, blue.")})