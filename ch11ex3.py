# shift words to make a cipher
letters = 'abcdefghijklmnopqrstuvwxyz'
letter_map = dict(zip(letters, range(len(letters))))

def shift_word(word, shift):
    """shifts the letters to make a cipher"""
    result = []
    for char in word:
        index = letter_map[char]
        shifted_index = (index + shift) % 26
        result.append(letters[shifted_index])
    return ''.join(result)
print(shift_word("cheer", 7))   # jolly
print(shift_word("melon", 16))  # cubed
