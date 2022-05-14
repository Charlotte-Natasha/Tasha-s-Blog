from . import main_blueprint
from flask import render_template

@main_blueprint.route('/')
def index():
    return render_template('index.html')

@main_blueprint.route('/blog')
def blog():
    return render_template('blog.html') 

@main_blueprint.route('/about')
def navbar():
    return render_template('about.html')       