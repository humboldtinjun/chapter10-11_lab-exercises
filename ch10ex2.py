#use get to get rid of the if statement
def value_counts(string): #counts letters in a string
    counter = {} # set counter to zero
    for letter in string:
        counter[letter] = counter.get(letter, 0) + 1
    return counter # checks if letter is in dic, if not 0, if is adds to the counter

print(value_counts('brontosaurus'))
# Output: {'b': 1, 'r': 2, 'o': 2, 'n': 1, 't': 1, 's': 2, 'a': 1, 'u': 2}
