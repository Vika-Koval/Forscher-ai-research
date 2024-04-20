#gpt:
import time
from memory_profiler import memory_usage
def create_acronym(message: str) -> str: 
    """
    Create acronyms from a given message.

    Args:
        message (str): The message from which acronyms will be created.

    Returns:
        str: A string containing acronyms.

    Examples:
        >>> create_acronym("random access memory\\nAs soon As possible")
        'RAM - random access memory\\nASAP - As soon As possible'
        >>> create_acronym("random access memory")
        'RAM - random access memory'
        >>> create_acronym('As soon As possible')
        'ASAP - As soon As possible'
    """
    if isinstance(message, int):  # Better type checking
        return None

    # Simplified character check
    if not all(char.isalpha() or char in (' ', '\n') for char in message):
        return None

    lines = []
    message = message.split('\n')

    for mess in message:
        words = mess.split()
        acronym = ''.join(word[0] for word in words).upper()
        lines.append(f"{acronym} - {mess.strip()}")

    return '\n'.join(lines)


import string

ALPHABET_START_UPPER = ord('A')
ALPHABET_END_UPPER = ord('Z')
ALPHABET_START_LOWER = ord('a')
ALPHABET_END_LOWER = ord('z')

def shift_char(char, key):
    if char.isupper():
        start = ALPHABET_START_UPPER
        end = ALPHABET_END_UPPER
    elif char.islower():
        start = ALPHABET_START_LOWER
        end = ALPHABET_END_LOWER
    else:
        return char  # Return non-alphabetic characters unchanged
    
    shifted = start + (ord(char) - start + key) % 26
    return chr(shifted)

def caesar_encode(message: str, key: int) -> str:
    """
    >>> caesar_encode('abc', 1)
    'bcd'
    >>> caesar_encode('xyz', 2)
    'zab'
    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    >>> caesar_encode("strings are awesome", 26)
    'strings are awesome'
    """
    return ''.join(shift_char(char, key) for char in message)

def caesar_decode(message: str, key: int) -> str:
    """
    >>> caesar_decode("oddzwsr gqwsbqs", 40)
    'applied science'
    >>> caesar_decode("e hkra lupdkj", 100)
    'i love python'
    >>> caesar_decode('abc', 3)
    'xyz'
    """
    return ''.join(shift_char(char, -key) for char in message)





start = time.time()

for _ in range(100):
    create_acronym("random access memory\nAs soon As possible")
for _ in range(100):
    caesar_decode('abcdefgh', 3)
for _ in range(100):
    caesar_encode('abcdefgh', 3)
end = time.time()

print((end - start)*5000000)

#time for gpt = 5009.174346923828
def main_code():

    start = time.time()
    for _ in range(100):
        create_acronym("random access memory\nAs soon As possible")
    for _ in range(100):
        caesar_decode('abcdefgh', 3)
    for _ in range(100):
        caesar_encode('abcdefgh', 3)
    end = time.time()
mem_usage = memory_usage(main_code)
print("Maximum memory usage (in MiB):", max(mem_usage))
# Memory_profiler returned: Maximum memory usage (in MiB): 43.3515625



#Blackbox:
import time
from memory_profiler import memory_usage
def create_acronym (message:str)->str:
    """
    In this function we are creating acronym
    """
    if isinstance(message,int):
        return
    for mess in message:
        if not mess.isalpha() and mess!=' ' and mess!='\n':
            return
    line = ''
    for mess in message.split('\n'):
        m_spl = mess.split()
        text = ''
        for word in m_spl:
            text += word[0]
        line += f'{text.upper()} - {mess.strip()}' + '\n'
    return line[:-1]


"""
This module provides functions to convert a sentence to and from Caesar cipher.
"""

def caesar_encode(message: str, key: int) -> str:
    """
    This function encodes a message using Caesar cipher.

    Args:
    message (str): The message to be encoded.
    key (int): The shift value for the Caesar cipher.

    Returns:
    str: The encoded message.

    Examples:
    >>> caesar_encode('abc', 1)
    'bcd'
    >>> caesar_encode('xyz', 2)
    'zab'
    >>> caesar_encode('computer', 3)
    'frpsxwhu'
    >>> caesar_encode("strings are awesome", 26)
    'strings are awesome'
    """
    if key >= 26:
        key = key % 26

    new_message = ''
    for letter in message:
        if not letter.isalpha():
            new_message += letter
            continue

        coef = ord(letter) + key
        if letter.islower():
            new_message += chr(97 + (coef - 97) % 26)
        else:
            new_message += chr(65 + (coef - 65) % 26)

    return new_message

