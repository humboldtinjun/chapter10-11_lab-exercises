# check if string has duplicates
from operator import truediv


def has_duplicates(string):
    """checks if theres duplicates"""
    found = set() # make found a set
    for item in string: #loops thru letters, if in set returns true, if not false
        if item in found:
            return True
        found.add(item)
    return False

#test
print(has_duplicates('hello'))       # True
print(has_duplicates('world'))       # False
print(has_duplicates('unpredictably'))  # False
