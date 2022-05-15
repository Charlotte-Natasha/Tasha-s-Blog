from crypt import methods
from . import main_blueprint
from flask import render_template, url_for
from .forms import LogIn


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

# @main_blueprint.route('/quotes')
# def quotes():
#     return render_template('quotes.html') 

@main_blueprint.route('/login', methods=['GET', 'POST'] )
def login():
    form=LogIn()
    # if form.validate_on_submit():
    #     user=User.query.filter_by(username = form.username.data).first()
    #     print(user)
    #     if user is not None and user.verify_password(form.password.data):
    #         print('Hello')
    #         login_user(user,form.remember.data)
    #         return redirect(request.args.get('next') or url_for('main.pitch'))
            

        # flash('Invalid username or Password')
        
    return render_template('login.html', form=form)          