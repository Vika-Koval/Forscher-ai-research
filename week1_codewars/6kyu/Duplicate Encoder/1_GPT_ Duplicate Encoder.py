def duplicate_encode(s):
#     def duplicate_encoder(s):
    # Convert the input string to lowercase
    s_lower = s.lower()
    
    # Initialize an empty string to store the result
    result = ''
    
    # Create a dictionary to count character occurrences
    char_count = {}
    for char in s_lower:
        char_count[char] = char_count.get(char, 0) + 1
    
    # Iterate through each character in the lowercase string
    for char in s_lower:
        # Check the count of the character
        if char_count[char] > 1:
            # If the count is greater than 1, append ')' to the result string
            result += ')'
        else:
            # If the count is 1, append '(' to the result string
            result += '('
    
    return result
