import sys
sys.path.append("./13_cinemas")
from cinemas import fetch_afisha_page,parse_afisha_list,fetch_movie_info
from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
def films_list():
    afisha_page = fetch_afisha_page('http://www.afisha.ru/msk/schedule_cinema/')
    afisha_list = parse_afisha_list(afisha_page)
    #test 23

    return render_template('films_list.html',afisha_list=afisha_list)


if __name__ == "__main__":
    app.run()
