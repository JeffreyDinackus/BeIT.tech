from flask import Flask, render_template
from logging import FileHandler,WARNING
app = Flask(__name__, template_folder = 'template')
file_handler = FileHandler('errorlog.txt')
file_handler.setLevel(WARNING)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/register")
def register():
    return render_template("register.html")

@app.route("/forum")
def forum():
    return render_template("forum.html")


if __name__ == "__main__":
    app.run()






