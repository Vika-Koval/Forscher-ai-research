# Код з GPT, достатньо було тільки умови
def break_camel_case(s):
    # Initialize an empty result string
    result = ''

    # Iterate through each character in the input string
    for char in s:
        # Check if the character is uppercase (indicating the start of a new word)
        if char.isupper():
            # Add a space before the uppercase character
            result += ' '
        
        # Add the current character to the result string
        result += char

    return result
