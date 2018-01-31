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
    y_list = list(range(2001, 2019))
    w_list = list(range(1, 53))
    print(y_list)
    print(w_list)
    for y in y_list:
        for w in w_list:
            current_html = get_soup(initial_url + f'?ye={y}&we={w}')
            info_list = current_html.find_all('div', {'class': 'infos'})

            for info in info_list:
                try:
                    artist = str(info.find(None, {'class': 'artist'}).contents[0])
                    title = str(info.find(None, {'class': 'title'}).contents[0])
                    # company = str(info.find(None, {'class': 'company'}).contents[0])
                    # print(f'{num_records} {artist} {title} {company}')
                    fp_write.write(f'{artist} {title}\n')
                    fp_write.flush()
                    num_records += 1
                except:
                    print(f'Invalid record {info}. Skipping.')


if __name__ == '__main__':
    assert len(sys.argv) == 3, 'Please provide the URL as argument and the output file.'
    download(sys.argv[1], open(sys.argv[2], 'w'))
