from flask import Flask
from flask_restful import Api
#from flask_cors import CORS
from flask_jwt import JWT
import home_back.database.mongo_setup as mongo_setup

mongo_setup.global_init()
app = Flask(__name__)
api = Api(app)


app.secret_key = "Lolol lol ich bin ein secret key"
#TODO: Generate secret key

#import Resources
from home_back.resources.shoppingList import ShoppingList, ShoppingItem

url_prefix = "/api/v1"

api.add_resource(ShoppingList, url_prefix + '/shoppinglists')
