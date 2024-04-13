# link: https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# Test 1 : using just the provided prompt

# Request:
    # An isogram is a word that has no repeating letters, consecutive or non-
    # consecutive. Implement a function that determines whether a string that contains
    # only letters is an isogram. Assume the empty string is an isogram. Ignore letter 
    # case.

# Blackbox's answer:
def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))
# Test 1, Attempt 1, Result 50/50


# Test 2 : using just the example

# Request:
    # Write a function in python that can do the following:
    # isIsogram "Dermatoglyphics" = true
    # isIsogram "moose" = false
    # isIsogram "aba" = false

# Blackbox's answer:
def is_isogram(word):
    return len(word) == len(set(word.lower()))
# Test 2, Attempt 1, Result 50/50


# Test 3 : using the tests provided

# Request:
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

# Blackbox's answer:
def is_isogram(word):
    """
    Returns True if the given word is an isogram, and False otherwise.
    A word is an isogram if it does not have any repeating characters.
    """
    # Use a set to keep track of the characters we've seen so far
    seen = set()
    
    # Iterate over each character in the word
    for char in word.lower():
        # If the character is alphanumeric and we've seen it before, return False
        if char.isalnum() and char in seen:
            return False
        # Add the character to the set of seen characters
        seen.add(char)
    
    # If we've made it through the entire word without returning False, return True
    return True
# Test 3, Attempt 1, Result 50/50


# Test 4 : a very brief formulation of the prompt

# Request:
    # write a function in python that checks if the word is an isogram

# Blackbox's answer:
def is_isogram(word):
    return len(word) == len(set(word))
# Test 4, Attempt 1, Result 45/50

# Request2:
    # you didn't consider that lowercase and uppercase letters are the same

# Blackbox's answer:
def is_isogram(word):
    return len(word) == len(set(word.lower()))
# Test 4, Attempt 2, Result 50/50


# Conclusion : Blackbox AI did a decent job at this level of difficulty and almost passed 100% of the tests on the first try
# The only time it failed was when a very short formulation of the prompt was provided
# 3 of 4 functions were almost identical and had a similar approach 
# Interestingly, test 3 was quite different and had a different approach when test cases were provided
