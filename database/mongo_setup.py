from mongoengine import *

def global_init():
    #DATABASE DATA
    DB_NAME = "home"
    DB_HOST = "192.168.0.227"
    DB_PORT = 27017
    DB_USERNAME = "home"
    DB_PASSWORD = "test2345"


    #DATABASE CONNECTION
    connect(
        db=DB_NAME,
        username=DB_USERNAME,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )
