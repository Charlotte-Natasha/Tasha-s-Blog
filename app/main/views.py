from . import main_blueprint
from flask import render_template

@main_blueprint.route('/home')
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

# @main_blueprint.route('/about')
# def navbar():
#     return render_template('about.html')         