from flask import Flask
from os import path
from flask_login import LoginManager
import json
from flask_mail import Mail

mail = Mail()

with open("config.json", "rb") as data:
  config = json.loads(data.read())

def create_app():
  app = Flask(__name__)
  app.secret_key = b'\xba\xa2g\x0f\xdej\x97\xe6\xcd\xb6H\x19\xd7\x1e-\xfb\xbe-\x10C\x82:u7#ff\xda\x1a\x9c\xfcSY\x1c5'
  app.config.update(
    MAIL_SERVER = "smtp.gmail.com",
    MAIL_PORT = '465',
    MAIL_USE_SSL = True,
    MAIL_USERNAME = config.get("mail_username"),
    MAIL_PASSWORD = config.get("mail_pass")
  )
  mail.init_app(app)

  from .view import view

  app.register_blueprint(view, url_prefix="/")
  
  return app