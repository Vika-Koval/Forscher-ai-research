# З першого разу
def count(s):
#     def count_characters(s):
    # Initialize an empty dictionary to store character counts
    char_count = {}

    # Iterate through each character in the input string
    for char in s:
        # Increment the count of the character in the dictionary
        char_count[char] = char_count.get(char, 0) + 1

    return char_count
