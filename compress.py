import os
import sys
from glob import glob

from pydub import AudioSegment
from tqdm import tqdm

assert len(sys.argv) == 2, 'Please specify the output as parameter.'

INPUT_DIR = sys.argv[1]  # Music dir from download.py script
OUTPUT_DIR = 'converted_music'
OUTPUT_BIT_RATE = '192k'
OUTPUT_FORMAT = 'mp3'

if __name__ == '__main__':

    print(f'Output dir is {OUTPUT_DIR}')
    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    musics = glob(INPUT_DIR + '/**/*.mp3', recursive=True)
    t = tqdm(musics)
    for i, music in enumerate(t):
        music_name = os.path.basename(music)
        output_filename = os.path.join(OUTPUT_DIR, music_name)
        t.set_description(music_name)
        if not os.path.isfile(output_filename):
            music_fp = AudioSegment.from_file(music)
            # music_fp = music_fp.set_frame_rate(16000)
            music_fp.export(output_filename,
                            format=OUTPUT_FORMAT,
                            bitrate=OUTPUT_BIT_RATE)
