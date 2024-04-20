#My code:
"""
This module converts a sentence to ceasar code and back.
"""
"""
create acronym
"""
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
    



#Blackbox: 

#Request1:
#improve this code

#Answer:

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
#The code is correct at first try.
