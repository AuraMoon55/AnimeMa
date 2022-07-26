from flask.blueprints import Blueprint
from flask import render_template, request, flash
from jikanpy import Jikan

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
  for result in res:
    resp = {}
    resp['img'] = result['image_url']
    resp['title'] = result['title']
    resp['about'] = {}
    resp['description'] = result['synopsis']
  with resp['about'] as about:
    if cate == 'anime':
      about['airing'] = result['airing']
      about['type'] = result['type']
      about['episodes'] = result['episodes']
      about['rating'] = result['rated']
      about['score'] = result['score']
      about['start_date'] = result['start_date'][:10]
      about['end_date'] = (result['end_date'][:10] or 'N/A')
    else:
      about['publishing'] = result['publishing']
      about['type'] = result['type']
      about['chapters'] = result['chapters']
      about['volumes'] = result['volumes'] 
      about['score'] = result['score']
      about['start_date'] = result['start_date'][:10]
      about['end_date'] = (result['end_date'][:10] or 'N/A')
    results.append(resp)
    return results
