
def long_str(letters):
    starting_index = 0
    maximum_length = 0
    checked_chars = {}
    for i in range(len(letters)):
        if letters[i] in checked_chars:
            starting_index = checked_chars[letters[i]] +1
        maximum_length =  i-starting_index +1
        checked_chars[letters[i]] = i
    return maximum_length
print(long_str("abcdefgabc"))