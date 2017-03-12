import sys
sys.path.append("./13_cinemas")
from bs4 import BeautifulSoup

def get_movie_info(raw_html):
    soup = BeautifulSoup(raw_html, 'html.parser')

    orig_name_class = soup.findAll('p', {'class': 'orig-name'})
    description = soup.findAll('p', {'id' : 'ctl00_CenterPlaceHolder_ucMainPageContent_pDescription'})

    return {
        'title' : soup.find('h1').text.strip(),
        'orig_name' : orig_name_class[0].get_text().strip()
                        if orig_name_class else '',
        'creation' : soup.find('span', {'class': 'creation'}).text,
        'genre' : [genre.text.strip() for genre in soup.findAll('div',{'class': 'b-tags'})],
        'director' : soup.find('div',{'class' : 'm-margin-btm'}),
        'desription' : description[0].get_text() if description else '',

    }