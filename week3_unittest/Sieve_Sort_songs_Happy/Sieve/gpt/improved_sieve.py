def sieve_flavius(number:int)->int:
    """
    This function generates a list of lucky numbers, smaller than the given number.
    """
    numbers = list(range(1,number+1))
    for num in numbers:
        if num%2==0:
            numbers.remove(num)
    for numb in range(1,len(numbers)-1):
        del_nums = []
        try:
            index = numbers[numb]
        except IndexError:
            break
        for i in range(index-1, len(numbers), index):
            del_nums.append(numbers[i])
        for k in numbers:
            if del_nums.count(k)>=1:
                numbers.remove(k)
    return numbers
