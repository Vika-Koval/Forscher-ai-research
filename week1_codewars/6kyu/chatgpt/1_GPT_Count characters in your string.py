# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python
def count(s):
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate through each character in the input string
    for char in s:
        # Increment the count of the character in the dictionary
        char_count[char] = char_count.get(char, 0) + 1

    return char_count
