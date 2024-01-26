import os
from flask import Flask
from pymongo import MongoClient

connection_string = os.environ.get('MONGO_URI')

client = MongoClient(connection_string)
db = client.movie_recommender_system

def create_app():

    app = Flask(__name__)

    app.config['MONGO_URI'] = os.environ.get('MONGO_URI')

    from .home import home
    from .model import insert_into_db
    # insert_into_db() # First time just to create a collection in MonogDB.

    app.register_blueprint(home, url_prefix='/')

    return app

