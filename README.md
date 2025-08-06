# YouTube Downloader

Download HD YouTube Videos

- Requires [ffmpeg](https://www.ffmpeg.org/download.html) to be installed on your computer
- Requires [pytubefix](https://github.com/JuanBindez/pytubefix) as python installed library
- Probably only works on Windows

This script will download & combine the highest quality audio & video files using pytubefix.

# I / Quick INSTALL (check URL data if doens't work anymore)
*procedure for windows only*

## 1- install ffmpeg
Open cmd in administrator and run this :
```bash
 choco install ffmpeg
```
> then follow instruction with Yes or No...
## 2- install pytubefix
> pytube is no loger functionnal, we use pytubefix now :
- open cmd in administrator and run this :
```bash
pip install pytubefix
```


# II / Quick run example
> ⚠️ Please replace XXX in example by valid data from real Youtube URL
## for only one video
```bash
py ./youtube-download.py -t https://www.youtube.com/shorts/XXX
py ./youtube-download.py -t https://www.youtube.com/watch?v=XXX
```
## for a full playlist :
> ⚠️ String ' is required
```bash
py ./youtube-download.py -t 'https://www.youtube.com/watch?v=XXX&list=XXX'
```


# III / For developpers
- [additionnal doc about pytubefix](https://korben.info/pytubefix-telechargement-videos-youtube-python.html)


# IV / audio source forced mode
# sometime almost all audio source are not the original but a translated version
# only the progressive file has the good one but it's not considered as the "highest" quality
# for fix this rare problem you have to use this tip
## To download the highest resolution progressive stream:
```bash
pytubefix https://www.youtube.com/watch?v=XXX
```
> This give you the good audio but not the highest video
> Now you have to find the tag if this source
```bash
pytubefix https://www.youtube.com/watch?v=XXX --list
```
> Keep the number value in "<Stream: itag="TAGID" mime_type...>" from the
> ⚠️ It's not a problem to use a video source and not an audio source only. Just keep audio you need
> Then run the download with this option :
python ...\youtube-download.py -t  https://www.youtube.com/watch?v=XXX -at TAGID

# V / force audio source original
```bash
pytubefix https://www.youtube.com/watch?v=XXX -af
```
> will keep the original first audio recorded