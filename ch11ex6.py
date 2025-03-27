def word_distance(word1, word2):
    count = 0
    for a, b in zip(word1, word2):
        if a != b:
            count += 1
    return count
print(word_distance("hello", "hullo"))  # Output: 1
print(word_distance("apple", "apply"))  # Output: 1
print(word_distance("cat", "dog"))      # Output: 3
