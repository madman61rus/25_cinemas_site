import sys
sys.path.append("./13_cinemas")
from cinemas import fetch_afisha_page,parse_afisha_list,fetch_movie_info
from flask import Flask, render_template, session,jsonify
from afisha import get_movie_info
from flask_cache import Cache


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE' : 'simple'})
app.secret_key='Avewf213sdf;lkjoim'


@cache.cached(timeout=50)
@app.route('/')
def films_list():
    afisha_page = fetch_afisha_page('http://www.afisha.ru/msk/schedule_cinema/')
    afisha_list = parse_afisha_list(afisha_page)
    session['afisha_list'] = afisha_list

   # movies = [get_movie_info(fetch_afisha_page('http:' + movie['url'])) for movie in afisha_list]


    return render_template('index.html')

@app.route('/get-info/<int:number_from>', methods=['POST'])
def get_info(number_from = 1):
    movies_info = []
    for number_movie in range(number_from,number_from + 3):
        movies_info.append(get_movie_info(fetch_afisha_page('http:' + session['afisha_list'][number_from]['url'])))


    return jsonify (movies_info = movies_info)

@app.route('/get-count',methods=['POST'])
def get_count():
    return jsonify (count = len(session['afisha_list']))

if __name__ == "__main__":
    app.run()
