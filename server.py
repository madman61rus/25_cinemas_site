import sys
sys.path.append("./13_cinemas")
from cinemas import fetch_afisha_page,parse_afisha_list,fetch_movie_info
from flask import Flask, render_template
from afisha import get_movie_info


app = Flask(__name__)

@app.route('/')
def films_list():
    afisha_page = fetch_afisha_page('http://www.afisha.ru/msk/schedule_cinema/')
    afisha_list = parse_afisha_list(afisha_page)

    movies = [get_movie_info(fetch_afisha_page('http:' + movie['url'])) for movie in afisha_list]

    return render_template('films_list.html',afisha_list=movies)


if __name__ == "__main__":
    app.run()
