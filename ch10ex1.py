#Why do keys in Python dictionaries have to be hashable?
"""
because dictionaries in python are built on a data structure called a hash table.
it uses hash functions to change the key into a number. the number decides where
in the memory the value is stored.
hashable means it has a hash value that stays the same during its lifetime and can be
compared to other keys using ==
"""

#How do I make a Python set from a list of strings and check whether a string is an element of the set?”
"""
a set is like a list, but only keeps unique items (no duplicates), and super fast.
"""
fruits = ['apple', 'banana', 'cherry', 'banana']
fruit_set = set(fruits)
print(fruit_set)
