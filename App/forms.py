from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SelectField, SubmitField
from wtforms.validators import DataRequired, Length, EqualTo, Email


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             DataRequired(), Length(min=6)])
    submit = SubmitField(label='Log In')


class RegisterForm(FlaskForm):
    username = StringField(label='User name', validators=[
                           Length(min=3, max=12), DataRequired()])
    email = StringField(label='Email', validators=[DataRequired(), Email()])
    password = PasswordField(label='Password', validators=[
                             Length(min=6), DataRequired()])
    password_confirm = PasswordField(
        label='Confirm password', validators=[EqualTo('password'), DataRequired()])
    first_name = StringField(label='First name', validators=[DataRequired()])
    middle_name = StringField(label='Middle name', validators=[])
    last_name = StringField(label='Last name', validators=[DataRequired()])
    phone = StringField(label='Phone', validators=[DataRequired()])
    gender = SelectField(label='Gender', choices=['Male', 'Female'], validators=[
                         DataRequired()], default="Male")
    submit = SubmitField(label='Register')
