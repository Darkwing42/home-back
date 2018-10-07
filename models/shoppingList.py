from home_back import db
from datetime import datetime

class ShopppingList(db.Model):
	__tablename__= 'shoppinglists'

	id = db.Column(db.Integer, primary_key = True)
	done = db.Column(db.Boolean, default=False)
	title = db.Column(db.String(200), nullable=False)
	created_at = db.Column(db.DateTime, default=datetime.now)
	items = db.relationship('Item', backref="shoppinglist", lazy=False)

	def to_dict(self):
		return dict(
			id=self.id,
			done=self.done,
			title=self.title,
			created_at=self.created_at.strftime('%d-%m-%Y'),
			items=[item.to_dict() for item in self.items]
		)
class Item(db.Model):
	__tablename__ = "items"

	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(200), nullable=False)
	quantity = db.Column(db.Integer)
	done = db.Column(db.Boolean, default=False)
	shopppingList_id = db.Column(db.Integer, db.ForeignKey('shoppinglists.id'))

	def to_dict(self):
		return dict(id=self.id,
			name=self.name,
			quantity=self.quantity,
			done=self.done,
			shoppingList_id=self.shopppingList_id
		)



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
