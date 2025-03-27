def word_distance(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    return count

def find_metathesis_pairs(words):
    from collections import defaultdict

    # group words by sorted letters
    anagram_dict = defaultdict(list)
    for word in words:
        key = ''.join(sorted(word))
        anagram_dict[key].append(word)

    # check each anagram group for metathesis pairs
    for group in anagram_dict.values():
        if len(group) > 1:
            for i in range(len(group)):
                for j in range(i + 1, len(group)):
                    if word_distance(group[i], group[j]) == 2:
                        print(group[i], group[j])


words = [
    'converse', 'conserve',
    'listen', 'silent',
    'deltas', 'desalt', 'lasted', 'salted', 'slated', 'staled'
]

find_metathesis_pairs(words)
