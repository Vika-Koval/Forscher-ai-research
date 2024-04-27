"""
These functions say if the number or list of numbers is happy.
"""
def happy_number(number: int) -> bool:
    """
    This function returns True if the number is happy.
    >>> happy_number(1234)
    False
    >>> happy_number(32100123)
    True
    >>> happy_number(159123)
    True
    """
    result = None
    number = str(number)
    if len(number)<8:
        number = '0'*(8-len(number)) + number
    num1 = 0
    num2 = 0
    for num in number[:4]:
        num1 += int(num)
    for num in number[4:]:
        num2 += int(num)
    suma = 10
    while len(str(suma))!= 1:
        suma = 0
        num1 = str(num1)
        for nnn in num1:
            suma += int(nnn)
        num1 =str(suma)
        if len(num1) == 1 and num1!=0:
            break
    suma = 10
    while len(str(suma))!= 1:
        suma = 0
        num2 = str(num2)
        for nnn in num2:
            suma += int(nnn)
        num2 = str(suma)
        if len(num2) == 1 and num2!=0:
            break
    if num1==num2:
        result = True
    if num1!=num2:
        result = False
    return result

def count_happy_numbers(max_number: int) -> int:
    """
    This function returns the amount of all happy numbers lower than certain number. 
    >>> count_happy_numbers(10001)
    1
    >>> count_happy_numbers(100000)
    9999
    """
    count = 0
    for num in range(1, max_number +1):
        if happy_number(num) is True:
            count += 1
    return count

def happy_numbers(min_num: int, max_num: int) -> list:
    """
    This function returns a list of all happy numbers in certain range
    >>> happy_numbers(10001, 10010)
    [10001, 10010]
    >>> happy_numbers(1, 3)
    []
    """
    result = []
    if max_num >= min_num:
        for i in range(min_num, max_num+1):
            if happy_number(i) is True:
                result.append(i)
    return result

