
class BaseConfig(object):
    DEBUG = True

    SQLALCHEMY_DATABASE_URI = 'sqlite:///home.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SECRET_KEY = "LOL_LOL_ICH_BIN_EIN_KEY"
