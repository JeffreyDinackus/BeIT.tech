from flask import Blueprint

auth = Blueprint("auth", __name__)

@auth.route('/login')
def login():
    return "<p>Login</p>"

@auth.route('/logout')
def logout():
    return "<p>logout</p>"

@auth.route('/signUp')
def signUp():
    return "<h1> This is the signUp page</h1>"