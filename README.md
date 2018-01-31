# Instantly Download any Playlist of Songs (IDPS) :violin:

*Provide a TXT file where each line is a music and run a single script to download them all (mp3 from YouTube).*


<p align="center">
  <b>*.txt > *.mp3</b>
</p>

<p align="center">
  <img src="https://www.winxdvd.com/resource/pics/youtube-to-mp3.png" width="100"><br/>
</p>


## Disclaimer

Downloading copyrighted material may be illegal in your country. Use at your own risk.

> Is it Legal to Convert YouTube Videos to MP3? The answer of this question depends upon your Geographical location. For example, in some countries, you can download and convert the videos to MP3 to listen them offline while others have very strict laws about this question. In United States, you can convert YouTube videos to MP3 and save them on your device to listen them but you cannot share these MP3 files with anyone else as you don’t own the copy rights of the video. Similarly, Canada has recently passed a new bill which states that you can make a single copy of the video from the YouTube and can convert it to the MP3 just for your own use. In Germany, you can download YouTube Videos or rip them to the MP3 songs to listen them offline on your computer or your cell phone.
From [https://imusic.aimersoft.com/download-music/is-youtube-to-mp3-legal.html](https://imusic.aimersoft.com/download-music/is-youtube-to-mp3-legal.html)

## Installation

Beforehand, please follow the instructions here: [https://github.com/yask123/Instant-Music-Downloader](https://github.com/yask123/Instant-Music-Downloader).

The command `instantmusic` should now work in your bash environment.

Additionally, run those commands (those are for python3):

```
git clone https://github.com/philipperemy/instant-music-playlist-downloader.git
cd instant-music-playlist-downloader
virtualenv -p python3 v
source v/bin/activate
python3.6 -m pip install -r requirements.txt
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
cd list_songs
python3 music_names_from_billboard.py
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
