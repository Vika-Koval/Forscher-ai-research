#Problem: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

#Request 1:
# Hi. Solve this in Python:
# Write a function which calculates the average of the numbers in a given list.

#Response:
def calculate_average(num_list):
    if len(num_list) == 0:
        return 0  # Avoid division by zero if the list is empty
    else:
        return sum(num_list) / len(num_list)

#AI understood the problem perfectly from the first try without any examples
