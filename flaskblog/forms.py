from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo

class RegistrationForm(FlaskForm):
	username = StringField('Username', 
		validators=[DataRequired(), Length(min=2,max=20)])
		# import validators for checking
	
	email = StringField('Email',
		validators=[DataRequired(), Email()])

	password = PasswordField('Password',
		validators=[DataRequired(), Length(min=8,max=50)])
    
	confirm_pass = PasswordField('Confirm Password',
		validators=[DataRequired(), EqualTo('password')])

	submit_button = SubmitField('Sign up')


class LoginForm(FlaskForm):	
	email = StringField('Email',
		validators=[DataRequired(), Email()])

	password = PasswordField('Password', 
		validators=[DataRequired()])
	
	remember = BooleanField('Remember me')

	submit_button = SubmitField('Login')
    