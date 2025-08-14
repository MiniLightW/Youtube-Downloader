# pip install -U deep-translator
import re
import os
import argparse
import configparser
from datetime import datetime
from pytubefix import YouTube
from deep_translator import GoogleTranslator
from utils import sanitize_filename
from utils import get_from_keyboard
from utils_translate import translateText

# this script transforms SRT subtitles into plain text with readable formatting
# it removes all timestamps and speaker labels
# it also removes all empty lines
# it also adds a newline after each point
# it also allow a GoogleTranslator translation with the required max parameter for each pass

# doc
# https://pytubefix.readthedocs.io/en/latest/user/captions.html


def formatSRT2TXT(content):
    # format srt format to simple txt without timing ans multi empty lines

    # delete number
    content = re.sub(r"^\d+\n", "", content, flags=re.MULTILINE)
    # delete timers
    content = re.sub(r"\d{2}:\d{2}:\d{2}.\d{3}.*\n", "", content)
    # delete empty multilines
    content = re.sub(r"\n{2,}", "", content)
    # delete point followed by space
    content = re.sub(r"\. ", ".\n", content)
    return content.strip()


def getSubtitleFromYt(output_dir, yt, translate=False):
    # download subtitle from a youtube URL
    # if true make a translation
    title = sanitize_filename(yt.title)
    print("Title: " + title)

    if not yt.captions:
        print("No subtitles found.")
        return
    nb = 0
    for caption in yt.captions:
        nb += 1
    print("Number of Subtitles: " + str(nb))
    
    for caption in yt.captions:
        print("-Subtitle : " + caption.code + " <> " + caption.name)
        
        #srt_file = caption.code + ".srt"
        #x = caption.save_captions(srt_file)
        print("output dir: " + output_dir)
        x = caption.download(caption.code, output_path=output_dir) #return file_path
        name_ext = os.path.basename(x)
        name     = os.path.splitext(name_ext)[0] # remove extension
        #print(x)
        #print(dir)
        print(name)     # only filename
        #print(name_ext) # only filename with extension

        # get the content
        with open(x, "r", encoding="utf-8") as f:
            file_content = f.read()
        f.close()
        formatted_txt_content = formatSRT2TXT(file_content)

        # write new file
        formated_txt_file_name = title + "_" + name + ".txt"
        formated_txt_file_name_path = os.path.join(output_dir, formated_txt_file_name)
        with open(formated_txt_file_name_path, 'w') as f:
            f.write(formatted_txt_content)
        f.close()
        print("--Formatted subtitle saved in: " + formated_txt_file_name_path)
        # remove old file
        os.remove(x)

        # translate
        if translate is not None:
            translateText(formated_txt_file_name_path, translate[0], translate[1])


def main():
    # Read configuration
    config = configparser.ConfigParser()
    script_dir  = os.path.dirname(os.path.abspath(__file__))
    config_path = os.path.join(script_dir, 'config.ini')
    config.read(config_path)

    max_length = int(config['translation']['max_length'])
    target_language = config['translation']['target_language']

    # Set up argument parser
    parser = argparse.ArgumentParser(description="Download YouTube videos and playlist, convert video audio to mp3")
    parser.add_argument("-t", "--target"  , help="URL of the YouTube video"       , required=True)
    parser.add_argument("-l", "--language", help="Target language for translation", required=False)
    parser.add_argument("-o", "--output"  , help="Optional output path"           , required=False)

    args = parser.parse_args()

    # If the output argument is provided, split it into path and filename
    output_dir, output_filename = '.', None
    if args.output:
        output_dir, output_filename = os.path.split(args.output)
    # directory name for current run
    d = datetime.now()
    time = d.strftime("%d%m%Y_%H%M%S_%f")
    output_dir = os.path.join(output_dir, time)

    translate = True
    if not args.language:
        translate = False
    elif args.language != '?':
        print("output target language asked: " + args.language)
        target_language = args.language
    else:
        x = ""
        while x not in GoogleTranslator().get_supported_languages(as_dict=True).values():
            print("Unrecognized language. Please choose from the following list:")
            print(GoogleTranslator().get_supported_languages(as_dict=True))
            x = get_from_keyboard("Enter target language code (write full name or short name): ")
        target_language = x 

    if translate:
        getSubtitleFromYt(output_dir,YouTube(args.target),[target_language, max_length])
    else:
        getSubtitleFromYt(output_dir,YouTube(args.target), None)


if __name__ == "__main__":
    print("### RUNNING : " + os.path.basename(__file__) + " ###")
    main()
