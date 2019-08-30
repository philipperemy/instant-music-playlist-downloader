import os
import shutil
from argparse import ArgumentParser
from glob import glob

from eyed3 import mp3
from eyed3.id3 import ID3_V1_0
from tqdm import tqdm


def get_script_arguments():
    args = ArgumentParser()
    args.add_argument('--input_dir', type=os.path.expanduser, required=True, help='MP3 directory.')
    args.add_argument('--output_dir', type=os.path.expanduser, required=True, help='Results directory.')
    args.add_argument('--force', action='store_true', help='Delete results.')
    args.add_argument('--min_minutes', type=float, default=0.0, help='Lower cutoff threshold.')
    args.add_argument('--max_minutes', type=float, required=True, help='Upper cutoff threshold.')
    return args.parse_args()


def main():
    args = get_script_arguments()
    if not os.path.exists(args.output_dir):
        os.makedirs(args.output_dir)
    elif args.force:
        shutil.rmtree(args.output_dir)
        os.makedirs(args.output_dir)
    else:
        print(f'{args.output_dir} already exists. Delete it first.')
        exit(1)

    with tqdm(glob(args.input_dir + '/**/*.mp3', recursive=True)) as bar:
        for input_filename in bar:
            music_name = os.path.basename(input_filename)
            bar.set_description(music_name)
            output_filename = os.path.join(args.output_dir, music_name)
            # just to avoid this warning: Invalid date: 20091201, we add version.
            f = mp3.Mp3AudioFile(input_filename, version=ID3_V1_0)
            if args.min_minutes * 60 < f.info.time_secs < args.max_minutes * 60:
                shutil.copy2(input_filename, output_filename)
    print('Completed.')


if __name__ == '__main__':
    main()
