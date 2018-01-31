import sys

import requests
from bs4 import BeautifulSoup


def get_soup(link):
    print(f'SOUP => {link}')
    resp = requests.get(link)
    assert resp.status_code == 200
    return BeautifulSoup(resp.content, 'lxml')


def start():
    links = ['http://www.snepmusique.com/tops-semaine/top-singles-telecharges/',  # Top Singles Téléchargés
             'http://www.snepmusique.com/tops-semaine/top-singles-streaming/',  # Top Singles Streaming
             'http://www.snepmusique.com/tops-annuel/top-singles-megafusion-annuel/',  # Top Singles
             'http://www.snepmusique.com/tops-semaine/top-singles-megafusion/',  # Top Singles
             'http://www.snepmusique.com/tops-semaine/top-radios/']  # Classements Radios
    with open('music_french.txt', 'w') as w:
        for link in links:
            download(link, w)


def download(initial_url, fp_write):
    num_records = 0
    current_html = get_soup(initial_url)
    while True:
        info_list = current_html.find_all('div', {'class': 'infos'})

        for info in info_list:
            artist = str(info.find(None, {'class': 'artist'}).contents[0])
            title = str(info.find(None, {'class': 'title'}).contents[0])
            company = str(info.find(None, {'class': 'company'}).contents[0])
            print(f'{num_records} {artist} {title} {company}')
            fp_write.write(f'{artist} {title}\n')
            fp_write.flush()
            num_records += 1

        try:
            next_link = current_html.find('nav', {'class': 'table-top-navigation'}).find_all('a')[0].attrs['href']
            current_html = get_soup(next_link)
        except:
            print('Could not find next link. Aborting.')
            return


if __name__ == '__main__':
    assert len(sys.argv) == 3, 'Please provide the URL as argument and the output file.'
    download(sys.argv[1], open(sys.argv[2], 'w'))
