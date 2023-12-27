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
from pytube import YouTube
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

def download_youtube_video(url, output_path='.', output_filename=None):
    try:
        yt = YouTube(url)

        # Determine the output filename
        if output_filename is None:
            output_filename = sanitize_filename(f"{yt.title}.mp4")
        else:
            output_filename = ensure_mp4_extension(output_filename)

        # Get the highest resolution video-only stream
        video_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_video=True).order_by('resolution').desc().first()
        
        # Get the highest quality audio stream
        audio_stream = yt.streams.filter(adaptive=True, file_extension='mp4', only_audio=True).order_by('abr').desc().first()

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
    parser.add_argument("-t", "--target", help="URL of the YouTube video", required=True)
    parser.add_argument("-o", "--output", help="Optional output path and filename", required=False)
    args = parser.parse_args()

    # If the output argument is provided, split it into path and filename
    output_path, output_filename = '.', None
    if args.output:
        output_path, output_filename = os.path.split(args.output)
        if not output_path:
            output_path = '.'

    download_youtube_video(args.target, output_path, output_filename)

if __name__ == "__main__":
    main()
