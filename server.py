import sys
sys.path.append("./13_cinemas")
from cinemas import fetch_afisha_page,parse_afisha_list,fetch_movie_info
from flask import Flask, render_template
from afisha import get_movie_info
from flask.ext.cache import Cache


app = Flask(__name__)
cache = Cache(app, config={'CACHE_TYPE' : 'simple'})


@cache.cached(timeout=50)
@app.route('/')
def films_list():
    afisha_page = fetch_afisha_page('http://www.afisha.ru/msk/schedule_cinema/')
    afisha_list = parse_afisha_list(afisha_page)

    movies = [get_movie_info(fetch_afisha_page('http:' + movie['url'])) for movie in afisha_list]


    return render_template('index.html',afisha_list=movies,count=len(movies))


if __name__ == "__main__":
    app.run()
