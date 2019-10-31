from flask import Blueprint

from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    user_collection = mongo.db.recruiters
    user_collection.insert({'name' : 'Cristina'})
    return '<h1>Added a Recruiter!</h1>'