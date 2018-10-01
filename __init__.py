from flask import Flask
from flask_restful import Api
from flask_cors import CORS
from mongoengine import *
from flask_jwt import JWT

app = Flask(__name__)
api = Api(app)

app.secret_key = "Lolol lol ich bin ein secret key"
#TODO: Generate secret key

#import Resources
from home-back.resources.shoppingList import ShoppingList, ShoppingItem 

url_prefix = "/api/v1"

api.add_resource(ShoppingList, url_prefix + '/shoppinglists')
api.add_resource(ShoppingItem, url_prefix + '/shoppinglist', url_prefix + '/shoppinglist/<str:title>')
