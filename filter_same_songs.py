import os
import shutil
from argparse import ArgumentParser
from glob import glob

from eyed3 import id3


def get_script_arguments():
    args = ArgumentParser()
    args.add_argument('--input_dir', type=os.path.expanduser, required=True, help='MP3 directory.')
    args.add_argument('--output_dir', type=os.path.expanduser, required=True, help='Results directory.')
    args.add_argument('--force', action='store_true', help='Delete results.')
    args.add_argument('--dry_run', action='store_true', help='No copy.')
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
    musics = {}
    keep_count = 0
    delete_count = 0
    for input_filename in glob(args.input_dir + '/**/*.mp3', recursive=True):
        music_name = os.path.basename(input_filename)
        output_filename = os.path.join(args.output_dir, music_name)
        # just to avoid this warning: Invalid date: 20091201, we add version.
        tag = id3.Tag()
        tag.parse(input_filename)
        key = tag.artist + ' - ' + tag.title
        if key not in musics:
            musics[key] = 1.0
            print(f'KEEP {input_filename}.')
            keep_count += 1
            if not args.dry_run:
                shutil.copy2(input_filename, output_filename)
        else:
            print(f'DELETE {input_filename}.')
            delete_count += 1
    print(keep_count)
    print(delete_count)
    print('Completed.')


if __name__ == '__main__':
    main()
