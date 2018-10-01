from flask_restful import Resource, reqparse
from mongoengine import *
from home_back.models.shoppingList import ShoppingList, Item

class ShoppingList(Resource):
	def get(self):
		#TODO: get all Shopping Lists
		lists = ShoppingList.objects()

		return { 'shoppinglists': [ list.to_dict() for list in lists ]}, 201

class ShoppingItem(Resource):
	def get(self, name):
		#TODO:get one shopping list
		pass
	def post(self):
		#TODO: save one new shopping list
		pass
	def put(self, name):
		#TODO: save one new or update a existing shopping list
		pass
