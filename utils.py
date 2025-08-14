# utils.py
import re
import os


def get_from_keyboard(prompt):
    """use it when you ask from an input"""
    # if user cancel the action it will exit properly
    try:
        x = input(prompt)
        return x
    except KeyboardInterrupt:
        print("\nAborting by user (Ctrl+C).")
        exit(0)


def sanitize_filename(filename):
    """Replace non authorized characters with nothing"""
    str = re.sub(r'[^\w\d\s\-_,!\[\]<>\'()+]', '', filename)
    # only one space between words
    str = re.sub(r'\s+', ' ', str)
    return str

