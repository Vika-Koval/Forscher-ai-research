# Це не працює
def solution(s):
    words = []
    word = ''
    for c in s:
        if c.islower():
            word += c
        elif c.isupper():
            if word:
                words.append(word.capitalize())
                word = ''
            words.append(c.lower())
        elif c == ' ':
            if word:
                words.append(word.capitalize())
                word = ''
            words.append(c)
        else:
            word += c
    if word:
        words.append(word.capitalize())
    result = ' '.join(words)
    return result.replace(' ', '').capitalize()
