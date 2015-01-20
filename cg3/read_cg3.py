import re


def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False


def read_cg3(cg3_file):
    """
    Reads a cg3 file and returns a list of each sentence removing numbers, and unknown words.
    :param cg3_file: path to file
    :return: list of words + attributes
    """
    rx_token = re.compile("^\"<(.+?)>\"$")
    rx_attributes = re.compile("^\s+\".+?\"\s+.+$")
    rx_eos = re.compile("^\s*$")

    curr_token = None
    curr_word = []
    curr_sentence = []
    result = []

    with open(cg3_file) as cg3_file:
        for line in cg3_file:

            if rx_token.match(line):
                curr_token = "\"%s\"" % rx_token.match(line).group(1)
                # print curr_token

            if rx_attributes.match(line):
                curr_word = line.split()
                # print curr_word
                if curr_token and curr_word:
                    # to get more tags uncomment this and comment below
                    # curr_sentence += [[curr_token] + curr_word]
                    if '$' not in curr_word[0] and not is_number(curr_word[0].strip('"').replace('.', '')) \
                            and len(curr_word[0]) < 30 and curr_word[1] != 'ukjent':
                        # curr_sentence += [[curr_token.strip('"')] +
                        # [curr_word[0].lower().strip('"')] + [curr_word[1]]]
                        curr_sentence += [curr_word[0].lower().strip('"')]
                    curr_token = None
                    curr_word = []

            if rx_eos.match(line):
                # print curr_sentence
                if curr_sentence:
                    result += [curr_sentence]
                curr_sentence = []
                curr_token = None
                curr_word = []

    # cleanup if last sentence not EOL
    if curr_token and curr_word:
        # print 'cg3 reached end of file and did some cleanup on file {}'.format(cg3_file)
        curr_sentence += [curr_word[0].lower().strip('"')]

    if curr_sentence:
        # print 'cg3 reached end of file and did some cleanup on file {}'.format(cg3_file)
        result += curr_sentence

    return result