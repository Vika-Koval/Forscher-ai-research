# Не проходить жоден тест
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
            return [num_indices[complement], i]
        
        # Add the current number and its index to the dictionary
        num_indices[num] = i
    
    # If no solution is found, return None or an appropriate message
    return None

# Example usage:
print(two_sum([1, 2, 3], 4))  # Output: [0, 2] or [2, 0]
print(two_sum([3, 2, 4], 6))  # Output: [1, 2] or [2, 1]
