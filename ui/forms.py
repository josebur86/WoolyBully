from flask_wtf import Form
from wtforms.fields import TextField, SubmitField, SelectField, IntegerField, FormField, PasswordField
from wtforms.validators import InputRequired, Email, ValidationError
from wtforms.fields.html5 import EmailField

class signInForm(Form):
	email = EmailField("Email", validators=[InputRequired("Please enter your email address."), Email("Please enter a valid email address.")])
	password = PasswordField("Password", validators=[InputRequired("Please enter your password.")])
	submit = SubmitField("Sign In")

	def __init__(self, *args, **kwargs):
		Form.__init__(self, *args, **kwargs)

	def validate(self):
		if not Form.validate(self):
			return False
