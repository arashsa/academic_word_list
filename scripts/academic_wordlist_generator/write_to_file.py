__author__ = 'arashsaidi'

import operator
import create_word_lists


def write_list_to_file(the_list, args=''):
    """
    Writes a normal list to file
    :param the_list:
    :param args:
    :return:
    """
    make_file = open('test_list.txt', 'w')
    if args:
        make_file.write(args + '\n')
    for w in the_list:
        make_file.write(w + '\n')


def write_dict_to_file(the_dict, args=''):
    """
    Writes a dictionary with two values to file sorted alphabetically
    :param the_dict:
    :param args:
    :return:
    """
    make_file = open('list_alpha.txt', 'w')
    if args:
        make_file.write(args + '\n')

    global_word_freq_list = create_word_lists.get_global_word_freq_list()

    make_file.write('{:20} {:10} {:10}\n'.format('word', 'r_freq', 'f_freq'))
    word_count = 1
    for w, count in sorted(the_dict.items()):
        make_file.write('{}: {:20} {:10} {:10}\n'.format(word_count, w, count, global_word_freq_list[w]))
        word_count += 1


def write_dict_to_file_cutoff(the_dict):
    """
    Writes a dictionary with two values to file sorted by the value (integers)
    :param the_dict:
    :return:
    """
    make_file = open('list_cutoff.txt', 'w')
    global_word_freq_list = create_word_lists.get_global_word_freq_list()

    make_file.write('{:20} {:10} {:10}\n'.format('word', 'reduced_frequency', 'frequency'))
    sorted_dict = sorted(the_dict.iteritems(), key=operator.itemgetter(1), reverse=True)
    word_count = 1
    for (w, v) in sorted_dict:
        make_file.write('{}: {:20} {:10} {:10}\n'.format(word_count, w, v, global_word_freq_list[w]))
        word_count += 1

