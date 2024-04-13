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

#Request 2:
# Now this:
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

#Response:
def calculate_average(num_list):
    if len(num_list) == 0:
        return 0  # Return 0 for an empty list
    else:
        return sum(num_list) / len(num_list)

#Request 3:
# And now this:
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.
# The following tests should pass:
#  test.assert_equals(find_average([1, 2, 3]), 2, "Failed for [1, 2, 3]")
#         test.assert_equals(find_average([]), 0, "Failed for []")
#         test.assert_approx_equals(find_average([1, 2]), 1.5, margin=1e-3, message="Failed for [1, 2]")

#Response:
def find_average(num_list):
    if len(num_list) == 0:
        return 0
    else:
        return sum(num_list) / len(num_list)

#literally nothing changed between the tries, so it seems like the AI understood the problem perfectly
#from the very beginning
