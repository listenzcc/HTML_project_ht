# coding: utf-8
# Make fake articles in a randomlized rapid way

import time
import random

# Occur probability table for 26 characters
char_prob_dict = dict(
    e=57, a=43, r=39, i=38, o=37,
    t=35, n=34, s=29, l=28, c=23,
    u=19, d=17, p=16, m=15, h=15,
    g=13, b=11, f=9, y=9, w=7,
    k=6, v=5, x=1, z=1, j=1, q=1
)

# Length probability range for components
length_range_dict = dict(
    word=(2, 10),  # One word should contain 2-10 characters.
    sentence=(5, 10),  # One sentence should contain 5-10 words.
    paragraph=(10, 20),  # One paragraph should contain 10-20 sentences.
    article=(7, 10)  # One article should contain 7-10 sentences.
)


def build_char_dict(char_prob_dict=char_prob_dict):
    # Build easily accessed character table
    # By placing each character several times according to probability
    char_dict = []
    for e in char_prob_dict.items():
        for j in range(e[1]):
            char_dict.append(e[0])
    return char_dict


def get_char(char_dict=build_char_dict()):
    # Get charactre using easily accessed character table
    return random.choice(char_dict)


def rand_length(length_range=length_range_dict['word']):
    # Gereralize rand_length for components in length_range_dict
    return int(random.uniform(length_range[0], length_range[1]))


def mk_word(length=0, is_first_word=False):
    # Make fake word
    if length < 2:
        # length can not be too short
        length = rand_length()

    if is_first_word:
        # Leading word has capitalized first character
        string = str.upper(get_char())
        length -= 1
    else:
        string = ''

    for j in range(length):
        string += get_char()
    return string


def mk_sentence(length=0, is_title=False):
    # Make fake sentence
    if length < 1:
        # length can not be too short
        length = rand_length(length_range_dict['sentence'])

    word_list = []
    word_list.append(mk_word(is_first_word=True))
    length -= 1
    for j in range(length):
        # Leading character should be capitalized
        word_list.append(mk_word(is_first_word=is_title))

    if is_title:
        # Title does not have peroid
        return ' '.join(word_list)

    return ' '.join(word_list)+'.'


def mk_paragraph(length=0):
    # Make fake paragraph
    if length < 1:
        # length can not be too short
        length = rand_length(length_range_dict['paragraph'])

    sentence_list = []
    for j in range(length):
        sentence_list.append(mk_sentence())

    return ' '.join(sentence_list)


def mk_article(length=0, newline='\n', author_name='anonymous'):
    # Make fake article
    if length < 1:
        # length can not be too short
        length = rand_length(length_range_dict['article'])

    article_list = []
    # Adding title
    article_list.append('Title: %s' % mk_sentence(is_title=True))
    for j in range(length):
        article_list.append(mk_paragraph())

    # Adding author
    article_list.append('Author: %s' % author_name)
    # Adding date
    article_list.append('Date: %s' % time.ctime())

    # Seperate paragraph using newling
    return newline.join(article_list)


print(mk_article())
