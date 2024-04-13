# link: https://www.codewars.com/kata/54ba84be607a92aa900000f1/train/python
# Test 1 : using just the provided prompt

# An isogram is a word that has no repeating letters, consecutive or non-
# consecutive. Implement a function that determines whether a string that contains
# only letters is an isogram. Assume the empty string is an isogram. Ignore letter 
# case.

def is_isogram(word):
    word = word.lower()
    return len(word) == len(set(word))

# Test 1, Attempt 1, Result 50/50
