from flask import Flask
import os
from flask_login import LoginManager




def create_app():
  app = Flask(__name__)
  app.secret_key = b'\xba\xa2g\x0f\xdej\x97\xe6\xcd\xb6H\x19\xd7\x1e-\xfb\xbe-\x10C\x82:u7#ff\xda\x1a\x9c\xfcSY\x1c5'
  

  from .view import view

  app.register_blueprint(view, url_prefix="/")
  
  return app
