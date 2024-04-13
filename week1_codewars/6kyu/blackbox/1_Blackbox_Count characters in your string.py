# https://www.codewars.com/kata/52efefcbcdf57161d4000091/train/python

def count(s):
    result = {}
    for char in s:
        if char in result:
            result[char] += 1
        else:
            result[char] = 1
    return result
