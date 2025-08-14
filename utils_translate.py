# utils.py
import os
from deep_translator import GoogleTranslator


def translateText(input_file, target_language, max_length):
    """Translate the text in the file given using GoogleTranslate"""
    # input_file      : path to text to translate
    # target_language : language code to translate to
    # max_length      : max length of text limit by each translator pass

    try:
        max_length = int(max_length)
    except ValueError:
        print("Unknown parameter in config : use int number for max limit text for each pass")

    print ("Starting translation...")
    dir      = os.path.dirname(input_file)
    name_ext = os.path.basename(input_file)
    name     = os.path.splitext(name_ext)[0]  # remove extension

    # cut text in max char delimited by the last point
    with open(input_file, 'r') as f:
        content = f.read()
        chunks = split_text_into_chunks(content, max_length)

    translated = ""
    x=0
    for chunk in chunks:
        x +=1
        print(".", end="", flush=True)
        translated += GoogleTranslator(source='auto', target=target_language).translate(chunk)
    print("")
    print("GoogleTranslator has been called "+ str(x) + " times")

    new_translated_file_name = name + "_" + target_language + ".txt"
    new_translated_file_name_path = os.path.join(dir, new_translated_file_name)
    with open(new_translated_file_name_path, 'w', encoding='utf-8') as f:
        f.write(translated)
    
    print("Translated text saved in:\n'" + dir +" => "+ new_translated_file_name + "'")


def split_text_into_chunks(text, max_length):
    """Split the text into chunks of max_length, ensuring not to cut off sentences"""
    chunks = []
    while len(text) > max_length:
        # Find the last period within the max_length limit
        split_str = text.rfind('.', 0, max_length)
        if split_str == -1:  # No period found, use space
            split_str = text.rfind(' ', 0, max_length)
        if split_str == -1:  # No space found, force split
            split_str = max_length
        chunks.append(text[:split_str + 1].strip())
        text = text[split_str + 1:].strip()
    if text:
        chunks.append(text)
    return chunks
