def print_anagram_sets(words):
    anagram_dict = {}

    # build dictionary using sorted letters as the key
    for word in words:
        key = ''.join(sorted(word))
        if key in anagram_dict:
            anagram_dict[key].append(word)
        else:
            anagram_dict[key] = [word]

    # print all lists that have more than one word (anagram sets)
    for word_list in anagram_dict.values():
        if len(word_list) > 1:
            print(word_list)

# example
words = [
    'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
    'retainers', 'ternaries',
    'generating', 'greatening',
    'resmelts', 'smelters', 'termless'
]

print_anagram_sets(words)

words = [
    'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled',
    'retainers', 'ternaries',
    'generating', 'greatening',
    'resmelts', 'smelters', 'termless'
]

print_anagram_sets(words)
