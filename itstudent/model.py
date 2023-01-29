from . import database
from flask_login import UserMixin

class jobPosting(database.Model):
    id = database.Column(database.Integer, primary_key =True)
    listingInfo = database.Column(database.String(5000))
    date = database.Column(database.DateTime(timezone=True))
    user_id = database.Column(database.Integer, database.ForeignKey('user.id'))



class User(database.Model, UserMixin):
    id = database.Column(database.Integer, primary_key =True)
    email = database.Column(database.String(100), unique=True)
    password = database.Column(database.String(100))
    username = database.Column(database.String(100))
    jobPostings = database.relationship("Note")


