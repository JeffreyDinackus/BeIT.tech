from flask import Flask, render_template
from itstudent import routes
app = Flask(__name__)
app.app_context().push()


