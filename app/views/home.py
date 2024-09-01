from flask import Blueprint, render_template

# Create the home blueprint
home = Blueprint('home', __name__)

# Define the home route
@home.route('/')
@home.route('/home/')
def index():
    """This the home page view, it renders the home page template
    
    Keyword arguments:
    argument -- description
    Return: A response object with the rendered template
    """
    return "Everything is working fine"
