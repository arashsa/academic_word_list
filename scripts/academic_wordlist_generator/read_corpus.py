__author__ = 'arashsaidi'

import glob

from scripts.academic_wordlist_generator.create_word_lists import read_xml, read_txt


def read_all_files(p, ending):
    """
    Reads all files in folder.
    :param p: path
    :param ending: ending of files: txt, xml.
    :return: None
    """
    # reads all files in a folder:
    # Example of usage: read_all_files('/folder/*.xml', 'xml')
    path = p
    files = glob.glob(path)
    count = 0
    for name in files:
        count += 1
        # read_current_file returns a frequency distribution
        # print 'Reading file: ' + name
        read_current_file(name, ending)
    print "Read {} files".format(count)


def read_all_files_every(p, ending, how_many_files_to_read):
    """
    Reads every nth file in a folder
    :param p: path
    :param ending: ending of files: txt, xml.
    :param how_many_files_to_read: number of files to read
    :return: None
    """
    # reads all files in a folder:
    # Example of usage: read_all_files('/folder/*.xml', 'xml')
    path = p
    files = glob.glob(path)
    count = 0
    for name in files:
        # read_current_file returns a frequency distribution
        # print 'Reading file: ' + name
        count += 1
        read_current_file(name, ending)
        if count == how_many_files_to_read:
            break
    print "Read {} files".format(how_many_files_to_read)


def read_current_file(f, ending):
    """
    Reads just one file
    :param f: file
    :param ending: txt, xml
    :return: None
    """
    # calls methods according to file type
    if ending == 'xml':
        read_xml(f)
    elif ending == 'txt':
        read_txt(f)
    else:
        print 'ERROR: Do not support type of file'

