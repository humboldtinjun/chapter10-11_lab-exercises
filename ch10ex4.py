#loop thru dictionary and return a list of keys with values greater than 1
def find_repeats(counter):
    """makes a list of keys with values > 1
       counter: dictionary that maps from keys to counts
       returns: list of keys
       """
    repeats = []
    for key in counter:
        if counter[key] > 1:
            repeats.append(key)
        return repeats

#test
counts = {'a': 3, 'b': 1, 'c': 2, 'd': 1}
print(find_repeats(counts))  # Output: ['a', 'c']
