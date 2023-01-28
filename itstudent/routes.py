from flask import Blueprint

routes = Blueprint("routes", __name__)

#Register these blueprints in our init pi

@routes.route('/')
def home():
    return "<h1> This is the home page</h1>"





