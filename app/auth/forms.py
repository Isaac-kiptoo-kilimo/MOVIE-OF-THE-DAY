from wtforms import StringField,PasswordField,BooleanField,SubmitField
from flask_wtf import FlaskForm
from wtforms.validators import DataRequired,Email,EqualTo
from wtforms import StringField,PasswordField,BooleanField,SubmitField
from wtforms import ValidationError

class LoginForm(FlaskForm):
    email = StringField('Your Email Address',validators=[DataRequired(),Email()])
    password = PasswordField('Password',validators =[DataRequired()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign In')