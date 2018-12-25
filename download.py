import sys
from time import sleep

import logging
import os
import pexpect
import shutil
from glob import glob
from pexpect.exceptions import ExceptionPexpect
from tqdm import tqdm

logger = logging.getLogger(__name__)

PERSISTENCE_FILENAME = 'persistence.txt'

KEYWORDS_TO_FILTER_OUT = ['album complet', 'compil', 'full album', 'compilation', 'full ep', 'full']


def get_music(name='Linkin Park papercut'):
    child = pexpect.spawn('instantmusic')
    child.logfile = open('/tmp/mylog', 'wb')
    child.expect('Enter*')
    child.sendline(name)
    child.expect('Pick one*')
    child.sendline('0')
    child.expect('Download*')
    child.sendline('y')
    child.expect(['Fixed*', 'couldnt get album art*'], timeout=240)


def remove_mp3():
    for f in glob('*.mp3'):
        os.remove(f)
    for f in glob('*.webm'):
        os.remove(f)


def run(song_filename, output_folder):
    if not os.path.isfile(PERSISTENCE_FILENAME):
        with open(PERSISTENCE_FILENAME, 'w') as w:
            w.write('0')

    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    remove_mp3()

    current_index = int(open(PERSISTENCE_FILENAME, 'r').read())
    musics = open(song_filename, 'rb').read().decode('utf8').strip().split('\n')
    bar = tqdm(musics)
    for i, music in enumerate(bar):

        if i < current_index:
            bar.set_description('Already fetched.')
            continue

        num_attempts = 0
        while num_attempts < 3:
            try:
                printable_music = music.strip()
                bar.set_description(f'Downloading <{printable_music.title()}>')
                get_music(printable_music)

                # logger.info(glob('*.mp3'))
                for mp3_music in glob('*.mp3'):
                    for keyword_to_filter in KEYWORDS_TO_FILTER_OUT:
                        if keyword_to_filter.lower() in mp3_music.lower():
                            logger.info('Music filtered {}.'.format(mp3_music))
                            os.remove(mp3_music)
                            continue
                    try:
                        shutil.move(mp3_music, output_folder + '/')
                    except FileNotFoundError:
                        logger.exception('')
                        remove_mp3()
                        logger.info(f'Could not find {mp3_music}. Skip this one.')
                        break
                    except shutil.Error:
                        logger.exception('')
                        remove_mp3()
                        break
                break
            except ExceptionPexpect:  # also check pexpect.exceptions.TIMEOUT: Timeout exceeded.
                num_attempts += 1
                logger.info('Going to sleep. We received an exception from pexpect. '
                            'Attempts = {0}'.format(num_attempts))
                sleep(10)
        current_index += 1
        open(PERSISTENCE_FILENAME, 'w').write(str(current_index))
    bar.close()


if __name__ == '__main__':
    if len(sys.argv) != 3:
        print('Specify a list of songs as txt file and the output folder for the songs.')
        print('Example: python download.py list_songs/french_song_listing/top-radios-unique.txt output_music')
        exit(1)
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    run(sys.argv[1], sys.argv[2])
