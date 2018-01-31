#!/usr/bin/env bash

rm -rf french_song_listing
mkdir french_song_listing

for endPoint in "top-singles-streaming" "top-singles-telecharges" "top-singles-megafusion-annuel" "top-singles-megafusion" "top-radios"; do
  python3 music_names_from_french_ranking.py "http://www.snepmusique.com/tops-semaine/${endPoint}/" french_song_listing/${endPoint}.txt
done