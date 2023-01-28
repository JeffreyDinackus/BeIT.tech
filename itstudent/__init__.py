from flask import Flask, render_template
app = Flask(__name__)


app.app_context().push()

from itstudent import routes


