from itertools import product
from flask.helpers import flash
from wtforms.validators import Email
from app import app, db
from flask import render_template, redirect, url_for
from app.forms import Create_product, RegisterForm, LoginForm
from app.models import Product, User, CartTable
from flask_login import login_user, logout_user, current_user, LoginManager

@app.route('/')
def home_page():
    products = Product.query.all()
    return render_template('index.html', products=products)

@app.route('/about')
def about_page():
    return render_template('about.html')

@app.route('/create_product', methods = ['GET','POST'])
def create_product():
    form = Create_product()
    if form.validate_on_submit():
        product_name= form.product_name.data
        price=form.price.data
        image=form.image.data

        new_product= Product(product_name,price,image)

        db.session.add(new_product)
        db.session.commit()

        return redirect(url_for('home_page'))


    return render_template('create_product.html',hello=form)

@app.route('/products', methods=['GET','POST'])
def products():
    my_products=Product.query.all()

    return render_template('shop.html',products=my_products)

@app.route('/view_cart')
def view_cart():
    return render_template('cart.html')

@app.route('/login')
def login():
    return render_template('login.html')
#aaron edit
    

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        # Grab data from our submitted form
        username = form.username.data
        email = form.email.data
        password = form.password.data
        print(username, email, password)
        # Create new instance of User
        new_user = User(username, email, password)

        # Add new_user to our database
        db.session.add(new_user)
        db.session.commit()

        # Once new_user is added to db, flash success message
        flash(f'Thank you for signing up {new_user.username}!', 'danger')

        # Redirect user back to home page
        return redirect(url_for('login'))
    return render_template('register.html', title='Register to Buy!', form=form)


@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.username.data
        password = form.password.data
       #return the first user object
        user = User.query.filter_by(username=username).first()
        
        
        if user is None or user.check_password(password): 
            flash('Incorrect Username/Password. Try Again', 'danger')
            return redirect(url_for('login'))

        login_user(user)
        flash(f'Hello {username}, welcome back', 'success')
        print('something')
        return redirect(url_for('products'))


    return render_template('login.html', form=form)

@app.route('/view_cart')
def view_cart():
    return render_template('cart.html')

@app.route('/cart/<int:product_id>', methods=['POST', 'GET'])
def add_to_cart(product_id):
    # product = Product.query.filter(Product.id == product_id)
    # cart_item = CartTable(product=product)
    # db.session.add(cart_item)
    # db.session.commit()
    print(product_id)
    print(current_user.id)
    products = Product.query.all()
    return render_template('index.html', product=products)


def remove_from_cart(product_id):
    product = Product.query.filter(Product.id == product_id)
    cart_item = CartTable(product=product)
    db.session.remove(cart_item)
    db.session.commit()
    return render_template('index.html', product=products)

# @app.route('/view_cart')
# def view_cart():
#     return render_template('cart.html')

@app.route('/view_product')
def openproduct():
    form = Product()
    product = form.product_name.data
    price = form.price.data
    products_id = CartItem(product_id=itemid)
    db.session.add(products)
    db.session.commit()
    return render_template('index.html',products_id=products)
