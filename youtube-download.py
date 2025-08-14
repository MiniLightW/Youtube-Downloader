#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Download audio or video from YouTube
Audio is converted to mp3 format
You can choose quality of extraction
You can use playlists
"""

import argparse
import os
import re
from datetime import datetime
from pytubefix import YouTube
from pytubefix import Playlist
from pytubefix.cli import on_progress
from utils import get_from_keyboard
from utils import sanitize_filename


def ensure_mp4_extension(filename):
    # Add '.mp4' extension if not present
    if not filename.lower().endswith('.mp4'):
        filename += '.mp4'
    return filename


def select_value(valid_list):
    x = "-"
    while x not in valid_list:
        x = get_from_keyboard(f"Please choose a value from the list (ex: write {valid_list[0]}) :")
        print(type(x))
    return x


def streamfilter (streams, type, res):
    # res specific : short

    # Filter streams based on type and resolution
    if type == 'video':

        # extract available resolution
        available_video_res = get_available_video_resolutions(streams)

        if res == 'high':
            stream = streams.filter(adaptive=True, only_video=True, file_extension='mp4').order_by('resolution').desc().first()
        elif res in available_video_res:
            stream = streams.filter(only_video=True, file_extension='mp4', resolution=res).first()
        elif res == '?':
            res = select_value(available_video_res)
            stream = streams.filter(only_video=True, file_extension='mp4', resolution=res).first()
        elif res == 'low':
            stream = streams.filter(only_video=True, file_extension='mp4').order_by('resolution').asc().first()

    elif type == 'audio':

        # extract available bitrate
        available_audio_abr = get_available_audio_abr(streams)

        if res == 'high':
            stream = streams.filter(only_audio=True).order_by('abr').desc().first()
        elif res in available_audio_abr:
            stream = streams.filter(only_audio=True, abr=res).first()
        elif res == 'short':
            stream = streams.order_by('itag').asc().first()
        elif res == '?':
            res = select_value(available_audio_abr)
            stream = streams.filter(only_audio=True, abr=res).first()
        else: # res = low
            stream = streams.filter(only_audio=True).order_by('abr').desc().last()
            #audio_stream = streams.get_by_itag(audio_tag)

    # error config or not found
    else:
        print("ERROR: No valid type or resolution found from function streamfilter()")
        exit(1)

    if not stream:
        raise ValueError(f"No stream found with type '{type}' and resolution '{res}'")
    
    return stream


def convert_to_mp3(input_file, output_file):
    # convert audio .m4a to .mp3
    print("Converting file to mp3...")
    os.system(f'ffmpeg -i "{input_file}" -c:v copy -c:a libmp3lame -q:a 4 "{output_file}"')
    os.remove(input_file)
    print(f"Converted to MP3 and saved as '{output_file}'")


def get_available_video_resolutions(streams):
    # return list of available video resolutions
    avr = []
    for x in streams.filter(only_video=True, file_extension='mp4'):
        if x.resolution and x.resolution not in avr:
            avr.append(x.resolution)
    print("Available resolutions:")
    for res in avr:
        print(f"- {res}")
    return avr


def get_available_audio_abr(streams):
    # return list of available audio abr
    aaa = []
    for x in streams.filter(only_audio=True):
        print(x)
        if x.abr and x.abr not in aaa:
            aaa.append(x.abr)
    print("Available audio bitrate:")
    for abr in aaa:
        print(f"- {abr}")
    return aaa


def get_source_yt(url):
    # Get the YouTube object from the URL
    try:
        yt = YouTube(url, on_progress_callback=on_progress)
        return yt
    except Exception as e:
        print(f"Error fetching YouTube object: {e}")
        exit(1)


def download_youtube_audio(url, output_dir, output_filename=None, quality=None):

    yt = get_source_yt(url)
    
    try:
        # audio only stream
        if quality:
            audio_stream = streamfilter(yt.streams, 'audio', quality)
        else:
            audio_stream = streamfilter(yt.streams, 'audio', 'high')

        # Determine the output filename
        output_filename_init = sanitize_filename(yt.title) + ".m4a"
        if output_filename is None:
            output_filename_final = sanitize_filename(yt.title) + ".mp3"
        else:
            output_filename_final = sanitize_filename(output_filename) + ".mp3"

        # Download video and audio streams
        print(f"[Downloading audio: {yt.title} > in > {output_filename_init}]")
        try:
            audio_stream.download(".", filename=output_filename_init)
        except Exception as e:
            print(f"Error downloading audio stream: {e}")
            exit(1)

        # convert to mp3
        convert_to_mp3(os.path.join(output_dir, output_filename_init),os.path.join(output_dir,output_filename_final))

    except Exception as e:
        print(f"Error: {e}")


def download_youtube_video(url, output_dir='.', output_filename=None, quality=None, short=None):

    yt = get_source_yt(url)
    try:
        # Determine the output filename
        if output_filename is None:
            output_filename = sanitize_filename(f"{yt.title}") + ".mp4"
            print("1" + output_filename)
        else:
            output_filename = ensure_mp4_extension(output_filename)
            print("2" + output_filename)

        # VIDEO : Get the highest resolution video-only stream
        if quality:
            video_stream = streamfilter(yt.streams, 'video', quality)
        else:
            video_stream = streamfilter(yt.streams, 'video', 'high')
        print (f"[{video_stream}]")

        # AUDIO : Get the highest quality audio stream
        if short:
            audio_stream = streamfilter(yt.streams, 'audio', 'short')
        else:
            audio_stream = streamfilter(yt.streams, 'audio', 'high')
        if not audio_stream:
            raise ValueError(f"No audio stream found")
        print (f"[{audio_stream}]")
        
        # Download video and audio streams
        print(f"Downloading video: {yt.title}")
        video_filename = 'video.mp4'
        audio_filename = 'audio.mp4'
        video_stream.download(output_dir, filename=video_filename)
        audio_stream.download(output_dir, filename=audio_filename)

        # Combine video and audio using ffmpeg
        full_output_path = os.path.join(output_dir, output_filename)
        os.system(f'ffmpeg -i "{os.path.join(output_dir, video_filename)}" -i "{os.path.join(output_dir, audio_filename)}" -c:v copy -c:a aac "{full_output_path}"')

        # Remove temporary video and audio files
        os.remove(os.path.join(output_dir, video_filename))
        os.remove(os.path.join(output_dir, audio_filename))

        print(f"Downloaded and merged into '{full_output_path}'")

    except Exception as e:
        print(f"Error: {e}")


def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos and playlist, convert video audio to mp3")
    parser.add_argument("-t"  , "--target" , help="URL of the YouTube video", required=True)
    parser.add_argument("-o"  , "--output" , help="Optional output path", required=False)
    parser.add_argument("-mp3", "--toMp3"  , help="Get audio with mp3", action='store_true')
    parser.add_argument("-v"  , "--video"  , help="Get video", action='store_true')
    parser.add_argument("-s"  , "--short"  , help="Use it for getting specific short video (sound difference)", action='store_true')
    parser.add_argument("-q"  , "--quality", help="Resolution of the video, use '?' value for choose among list yourself", required=False)

    args = parser.parse_args()

    # If the output argument is provided, split it into path and filename
    output_dir, output_filename = '.', None
    if args.output:
        output_dir, output_filename = os.path.split(args.output)
    # directory name for current run
    d = datetime.now()
    time = d.strftime("%d%m%Y_%H%M%S_%f")
    output_dir = os.path.join(output_dir, time)

    if not args.video and not args.toMp3:
        args.video = True

    # use playlist if the URL contains a playlist identifier
    motif = r"\&list="
    res = re.search(motif, args.target)
    if res:
        print("/!\\ This is a playlist URL")
        print("All following videos will be downloaded:")
        pl = Playlist(args.target)
        for video in pl.videos:
            print(video.title + " " + video.watch_url)

        x = ""
        while x != "y":
            x = get_from_keyboard("Write 'y' to continue... or Ctrl+C to abbort:")

        for video in pl.videos:
            print(video.title + " > " + video.watch_url)
            if args.toMp3:
                download_youtube_audio(video.watch_url, output_dir, video.title, args.quality)
            if args.video:
                download_youtube_video(video.watch_url, output_dir, video.title, args.quality, args.short)
    else:
        if args.toMp3:
            download_youtube_audio(args.target, output_dir, output_filename, args.quality)
        if args.video:
            download_youtube_video(args.target, output_dir, output_filename, args.quality, args.short)


if __name__ == "__main__":
    print("### RUNNING : " + os.path.basename(__file__) + " ###")
    main()


'''
# execution via un programme externe
import subprocess
# Appelle un autre script Python (par exemple, text_translator.py)
result = subprocess.run(
    ["python", "text_translator.py", "-t", "fichier.txt", "-l", "fr"],
    capture_output=True, text=True
)
print("Sortie du script :", result.stdout)

# via appel du main (attention à la gestion des arguments...)
import text_translator
text_translator.main()


traitement résumé :
https://hackernoon.com/lang/fr/construire-un-analyseur-de-documents-avec-chatgpt-google-cloud-et-python
'''
