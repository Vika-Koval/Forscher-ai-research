# https://www.codewars.com/kata/52c31f8e6605bcc646000082/train/python
def sum_to_target(numbers, target):
    # First, we'll create a dictionary to store the indices of the numbers we've seen so far
    number_indices = {}
    
    # Next, we'll iterate over the numbers array
    for i, number in enumerate(numbers):
        # We'll calculate the difference between the target and the current number
        difference = target - number
        
        # If the difference is in our dictionary, that means we've seen a number before that, when added to the current number, gives us the target
        if difference in number_indices:
            # We'll return a tuple containing the indices of the two numbers
            return (number_indices[difference], i)
        else:
            # If the difference isn't in our dictionary, we'll add the current number and its index to the dictionary
            number_indices[number] = i
    
    # If we've made it through the entire array without finding two numbers that add up to the target, we'll return None
    return None
