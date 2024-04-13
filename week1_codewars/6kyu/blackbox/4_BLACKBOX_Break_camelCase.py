# https://www.codewars.com/kata/5208f99aee097e6552000148
# Працююча версія
def solution(s):
    word = ''
    for c in s:
        if c.islower():
            word += c
        elif c.isupper():
                word += ' '
                word += c
        elif c == ' ':
                word += ' '
        else:
            word += c
    result = word
    return result
