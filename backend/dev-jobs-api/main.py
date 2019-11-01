from flask import Blueprint, render_template

from .extensions import mongo 

main = Blueprint('main', __name__)

@main.route('/')
def index():
    #user_collection = mongo.db.recruiters
    #user_collection.insert({'name' : 'Cristina'})
    return render_template('index.html')

if __name__ == "__main__":
    app.run(debug=True)