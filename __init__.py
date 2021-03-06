from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
#from flask_cors import CORS
from flask_jwt import JWT

from home_back.config.config import app_config

db = SQLAlchemy()






def create_app(config_name):
	app = Flask(__name__, instance_relative_config=True)
	app.config.from_object(app_config[config_name])
	db.init_app(app)
	api = Api(app)
	#TODO: Generate secret key

	#import Resources

	from home_back.resources.weather import Weather, WeatherPrefs
	url_prefix = "/api/v1"

	api.add_resource(Weather, url_prefix + '/weather', url_prefix + '/weather/<string:city_name>')
	api.add_resource(WeatherPrefs, url_prefix + '/weather/config')

	
	return app
	
