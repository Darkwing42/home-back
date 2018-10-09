import os
#https://scotch.io/tutorials/build-a-restful-api-with-flask-the-tdd-way

from home_back import app, db
from flask_migrate import Migrate, MigrateCommand
from flask_script import Manager

#app = create_app(config_name=))
migrate = Migrate(app, db)
manager = Manager(app)

manager.add_command('db', MigrateCommand)

if __name__ == '__main__':
	manager.run()
