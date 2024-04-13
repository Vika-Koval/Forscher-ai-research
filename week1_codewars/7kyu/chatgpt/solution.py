# link: https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# Test 1 : using just the prompt provided

# An isogram is a word that has no repeating letters, consecutive or non-
# consecutive. Implement a function that determines whether a string that contains
# only letters is an isogram. Assume the empty string is an isogram. Ignore letter 
# case.

def is_isogram(string):
    # Convert the string to lowercase to ignore letter case
    string = string.lower()
    
    # Create a set to store unique letters encountered
    seen = set()
    
    # Iterate through each letter in the string
    for char in string:
        # If the letter is already in the set, the string is not an isogram
        if char in seen:
            return False
        # Otherwise, add the letter to the set
        seen.add(char)
    
    # If the loop completes without returning False, the string is an isogram
    return True

# Test 1, Attempt 1, Result 50/50


# Test 2 : using just the example

# Write a function in python that can do the following:
# isIsogram "Dermatoglyphics" = true
# isIsogram "moose" = false
# isIsogram "aba" = false

def is_isogram(word):
    # Convert the word to lowercase to handle case sensitivity
    word = word.lower()
    
    # Create a set to store unique characters
    unique_chars = set()
    
    # Iterate through each character in the word
    for char in word:
        # If the character is already in the set, it's a repeat, return False
        if char in unique_chars:
            return False
        # Otherwise, add it to the set
        unique_chars.add(char)

# Test 2, Attempt 1, Result 50/50
