word_list = open("wordlist.txt").read().split()
word_set = set(word_list) # to look up faster

def is_interlocking(word, word_set):
    first = word[::2]
    second = word[1::2]
    return first in word_set and second in word_set

for word in word_list:
    if len(word) >= 8 and is_interlocking(word, word_set):
        first = word[::2]
        second = word[1::2]
        print(word, first, second)