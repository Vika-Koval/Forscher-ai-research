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


# Test 3 : using the tests provided

# Write a function that can pass the following tests:
# def fixed_tests():
#     @test.it('Basic Test Cases')
#     def basic_test_cases():      
#         test.assert_equals(is_isogram("Dermatoglyphics"), True )
#         test.assert_equals(is_isogram("isogram"), True )
#         test.assert_equals(is_isogram("aba"), False, "same chars may not be adjacent" )
#         test.assert_equals(is_isogram("moOse"), False, "same chars may not be same case" )
#         test.assert_equals(is_isogram("isIsogram"), False )
#         test.assert_equals(is_isogram(""), True, "an empty string is a valid isogram" )

def is_isogram(string):
    # Convert string to lowercase to handle case insensitivity
    string = string.lower()
    
    # Set to store characters encountered
    char_set = set()
    
    # Iterate through each character in the string
    for char in string:
        # Check if character is alphabetic
        if char.isalpha():
            # If character is already in the set, it's not an isogram
            if char in char_set:
                return False
            # Otherwise, add it to the set
            else:
                char_set.add(char)
    
    # If all characters are unique, it's an isogram
    return True

# Test 3, Attempt 1, Result 50/50


# Test 4 : a very brief formulation of the prompt

# write a function in python that checks if the word is an isogram

def is_isogram(word):
    # Convert the word to lowercase to make the comparison case-insensitive
    word = word.lower()
    
    # Create a set to store unique letters encountered
    unique_letters = set()
    
    # Iterate through each letter in the word
    for letter in word:
        # If the letter is already in the set, it's a repeated letter, so return False
        if letter in unique_letters:
            return False
        # Otherwise, add the letter to the set
        else:
            unique_letters.add(letter)
    
    # If the loop completes without returning False, the word is an isogram
    return True

# Test 4, Attempt 1, Result 50/50


# Conclusion : ChatGPT did a great job at this level and passed 100% of the tests on the first try
# All of the functions that were generated were almost identical but in test 3 the answer was slightly different
# probably because more details and test cases were provided
