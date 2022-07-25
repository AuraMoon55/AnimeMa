from flask.blueprints import Blueprint
from flask import render_template, request, flash
import secureme

view = Blueprint("view", __name__)

@view.route("/", methods=("GET", "POST"))
async def home():
  if request.method == 'POST':

    if not request.args['manga']:
      flash('Please Choose Type Of Query', category='error')

    if not request.args['query']:
      flash('Please Enter Query To Search', category='error')

    result = get_results(request.args['manga'], request.args['query'])
    return render_template('home.html', results=result, query=request.args['query'])


  return render_template("home.html", form=form)


def get_results(cate, query):
  jikan = Jikan()
  res = jikan.search(cate, query)['results']
  results = []
  for result in results:
    resp = {}
    if cate == 'anime':
      resp['title'] = result['title']
      
    else:
      
