import os

class Config(object):
	"""Parent config class"""
	DEBUG = False
	CSRF_ENABLED = True
	SECRET = "LOL LOL ICH BIN EIN SECRET KEX"
	SQLALCHEMY_DATABASE_URI = "sqlite:///home.db"
	SQLALCHEMY_TRACK_MODIFICATIONS = False
	
class DevelopmentConfig(Config):
	"""Config for dev"""
	DEBUG = True
	
class TestingConfig(Config):
	"""Config for testing, with separate database"""
	TESTING = True
	SQLALCHEMY_DATABASE_URI = 'sqlite:///testing.db"
	DEBUG = True
	
class StagingConfig(Config):
	"""Config for staging"""
	DEBUG = True
	
class ProductionConfig(Config):
	DEBUG = False
	TESTING = False

app_config = {
	'development': DevelopmentConfig,
	'testing': TestingConfig,
	'staging': StagingConfig,
	'production': ProductionConfig,
}
