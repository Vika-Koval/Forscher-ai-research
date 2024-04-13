# https://www.codewars.com/kata/5208f99aee097e6552000148
# Працююча версія
def solution(s):
    result = ''
    for char in s:
        if char.isupper():
            result += ' '
        result += char

    return result