from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_cors import CORS
from flask_jwt import JWT


app = Flask(__name__)
app.config.from_object('home_back.config.BaseConfig')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
api = Api(app)



#TODO: Generate secret key

#import Resources
from home_back.resources.shoppingList import ShoppingList, ShoppingItem

url_prefix = "/api/v1"

api.add_resource(ShoppingList, url_prefix + '/shoppinglists')
