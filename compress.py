import os
from glob import glob

from pydub import AudioSegment
from tqdm import tqdm

INPUT_DIR = 'MUSIC'  # Music dir from download.py script
OUTPUT_DIR = 'CONVERTED_MUSIC'
OUTPUT_BIT_RATE = '192k'
OUTPUT_FORMAT = 'mp3'

if __name__ == '__main__':

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    musics = glob(INPUT_DIR + '/**/*.*', recursive=True)
    for i, music in tqdm(enumerate(musics)):
        output_filename = os.path.join(OUTPUT_DIR, os.path.basename(music))
        if not os.path.isfile(output_filename):
            AudioSegment.from_file(music).export(output_filename,
                                                 format=OUTPUT_FORMAT,
                                                 bitrate=OUTPUT_BIT_RATE)
            print(f'{i}/{len(musics)} [DONE] {output_filename}')
        else:
            print(f'{i}/{len(musics)} [SKIPPING] {output_filename}')
