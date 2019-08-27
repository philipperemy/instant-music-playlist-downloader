import sys

import eyed3
import os
from glob import glob
from tqdm import tqdm

assert len(sys.argv) == 2, 'Please specify the input as parameter.'

INPUT_DIR = sys.argv[1]  # Music dir from download.py script


def remove_text_inside_brackets(text, brackets="()[]"):
    count = [0] * (len(brackets) // 2)  # count open/close brackets
    saved_chars = []
    for character in text:
        for i, b in enumerate(brackets):
            if character == b:  # found bracket
                kind, is_close = divmod(i, 2)
                count[kind] += (-1) ** is_close  # `+1`: open, `-1`: close
                if count[kind] < 0:  # unbalanced bracket
                    count[kind] = 0  # keep it
                else:  # found bracket to remove
                    break
        else:  # character is not a [balanced] bracket
            if not any(count):  # outside brackets
                saved_chars.append(character)
    return ''.join(saved_chars)


if __name__ == '__main__':

    print(f'Input dir is {INPUT_DIR}')
    t = tqdm(glob(INPUT_DIR + '/**/*.mp3', recursive=True))
    for i, music in enumerate(t):
        music_name = os.path.splitext(os.path.basename(music))[0]
        possible_split_characters = ['-', '#']
        for split_char in possible_split_characters:
            tags = music_name.split('-')
            song_name = remove_text_inside_brackets(tags[-1]).title()
            artist = remove_text_inside_brackets('-'.join(tags[0:-1])).title()
            if artist is not None:
                break
        a = eyed3.load(music)
        a.tag.artist = artist.strip()
        a.tag.title = song_name.strip()
        a.tag.save()
