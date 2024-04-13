# Код GPT був некоректний, вручну змінила варіант return, бо повертались дані в [], а не ()
# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
def two_sum(nums, target):
    # Create a dictionary to store the indices of numbers as we iterate through the array
    num_indices = {}
    
    # Iterate through the array
    for i, num in enumerate(nums):
        # Calculate the complement needed to reach the target
        complement = target - num
        
        # Check if the complement exists in the dictionary
        if complement in num_indices:
            # If found, return the indices of the two numbers
            return (num_indices[complement], i)
        
        # Add the current number and its index to the dictionary
        num_indices[num] = i
    
    # If no solution is found, return None
    return None
