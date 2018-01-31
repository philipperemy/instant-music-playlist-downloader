import re
import string

import requests
from bs4 import BeautifulSoup

printable = set(string.printable)

music_names = open('music_2.txt', 'w')

URLS_PATTERNS = [
    'http://www.playlistresearch.com/{0}s/{1}latin.htm',
    'http://www.playlistresearch.com/{0}s/{1}rockhits.htm',
    'http://www.playlistresearch.com/{0}s/{1}dance.htm',
    'http://www.playlistresearch.com/{0}s/{1}pop.htm'
]

for major_year in range(1998, 2018):

    minor_year = 0
    if major_year < 2000:
        minor_year = 1990
    elif major_year < 2010:
        minor_year = 2000
    elif major_year < 2020:
        minor_year = 2010

    for url in URLS_PATTERNS:
        download_url = url.format(minor_year, major_year)
        print(download_url)
        response = requests.get(download_url)
        if response.status_code != 200:
            print('Not found. Skipping.')
            continue
        soup = BeautifulSoup(response.content, 'lxml')

        for text in soup(text=re.compile(r'.+ - .+')):
            music_name = text.strip()
            printable_music = ''.join(list(filter(lambda x: x in printable, music_name))).strip()
            if len(printable_music) != 0:
                music_names.write(printable_music)
                music_names.write('\n')
                music_names.flush()

music_names.close()
