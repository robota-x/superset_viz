from configparser import RawConfigParser

config = RawConfigParser()
config.read("config.ini")

MAPBOX_API_KEY = config["SUPERSET"]["mapbox_api_key"]
SECRET_KEY = config["SUPERSET"]["secret_key"]

SQLALCHEMY_DATABASE_URI = f"{config['DATABASE']['location']}_main"
ENABLE_JAVASCRIPT_CONTROLS = True