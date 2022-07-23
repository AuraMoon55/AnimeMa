from flask import Flask
import os
from flask_login import LoginManager
from dotenv import load_dotenv
from flask_mail import Mail
from flask_mongoengine import MongoEngine


load_dotenv()

mongo = MongoEngine()


def create_app():
  app = Flask(__name__)
  app.secret_key = b'\xba\xa2g\x0f\xdej\x97\xe6\xcd\xb6H\x19\xd7\x1e-\xfb\xbe-\x10C\x82:u7#ff\xda\x1a\x9c\xfcSY\x1c5'
  app.config.update(
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME"),
    MAIL_PASSWORD = os.environ.get("MAIL_PASS")
  )
  app.config['MONGODB_SETTINGS'] = {
    "db": __name__,
    "host": os.environ.get("MONGO_URI")
  }
  mail.init_app(app)
  mongo.init_app(app)
  

  from .view import view

  app.register_blueprint(view, url_prefix="/")
  
  return app