def caesar_decode(message: str, key: int) -> str:
    """
    This function decodes a message from Caesar cipher.

    Args:
    message (str): The message to be decoded.
    key (int): The shift value for the Caesar cipher.

    Returns:
    str: The decoded message.

    Examples:
    >>> caesar_decode("oddzwsr gqwsbqs", 40)
    'applied science'
    >>> caesar_decode("e hkra lupdkj", 100)
    'i love python'
    >>> caesar_decode('abc', 3)
    'xyz'
    """
    if key >= 26:
        key = key % 26

    new_message = ''
    for letter in message:
        if not letter.isalpha():
            new_message += letter
            continue

        coef = ord(letter) - key
        if letter.islower():
            new_message += chr(97 + (coef - 97) % 26)
        else:
            new_message += chr(65 + (coef - 65) % 26)

    return new_message



start = time.time()

for _ in range(100):
    create_acronym("random access memory\nAs soon As possible")
for _ in range(100):
    caesar_decode('abcdefgh', 3)
for _ in range(100):
    caesar_encode('abcdefgh', 3)
end = time.time()

print((end - start)*5000000)

#time for blackbox = 4814.863204956055
def main_code():

    start = time.time()
    for _ in range(100):
        create_acronym("random access memory\nAs soon As possible")
    for _ in range(100):
        caesar_decode('abcdefgh', 3)
    for _ in range(100):
        caesar_encode('abcdefgh', 3)
    end = time.time()
mem_usage = memory_usage(main_code)
print("Maximum memory usage (in MiB):", max(mem_usage))
# Memory_profiler returned: Maximum memory usage (in MiB): 43.14453125


#my code:

"""
This module converts a sentence to ceasar code and back.
"""
"""
create acronym
"""
import time
from memory_profiler import memory_usage
def create_acronym (message:str)->str:
    """
    In this function we are creating acronym
    >>> create_acronym("random access memory\\nAs soon As possible")
    'RAM - random access memory\\nASAP - As soon As possible'
    >>> create_acronym("random access memory")
    'RAM - random access memory'
    >>> create_acronym('As soon As possible')
    'ASAP - As soon As possible'
    """
    if isinstance(message,int):
        return None
    for mess in message:
        if mess.isalpha() is False and mess!=' ' and mess!='\n':
            return None
    line = ''
    message = message.split('\n')
    for mess in message:
        m_spl = mess.split()
        text = ''
        for word in m_spl:
            text = text + word[0]
        line += f'{text.upper()} - {mess.strip()}' + '\n'
    return line[:-1]
    
def caesar_encode(message:str,key:int)->str:
    """
    This function encodes message to caesar encode.
    >>> caesar_encode('abc', 1)
    'bcd'
    >>> caesar_encode('xyz',2)
    'zab'
    >>> caesar_encode('computer',3)
    'frpsxwhu'
    >>> caesar_encode("strings are awesome", 26)
    'strings are awesome'
    """
    if key>=26:
        key = key%26
    new_message = ''
    for letter in message:
        coef = ord(letter)+key
        if ord(letter)==32:
            letter = ' '
        elif ord(letter)<65 or ord(letter)>122 or (ord(letter)>90 and ord(letter)<97):
            return None
        elif ord(letter) > 97 and coef>122:
            letter = chr(96+key-122+ord(letter))
        elif ord(letter) <91 and coef>90:
            letter = chr(64+key-(90-ord(letter)))
        else:
            letter = chr(coef)
        new_message += letter
    return new_message

def caesar_decode(message:str,key:int)->str:
    """
    This function decodes a message from caesar code.
    >>> caesar_decode("oddzwsr gqwsbqs", 40)
    'applied science'
    >>> caesar_decode("e hkra lupdkj", 100)
    'i love python'
    >>> caesar_decode('abc',3)
    'xyz'
    """
    new_message = ''
    if key>=26:
        key = key%26
    for letter in message:
        coef = ord(letter)-key
        if ord(letter)==32:
            letter = ' '
        elif ord(letter)<65 or ord(letter)>122 or (ord(letter)>90 and ord(letter)<97):
            return None
        elif ord(letter) > 96 and coef<97:
            letter = chr(ord(letter) - 96 + 122 - key)
        elif ord(letter) <91 and coef<65:
            letter = chr(ord(letter) - 64 + 90 - key)
        else:
            letter = chr(coef)
        new_message += letter
    return new_message
    


start = time.time()

for _ in range(100):
    create_acronym("random access memory\nAs soon As possible")
for _ in range(100):
    caesar_decode('abcdefgh', 3)
for _ in range(100):
    caesar_encode('abcdefgh', 3)
end = time.time()

print((end - start)*5000000)

#time for my code = 8735.65673828125
def main_code():

    start = time.time()
    for _ in range(100):
        create_acronym("random access memory\nAs soon As possible")
    for _ in range(100):
        caesar_decode('abcdefgh', 3)
    for _ in range(100):
        caesar_encode('abcdefgh', 3)
    end = time.time()
mem_usage = memory_usage(main_code)
print("Maximum memory usage (in MiB):", max(mem_usage))
# Memory_profiler returned: Maximum memory usage (in MiB): 43.52734375

#time for ai's versions is better than for mine
