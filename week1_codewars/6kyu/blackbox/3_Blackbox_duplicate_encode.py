https://www.codewars.com/kata/54b42f9314d9229fd6000d9c/train/python
def duplicate_encode(word):
    word = word.lower()
    encoded = ""
    for char in word:
        if word.count(char) == 1:
            encoded += "("
        else:
            encoded += ")"
    return encoded
