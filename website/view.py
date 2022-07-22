from flask.blueprints import Blueprint

view = Blueprint("view", __name__)

@view.route("/")
async def home():
  return "<h3>I'm Alive</h3>"