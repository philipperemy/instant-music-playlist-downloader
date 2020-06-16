python google_takeout.py --youtube_archive_dir /media/philippe/DATA/google-takeout/Takeout\ 2 --output_dir /media/philippe/DATA/google-takeout/mp3-takout --download_watch_history
python google_takeout.py --youtube_archive_dir /media/philippe/DATA/google-takeout/Takeout --output_dir /media/philippe/DATA/google-takeout/mp3-takout --download_watch_history

python filter_lengthy_songs.py --input_dir /media/philippe/DATA/google-takeout/mp3-takout --output_dir /media/philippe/DATA/google-takeout/mp3-takout-2 --force --min_minutes 0 --max_minutes 8 --dry_run > out.txt
