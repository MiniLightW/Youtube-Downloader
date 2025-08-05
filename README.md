# YouTube Downloader

Download HD YouTube Videos

- Requires [ffmpeg](https://www.ffmpeg.org/download.html) to be installed on your computer
- Requires [pytubefix](https://korben.info/pytubefix-telechargement-videos-youtube-python.html) as python installed library
- Probably only works on Windows


This script will download & combine the highest quality audio & video files using pytube.


# Quick INSTALL (check URL data if doens't work anymore)
(procedure for windows only)
- 1- install ffmpeg
- open cmd in administrator and run this :
choco install ffmpeg
=> hen follow instruction with Yes or No...

- 2- install pytubefix
=> pytube is no loger functionnal, we use pytubefix now :
- open cmd in administrator and run this :
pip install pytubefix


# Quick run example : (replace XXX in example by valid data from real URL)
- py d:/DEV/Python/Youtube/Youtube-Downloader-main/youtube-download.py -t 'https://www.youtube.com/shorts/XXX'
- py d:/DEV/Python/Youtube/Youtube-Downloader-main/youtube-download.py -t 'https://www.youtube.com/watch?v=XXX'
