from app import db,login
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin
#change////
@login.user_loader
def load_user(user_id):
    return User.get(user_id)
# @login.der
# def load_user(user_id):
#     return User.query.get(user_id)
  


class CartTable(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    user_table=db.Column(db.Integer(), db.ForeignKey('user.id'))
    product_table=db.Column(db.Integer(), db.ForeignKey('product.id'))
    

class Product(db.Model):
    id=db.Column(db.Integer(),primary_key=True)
    product_name=db.Column(db.String(50),nullable=False, unique=True)
    price=db.Column(db.Float(),nullable=False)
    image=db.Column(db.String())
    def __init__(self,product_name,price,image):
        self.product_name=product_name
        self.price=price
        self.image=image


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), nullable=False, unique=True)
    email = db.Column(db.String(50), nullable=False, unique=True)
    password = db.Column(db.String(256), nullable=False)
    def __init__(self, username, email, password):
        self.username = username
        self.email = email
        self.password = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password, password)

