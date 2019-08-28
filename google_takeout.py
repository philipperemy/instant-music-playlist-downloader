# takeout.google.com.
# Deselect All.
# Select Youtube.
# Press on "multiple formats" > History > "JSON" and press "OK".
# Press on "Next Step".
# You will receive a .ZIP on your email address.
# Extract this .ZIP.
# This extracted directory is the input to this script.
import json
import os
from argparse import ArgumentParser
from collections import Counter
from glob import glob
from os.path import join
from time import time


def get_script_arguments():
    args = ArgumentParser()
    args.add_argument('--youtube_archive_dir', type=os.path.expanduser, required=True,
                      help='https://takeout.google.com')
    args.add_argument('--output_dir', type=os.path.expanduser, required=True)
    args.add_argument('--download_watch_history', action='store_true', help='Youtube search history')
    return args.parse_args()


def download_music(video_id: str, output_dir='', is_quiet=True):
    # https://github.com/yask123/Instant-Music-Downloader/blob/master/instantmusic-0.1/bin/instantmusic#L131
    # video_link = /watch\?v\=nPA2czkOsFE"
    command_tokens = [
        f'youtube-dl',
        f'--extract-audio',
        f'--audio-format mp3',
        f'--audio-quality 0',
        f'--output \'{output_dir}/%(title)s.%(ext)s\'',
        f'https://www.youtube.com' + '/watch?v=' + video_id]
    if is_quiet:
        command_tokens.insert(1, '-q')
    command = ' '.join(command_tokens)
    os.system(command)


def check_if_music_already_exists(title: str, output_dir=''):
    return os.path.exists(join(output_dir, title) + '.mp3')


def download_music_wrapper(i, title, video_id, output_dir):
    print(i, title.ljust(100), video_id, end='')
    start = time()
    if not check_if_music_already_exists(title, output_dir):
        download_music(video_id, output_dir)
        print('... DOWNLOADED    '.ljust(30), end=' ')
    else:
        print('... ALREADY EXISTS'.ljust(30), end=' ')
    print(f'{time() - start:.1f} seconds')


def download_playlist(playlist_filename: str, output_dir: str):
    with open(playlist_filename, 'r', encoding='utf8') as r:
        playlist = json.load(r)
    for video in playlist:
        title = video['snippet']['title'].strip()
        video_id = video['snippet']['resourceId']['videoId'].strip()
        download_music_wrapper(0, title, video_id, output_dir)


def download_history(history_filename: str, output_dir: str):
    with open(history_filename, 'r', encoding='utf8') as r:
        history = json.load(r)
    counter = Counter([t['titleUrl'] for t in history if 'titleUrl' in t])
    # select videos with at least 2 personal views.
    relevant_urls = [x for x, count in dict(counter).items() if count >= 2]
    # only select unique videos in the history.
    picks = {}
    for record in history:
        if 'titleUrl' in record \
                and record['titleUrl'] in relevant_urls \
                and record['titleUrl'] not in picks:
            picks[record['titleUrl']] = record
    sub_history = list(picks.values())
    for i, record in enumerate(sub_history):
        title = record['title'].strip()
        if 'titleUrl' in record:
            video_id = record['titleUrl'].split('=')[-1]
            if title.startswith('Watched '):
                title = title.replace('Watched ', '')
            download_music_wrapper(i, title, video_id, output_dir)
        else:
            pass  # 'Watched a video that has been removed'


def main():
    args = get_script_arguments()
    assert os.path.exists(args.youtube_archive_dir)
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    youtube_dir = join(args.youtube_archive_dir, 'YouTube')
    if args.download_watch_history:
        search_history = join(youtube_dir, 'history', 'search-history.json')
        watch_history = join(youtube_dir, 'history', 'watch-history.json')
        assert os.path.isfile(search_history)
        assert os.path.isfile(watch_history)
        download_history(watch_history, args.output_dir)
    playlists = glob(join(youtube_dir, 'playlists') + '/*.json')
    assert len(playlists) > 0
    for playlist in playlists:
        print('-' * 80)
        playlist_name = os.path.splitext(os.path.basename(playlist))[0]
        print(f'PLAYLIST: ', playlist_name)
        download_playlist(playlist, args.output_dir)


if __name__ == '__main__':
    main()
