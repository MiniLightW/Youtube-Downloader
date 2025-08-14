#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Text Translator with Google Translate API

import argparse
import configparser
import os
from deep_translator import GoogleTranslator
from utils import get_from_keyboard
from utils_translate import translateText


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
    parser.add_argument("-t", "--target",    help="URL of the YouTube video", required=True)
    parser.add_argument("-l", "--language",  help="Target language for translation", required=False)

    args = parser.parse_args()
    if not args.language:
        print("output target language not defined in asked command\n => default language will be used (from config.ini): "+ target_language)
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

    # call main function
    translateText(args.target, target_language, max_length)


if __name__ == "__main__":
    print("### RUNNING : " + os.path.basename(__file__) + " ###")
    main()

# faire une traduction
# https://www.youtube.com/watch?v=XH-7bMLZhdk
# https://pypi.org/project/deep-translator/

