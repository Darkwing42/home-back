from mongoengine import *
import datetime


class Item(EmbeddedDocument):
	name = StringField(max_length=200)
	quantity = IntField(min_value=0)
	done = BooleanField(default=False)

	def to_dict(self):
		template = {
			"name": self.name,
			"quantity": self.quantity,
			"done": self.done
		}
		return template

class ShoppingList(Document):
	title = StringField(max_length=200, required=True)
	done = BooleanField(default=False)
	created_at = DateTimeField(default=datetime.datetime.now)
	items = ListField(EmbeddedDocumentField(Item))
	
	def to_dict(self):
		template = {
			"title": self.title,
			"done": self.done,
			"created_at": self.created_at.strftime('%d-%m-%Y'),
			"items": [ item.to_dict() for item in self.items ]
		}
		return template
