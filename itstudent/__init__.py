from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask(__name__)


db = SQLAlchemy(app)
app.app_context().push()

from itstudent import routes


