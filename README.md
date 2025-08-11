# YouTube Downloader

Download HD YouTube Videos

- Requires [ffmpeg](https://www.ffmpeg.org/download.html) to be installed on your computer
- Requires [pytubefix](https://github.com/JuanBindez/pytubefix) as python installed library
- Probably only works on Windows

This script will download & combine the highest quality audio & video files using pytubefix.
You can also download all vidéos from a playlist.
For downloading shorts videos use the PS script.

---

## Quick INSTALL (check URL data if doens't work anymore)
*procedure for windows only*

### 1- install ffmpeg
> Open cmd in administrator and run this :
```bash
 choco install ffmpeg
```
> then follow instruction with Yes or No...
### 2- install python library(ies) from requirements.txt file
> pytube is no loger functionnal, we use pytubefix now
> you can rin the first command or the next proposed as you wish
- open cmd in administrator and run this :
```bash
pip install -r requirements.txt
```
> instead of previous cmd you can only use this one to install pytubfix (the only package required for this project)
```bash
pip install pytubefix
```

---

## Quick run example
> ⚠️ Please replace XXX in example by valid data from real Youtube URL
### with cmd
```bash
py ./youtube-download.py -t https://www.youtube.com/shorts/XXX
py ./youtube-download.py -t https://www.youtube.com/watch?v=XXX

Exemples :
# video with best quality (default usage)
py ./youtube-download.py -t 'url'

# video with best quality
py ./youtube-download.py -t 'url' -v

# video with 360p quality
py ./youtube-download.py -t 'url' -v -q '360p'

# video with chosen quality inside the script
py ./youtube-download.py -t 'url' -v -q '?'

# video short
py ./youtube-download.py -t 'url' -v -s

# video short with 360p quality
py ./youtube-download.py -t 'url' -v -s -q '360p'

# video with chosen quality inside the script
py ./youtube-download.py -t 'url' -v -q '?'

# audio to mp3
py ./youtube-download.py -t 'url' -mp3
```
### for easier use :
> Use the PowerShell Script ! (update inside config first)

---

## For developpers

- [doc about pytubefix github](https://github.com/JuanBindez/pytubefix)
- [doc about pytubefix korben](https://korben.info/pytubefix-telechargement-videos-youtube-python.html)

---

### To download the highest resolution progressive stream without this script
```bash
pytubefix https://www.youtube.com/watch?v=XXX
```

---

## Force audio source original
> this will keep the original first audio recorded and not translated
```bash
pytubefix https://www.youtube.com/watch?v=XXX -af
```

## Use optimized script with only one user answer
### For normal video
> run this script : youtube-download_video_BestQuality.ps1
### For short video download
> run this script : youtube-download_video_shorts.ps1
### For short audio download
> run this script : youtube-download_audio.ps1
