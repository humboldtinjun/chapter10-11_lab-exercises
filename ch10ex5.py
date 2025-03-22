#write a function that combines two dictionaries into a new one
def value_counts(string): #counts letters in a string
    counter = {} # set counter to zero
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter # checks if letter is in dic, if not 0, if is adds to the counter

def add_counters(counter1, counter2):
    result = {}
    for key in counter1:
        result[key] = counter1.get(key, 0) + counter2.get(key, 0)
    for key in counter2:
        if key not in result:
            result[key] = counter2[key]
    return result

counter1 = value_counts('brontosaurus')  # e.g., {'b': 1, 'r': 2, 'o': 2, ...}
counter2 = value_counts('apatosaurus')   # e.g., {'a': 3, 'p': 1, 't': 1, ...}

c1 = value_counts('brontosaurus')
c2 = value_counts('apatosaurus')
print(add_counters(c1, c2))
