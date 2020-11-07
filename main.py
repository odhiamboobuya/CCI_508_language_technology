# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import string
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
import re

file_path = ""


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


def remove_stopwords(sentence):
    text_tokens = word_tokenize(sentence)
    tokens_without_sw = [word for word in text_tokens if not word in stopwords.words()]
    refined_sentence = " ".join(tokens_without_sw)
    return refined_sentence.strip()


def replace_non_ascii_with_spaces(sentence):
    refined_sentence = ''.join(char for char in sentence if 31 < ord(char) < 127 or char in "\n\r ")
    return refined_sentence.strip()


def remove_html_and_punctuation(sentence):
    html_tags_regex = re.compile(r'<[^>]+>')
    refined_sentence_without_html = html_tags_regex.sub('', sentence)
    punctuation = string.punctuation
    punctuation_regex = r"[{}]".format(punctuation)
    refined_sentence = re.sub(punctuation_regex, "", refined_sentence_without_html)
    return refined_sentence.strip()


def lowercase_all_messages(sentence):
    return sentence.lower()

def remove_emoticons(sentence):
    return sentence


def main(filepath):
    list_of_refined_strings = []
    with open(filepath, encoding='latin-1') as csv_file:
        line_count = 0
        separator = ';,'
        for row in csv_file.readlines():
            tweet_string = row.split(separator)[1].strip()
            tweet_string_without_stopwords = remove_stopwords(tweet_string)
            refined_str_without_non_ascii = replace_non_ascii_with_spaces(tweet_string_without_stopwords)
            refined_str_without_html_and_punctuation = remove_html_and_punctuation(refined_str_without_non_ascii)
            refined_str_lowercase = lowercase_all_messages(refined_str_without_html_and_punctuation)
            refined_str_without_emoticons = remove_emoticons(refined_str_lowercase)
            final_refined_str = refined_str_without_emoticons
            list_of_refined_strings.append(final_refined_str)
            print("now in row " + str(line_count))
            line_count += 1
    output_file_name = "refined_tweet_data.txt"
    output_file = open(output_file_name, "a")
    for refined_string in list_of_refined_strings:
        output_file.write(refined_string + "\n")
    print("output file: " + output_file_name)
    output_file.close()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    main(file_path)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
