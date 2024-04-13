# Усе проходить
def sort_array(source_array):
    odd_numbers = sorted((num for num in source_array if num % 2 != 0), reverse=False)
    
    # Replace the odd numbers in the original array with the sorted ones
    result = [odd_numbers.pop(0) if num % 2 != 0 else num for num in source_array]
    
    return result
