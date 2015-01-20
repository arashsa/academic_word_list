__author__ = 'arashsaidi'

from scripts.academic_wordlist_generator.create_word_lists import *
from scripts.academic_wordlist_generator.printing import *
from scripts.academic_wordlist_generator.read_corpus import *
from scripts.academic_wordlist_generator.write_to_file import *
import time


def create_list(print_alpha=False, print_val=False, cutoff=15):
    """
    Method that initiates the main processes. Before running this make sure you have read in data from file
    or stream.
    :param print_alpha:
    :param print_val:
    :param cutoff: The cutoff for the reduced frequency.
    :return: None
    """
    create_most_freq_word_list(
        '/Users/arashsaidi/Work/TextLab/academic_dictionary-d197b26860cde69c7d7b21ede663781e44b0f557/'
        'emptylist.txt')
    create_english_word_list(
        '/Users/arashsaidi/Work/TextLab/academic_dictionary-d197b26860cde69c7d7b21ede663781e44b0f557/'
        'brit-a-z.txt')
    reduced_frequency(cutoff)
    remove_most_frequent_words_numbers_english(cutoff)

    if print_alpha:
        print_dictionary_alphabetically(get_global_reduced_freqs())
    if print_val:
        print_dictionary_by_value(get_global_reduced_freqs())


print "starting time: {}.{}".format(time.gmtime().tm_hour + 1, time.gmtime().tm_min)
start_time = time.time()
read_all_files('/Users/arashsaidi/Work/Corpus/DUO_Corpus/Bokmaal-tagged-random/*.txt', 'txt')
create_list()
write_dict_to_file(get_global_reduced_freqs())
write_dict_to_file_cutoff(get_global_reduced_freqs())
print "--- {} seconds ---".format(time.time() - start_time)