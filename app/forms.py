from flask_wtf import FlaskForm
from wtforms import StringField, TextAreaField, SubmitField, PasswordField
from wtforms.validators import DataRequired, EqualTo, Email
#user to product
class Create_product(FlaskForm):
        product_name = StringField('Product Name', validators=[DataRequired()])
        price = StringField('Product Price', validators=[DataRequired()])
        image = TextAreaField('Image URL')
        submit = SubmitField()

class RegisterForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    confirm_pass = PasswordField('Confirm Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField()

class LoginForm(FlaskForm):
        username = StringField('Username', validators=[DataRequired()])
        email = StringField('Email', validators=[DataRequired(), Email()])
        password = StringField('Password', validators=[DataRequired()])
        submit = SubmitField()