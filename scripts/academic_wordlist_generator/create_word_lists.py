# !/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = 'arashsaidi'

import string
import xml.etree.ElementTree as ElTree
from lxml import etree
from collections import Counter
import re

most_frequent_words = []  # List of most frequent words taken from file

global_word_list = []  # The word_list as read from file(s)
global_english_word_list = []

global_word_freq_list = {}  # List of frequencies for one xml/text document
global_word_list_many_freq_lists = []  # Frequency list of many xml/text documents

global_reduced_freqs = {}  # Dict of relative frequency


def create_english_word_list(filename):
    """
    Reads and stores a list of English words
    :param filename:
    :return: None
    """
    global global_english_word_list

    if not global_english_word_list:
        with open(filename) as f:
            for line in f:
                global_english_word_list.append(re.sub(r'\s+', '', line))


def create_most_freq_word_list(filename):
    """
    Reads and stores a list of most frequent words
    :param filename:
    :return: None
    """
    global most_frequent_words

    if not most_frequent_words:
        with open(filename) as fp:
            for line in fp:
                most_frequent_words.append(re.sub(r'\s+', '', line))


def read_tagged_word_list(filename):
    # TODO: write and test this method
    """
    Method for reading tagged words. Skip every line and read word within ""
    :param filename: path to file
    :return: None
    """
    print 'reading tagged file'


def read_many_xml_in_one_file(filename, to_xml=' ', write_to_file=False):
    """
    Reads an xml files and creates a word list
    :param filename:
    :param to_xml:
    :param write_to_file:
    :return:
    """
    global global_word_list_many_freq_lists

    with open(filename) as f:
        for line in f:
            to_xml += line
            if '</document>' in to_xml:
                # goes through each document and adds to list
                global_word_list_many_freq_lists.append(read_xml(to_xml, True, write_to_file))
                to_xml = ' '

    return global_word_list_many_freq_lists


def read_xml(filename, from_string=False, write_to_file=False):
    """
    Reads a single xml file
    :param filename:
    :param from_string:
    :param write_to_file:
    :return:
    """
    # TODO: write the stripped xml to file for OBT (Oslo Bergen Tagger)
    print 'reading xml'
    if write_to_file:
        pass

    if from_string:
        try:
            tree = ElTree.fromstring(filename)
            no_tags = ElTree.tostring(tree, encoding='utf8', method='text')
        except Exception as inst:
            return {'Error reading xml': inst}
    else:
        tree = etree.parse(filename)
        no_tags = etree.tostring(tree, encoding='utf-8', method='text')
        no_tags = re.sub(ur'[^a-zA-Z0-9]', ' ', no_tags, re.UNICODE)

    return create_word_list(no_tags)


def read_txt(filename):
    """
    Reads a text file and creates a word list
    :param filename:
    :return:
    """
    file_object = open(filename, 'r')
    file_as_string = file_object.read()
    return create_word_list(file_as_string)


def create_word_list(text_as_string):
    """
    Creates a word list, removes punctuation, lowers characters
    :param text_as_string:
    :return:
    """
    # print 'creating word list'
    global global_word_list

    for w in text_as_string.split():
        word = w.translate(string.maketrans("", ""), string.punctuation).lower()
        if len(word) > 0:
            global_word_list.append(word)  # Appends each word to global word list

    return global_word_list


def is_number(s):
    """
    Checks if s is a number
    :param s: any value
    :return: boolean
    """
    try:
        float(s)
        return True
    except ValueError:
        return False


def reduced_frequency(cutoff):
    """
    The method from the swedish article. Computes a reduced frequency for each word in the list by iterating through
    the list and assigning a value based on its frequency in relation to the length of list
    :param cutoff: the reduced frequency to exclude files
    :return: None
    """
    print 'reduced frequency method'
    global global_word_list
    global global_reduced_freqs

    doc_length = len(global_word_list)
    print 'number of words in files: {}'.format(doc_length)
    count = 0
    freq_list = count_words(global_word_list)  # Calls count_words()

    for (w, freq) in freq_list.items():
        # a count for testing
        count += 1
        # if count % 100 == 0:
        #     print '.',
        # if count % 10000 == 0:
        #     print '\n{}'.format(count)
        # end of count
        global_reduced_freqs[w] = 0
        interval = doc_length / freq
        if interval != doc_length and freq > cutoff:
            for i in range(0, doc_length, interval):
                # Checking if a word is in interval
                if w in global_word_list[i: interval + i]:
                    global_reduced_freqs[w] += 1


def count_words(word_list, print_words=False):
    """
    Creates a frequency distribution of the words in articles
    :param word_list: the word list read from files
    :param print_words: for testing
    :return: frequency distribution
    """
    freq_dist = Counter(word_list)
    global global_word_freq_list

    if print_words:
        for (word, freq) in freq_dist.items():
            print('{:25}{:10}'.format(word, freq))

    global_word_freq_list = freq_dist.copy()
    return freq_dist


def remove_most_frequent_words_numbers_english(score):
    """
    Should only be run once reduce_frequency method has been run
    removes both from global_word_list and global_relative_freqs
    :param score: The frequency score for removing words with lower reduced frequency than given number
    :return: None
    """
    print 'removing most frequent words'
    print 'removing numbers'
    print 'removing english words'
    print 'removing words with a relative frequency below: ', score
    global most_frequent_words
    global global_reduced_freqs
    global global_word_list

    for w, v in global_reduced_freqs.items():
        # Removes words of length 1, don't know if this should be done here
        if v < score:
            del global_reduced_freqs[w]
        elif w in most_frequent_words or is_number(w) or w in global_english_word_list or len(w) == 1:
            del global_reduced_freqs[w]


def remove_relative_frequent_words_below_score(score):
    """
    This removes words with relative frequencies lower that score
    :param score:
    :return:
    """
    print 'removing words with a relative frequency below: ', score
    global global_reduced_freqs

    for w, value in global_reduced_freqs.items():
        if value < score:
            del global_reduced_freqs[w]


# GETTERS (for testing)
def get_global_word_list():
    if global_word_list:
        return global_word_list
    else:
        return 'global_word_list is empty'


def get_global_word_list_many_freq_lists():
    if global_word_list_many_freq_lists:
        return global_word_list_many_freq_lists
    else:
        return 'global_word_list_many_freq_lists is empty'


def get_global_word_freq_list():
    if global_word_freq_list:
        return global_word_freq_list
    else:
        return 'global_word_freq_list is empty'


def get_global_reduced_freqs():
    if global_reduced_freqs:
        return global_reduced_freqs
    else:
        return 'get_global_reduced_freqs is empty'


