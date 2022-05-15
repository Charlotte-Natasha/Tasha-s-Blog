from . import main_blueprint
from flask import render_template, url_for, redirect, flash, request
from .forms import LogIn, Signup
from ..model import User
from flask_login import login_user, logout_user
from app import db

@main_blueprint.route('/home')
@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/blogs')
def blogs():
    return render_template('blog.html') 

@main_blueprint.route('/about')
def about():
    return render_template('about.html')       

@main_blueprint.route('/quotes')
def quotes():
    return render_template('quotes.html') 

@main_blueprint.route('/login', methods=['GET', 'POST'] )
def login():
    form=LogIn()
    if form.validate_on_submit():
        user=User.query.filter_by(username = form.username.data).first()
        if user is not None and user.verify_password(form.password.data):
            login_user(user,form.remember.data)
            return redirect(request.args.get('next') or url_for('main_blueprint.blog'))  

        flash('Invalid username or Password')
        
    return render_template('login.html', form=form)

@main_blueprint.route("/signup", methods=['POST', 'GET'])
def sign_up():
    signup_form = Signup()
    if signup_form.validate_on_submit():
        user = User(email = signup_form.email.data, username = signup_form.username.data,password = signup_form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Successfully signed in for {signup_form.username.data}', category='success')
        return redirect(url_for('main_blueprint.login'))   
    return render_template("signup.html", form=signup_form)      
