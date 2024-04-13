# https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
# Проходить тільки 1 тест
def string_conversion(string):
    char_count = {}
    result = ''
    for char in string:
        char = char.lower()
        if char in char_count:
            result += ')'
        else:
            result += '('
        char_count[char] = char_count.get(char, 0) + 1
    return result
