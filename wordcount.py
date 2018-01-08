# put your code here.
word_counts = {}

import sys
# import Counter

file_names = sys.argv[1:]
print file_names

def count_words(fil):
    """ counts occurance of each word in text file """
    print fil
    with open(fil) as fil:
        words = fil.read().split()

        for word in words:
            word = word.strip('()_\",.?!:;').lower()
            word_counts[word] = word_counts.get(word, 0) + 1

        # c = Counter(words)

        for word in words:
            # print word, c[word]
            print word, word_counts[word]
        print " \n \n \n \n "

for f in file_names:
    count_words(f)

# https://svn.python.org/projects/python/branches/release22-maint/Lib/string.py