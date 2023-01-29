from flask import Blueprint
from flask import render_template
from flask import request

auth = Blueprint("auth", __name__)

@auth.route('/login', methods = ['POST', 'GET'])
def login():
    formData = request.form
    print(formData)
    return render_template("login.html")
#this one executes the verbwire script
@auth.route('/complete2')
def complete2():
    return complete()
@auth.route('/logout')
def logout():
    return render_template("logout.html")
@auth.route('/jobpost1')
def jobpost1():
    return render_template("jobpost1.html")
@auth.route('/jobpost2')
def jobpost2():
    return render_template("jobpost2.html")
@auth.route('/jobpost3')
def jobpost3():
    return render_template("jobpost3.html")
@auth.route('/jobboard')
def jobboard():
    return render_template("jobboard.html")
@auth.route('/complete')
def complete():
    return render_template("complete.html")
#default route http method is GET, so we have to add POST as well to utilize it without error
@auth.route('/signUp', methods = ["POST", "GET"])
def signUp():
    #if a POST request was made, grab the values from the form and store them in variables email, userName, and password
    if request.method == "POST":
        email = request.form.get('email')
        userName = request.form.get('userName')
        password = request.form.get('password')
        if len(email) > 3:
            pass
        elif len(password) > 0:
            pass
        elif len(userName) > 0:
            pass
    #if email 3 letters, or password is more than 0, and userName is more than 0, then value was inputted so add this user to the database

    #conditions 
    formData = request.form
    print(formData)
    return render_template("signUp.html")
