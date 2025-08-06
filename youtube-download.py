"""
YouTube Video Downloader Script
- Downloads the highest quality video and audio streams separately from a given YouTube video URL.
- Merges the downloaded video and audio streams into a single MP4 file.
- Allows specifying an output path and filename using the -o/--output option.
- Automatically adds the '.mp4' extension if it's not specified in the output filename.
- Sanitizes filenames from trouble-causing special characters.
- Uses the pytube library for downloading and ffmpeg for merging streams.
"""

import argparse
from pytubefix import YouTube
from pytubefix.cli import on_progress
from pytubefix import Playlist
import os
import re

def sanitize_filename(filename):
    # Replace problematic characters with underscores
    return re.sub(r'[\\/*?:"<>|]', '_', filename)

def ensure_mp4_extension(filename):
    # Add '.mp4' extension if not present
    if not filename.lower().endswith('.mp4'):
        filename += '.mp4'
    return filename

def download_youtube_video(url, output_path='.', output_filename=None, audio_tag=None):
    try:
        yt = YouTube(url, on_progress_callback=on_progress)

        # Determine the output filename
        if output_filename is None:
            output_filename = sanitize_filename(f"{yt.title}.mp4")
        else:
            output_filename = ensure_mp4_extension(output_filename)

        '''
        # show all data
        for x in yt.streams:
            print(f"{x.itag} {x.mime_type} {x.type} {x.resolution} {x.abr} {x.fps}")
            print(f"Video: {x.title} - {x.resolution} - {x.abr} - {x.fps}fps")
        exit()
        '''

        # Get the highest resolution video-only stream
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        
        # Get the highest quality audio stream
        if not audio_tag:
            audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()
        else:
            audio_stream = yt.streams.get_by_itag(audio_tag)
            if not audio_stream:
                raise ValueError(f"No audio stream found with tag '{audio_tag}'")

        # Download video and audio streams
        print(f"Downloading video: {yt.title}")
        video_filename = 'video.mp4'
        audio_filename = 'audio.mp4'
        video_stream.download(output_path, filename=video_filename)
        audio_stream.download(output_path, filename=audio_filename)

        # Combine video and audio using ffmpeg
        full_output_path = os.path.join(output_path, output_filename)
        os.system(f'ffmpeg -i "{os.path.join(output_path, video_filename)}" -i "{os.path.join(output_path, audio_filename)}" -c:v copy -c:a aac "{full_output_path}"')

        # Remove temporary video and audio files
        os.remove(os.path.join(output_path, video_filename))
        os.remove(os.path.join(output_path, audio_filename))

        print(f"Downloaded and merged into '{full_output_path}'")

    except Exception as e:
        print(f"Error: {e}")

def main():
    parser = argparse.ArgumentParser(description="Download YouTube videos in the highest quality")
    parser.add_argument("-t",  "--target",   help="URL of the YouTube video", required=True)
    parser.add_argument("-at", "--audiotag", help="Forced audio tag (no playlist)", required=False)
    parser.add_argument("-o",  "--output",   help="Optional output path and filename", required=False)
    args = parser.parse_args()

    # If the output argument is provided, split it into path and filename
    output_path, output_filename = '.', None
    if args.output:
        output_path, output_filename = os.path.split(args.output)
        if not output_path:
            output_path = '.'

    if args.audiotag:
        print(f"Using forced audio tag: {args.audiotag}")
        pytube_list_audio_tag = args.audiotag
    else:
        pytube_list_audio_tag = None

    motif = r"\&list="
    res = re.search(motif, args.target)
    if res:
        print("This is a playlist URL, please use the playlist downloader instead.")
        pl = Playlist(args.target)
        print("All following videos will be downloaded:")
        for video in pl.videos:
            print(video.title + " " + video.watch_url)
        input("Press Enter to continue... or Ctrl+C to abbort.")
        for video in pl.videos:
            print(video.title + " " + video.watch_url)
            """
            ys = video.streams.get_audio_only()
            ys.download()
            """
            download_youtube_video(video.watch_url, output_path, output_filename)
    else:
        download_youtube_video(args.target, output_path, output_filename, pytube_list_audio_tag)

if __name__ == "__main__":
    main()
