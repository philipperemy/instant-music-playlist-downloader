from time import sleep

import pexpect
from pexpect.exceptions import ExceptionPexpect


def get_music(name='Linkin Park papercut'):
    child = pexpect.spawn('instantmusic')
    child.logfile = open('/tmp/mylog', 'wb')
    child.expect('Enter*')
    child.sendline(name)
    child.expect('Pick one*')
    child.sendline('0')
    child.expect('Download*')
    child.sendline('y')
    child.expect(['Fixed*', 'couldnt get album art*'])


def run():
    current_index = int(open('persistence.txt', 'r').read())
    musics = open('music.txt').readlines()
    for i, music in enumerate(musics):

        if i < current_index:
            print('already fetched.')
            continue

        num_attempts = 0
        while num_attempts < 3:
            try:
                printable_music = music.strip()
                print('Downloading {0}'.format(printable_music))
                get_music(printable_music)
                break
            except ExceptionPexpect:  # also check pexpect.exceptions.TIMEOUT: Timeout exceeded.
                num_attempts += 1
                print('Going to sleep. We received an exception from pexpect. Attempts = {0}'.format(num_attempts))
                sleep(10)
        current_index += 1
        open('persistence.txt', 'w').write(str(current_index))


if __name__ == '__main__':
    # get_music('Montell Jordan This Is How We Do It')
    run()
