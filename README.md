# Instantly download any list of songs :violin:

*Provide a TXT file where each line is a music and run a single script to download them all (mp3 from YouTube).*

<p align="center">
  <img src="https://www.winxdvd.com/resource/pics/youtube-to-mp3.png" width="100"><br/>
</p>


## Disclaimer

Downloading copyrighted material may be illegal in your country. Use at your own risk.

## Installation

Beforehand, please follow the instructions here: [https://github.com/yask123/Instant-Music-Downloader](https://github.com/yask123/Instant-Music-Downloader).

The command `instantmusic` should now work in your bash environment.

Additionally, run those commands (those are for python3):

```
git clone https://github.com/philipperemy/instant-music-playlist-downloader.git
cd instant-music-playlist-downloader
pip3 install -r requirements.txt
```

## Download a playlist

A playlist is a TXT file named `music.txt` at the root of the project. For example, this is a playlist:

```
instant-music-playlist-downloader % head music.txt
```

```
Coolio Gangstas Paradise
TLC Waterfalls
TLC Creep
Seal Kiss From A Rose
Boyz II Men On Bended Knee
Real McCoy Another Night
Mariah Carey Fantasy
Madonna Take A Bow
Monica Dont Take It Personal (Just One Of Dem Days)
Montell Jordan This Is How We Do It
```

I provide a script to download the [Billboard TOP 100 - Per Year](http://billboardtop100of.com/). Just run the following command
to build a playlist of roughly 2000 popular musics:

```
python3 music_names.py
```

## Download the musics

Now that we have our `music.txt` at the root of the project, all what you have to do is run:

```
python3 download.py
```

This script will download all the musics in the playlist in the current folder. To check the progression, simply run:

```
tail -f /tmp/mylog
```

## References

- [https://github.com/yask123/Instant-Music-Downloader](https://github.com/yask123/Instant-Music-Downloader)
