from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField,PasswordField,ValidationError,BooleanField
from wtforms.validators import Required,EqualTo,Email 
from ..models import User

class RegistrationForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(),Email()])
    username = StringField('Enter your name',validators=[Required()])
    password = PasswordField('Password',validators=[Required(), EqualTo('password_confirm',message='Passwords must match')])
    password_confirm = PasswordField('Confirm passwords',validators=[Required()])
    submit = SubmitField('Sign Up')

    def validate_email(self,data_field):
        if User.query.filter_by(email = data_field.data).first():
            raise ValidationError('There is an account with that email')

    def validate_username(self,data_field):
        if User.query.filter_by(username = data_field.data).first():
            raise ValidationError('The username is already taken')

class LoginForm(FlaskForm):
    email = StringField('Your email address',validators=[Required(),Email()])
    password = PasswordField('Password',validators=[Required()])
    remember = BooleanField('Remember me')
    submit = SubmitField('Sign Up')


