from flask.blueprints import Blueprint
from flask import render_template, request, flash
from jikanpy import Jikan

view = Blueprint("view", __name__)

@view.route("/", methods=("GET", "POST"))
async def home():
  if request.args:
    if not request.args['manga']:
      flash('Please Choose Type Of Query', category='error')

    if not request.args['query']:
      flash('Please Enter Query To Search', category='error')

    result = get_results(request.args['manga'], request.args['query'])
    return render_template('home.html', results=result, query=request.args['query'])


  return render_template("home.html")


def get_results(cate, query):
  jikan = Jikan()
  res = jikan.search(cate, query)['results']
  results = []
  for result in res:
    resp = {}
    resp['img'] = result['image_url']
    resp['title'] = result['title']
    resp['about'] = {}
    resp['description'] = []
    num = int(len(result['synopsis'])/16)
    for x in range(num):
      resp['description'].append(result['synopsis'][(x):(x+17)])
    if cate == 'anime':
      resp['about']['airing'] = result['airing']
      resp['about']['type'] = result['type']
      resp['about']['episodes'] = result['episodes']
      resp['about']['rating'] = result['rated']
      resp['about']['score'] = result['score']
      resp['about']['start_date'] = (result['start_date'] or 'N/A')[:10]
      resp['about']['end_date'] = (result['end_date'] or 'N/A')[:10]
    else:
      resp['about']['publishing'] = result['publishing']
      resp['about']['type'] = result['type']
      resp['about']['chapters'] = result['chapters']
      resp['about']['volumes'] = result['volumes'] 
      resp['about']['score'] = result['score']
      resp['about']['start_date'] = (result['start_date'] or 'N/A')[:10]
      resp['about']['end_date'] = (result['end_date'] or 'N/A')[:10]
    results.append(resp)
  return results
