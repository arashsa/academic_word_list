stop_list = []
with open('../../1000_hifreq_lemmas_forms.txt') as sl:
    for word in sl.readlines():
        stop_list.append(word.rstrip())

with open('list_cutoff.txt') as l:
    for sentence in l.readlines():
        s = sentence.split()
        if s[1] not in stop_list:
            print s[1]