from flask import Blueprint

routes = Blueprint("routes", __name__)
from flask import render_template

#Register these blueprints in our init pi

@routes.route('/')
def home():
    return render_template('home.html')






