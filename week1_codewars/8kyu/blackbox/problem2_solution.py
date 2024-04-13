#Problem: https://www.codewars.com/kata/57a2013acf1fa5bfc4000921/train/python

#Request 1:
# Write a function which calculates the average of the numbers in a given list.

#Response:
def calculate_average(numbers):
    return sum(numbers) / len(numbers)

#Request 2:
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

#Response:
def calculate_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

#Request 3:
# Write a function which calculates the average of the numbers in a given list.

# Note: Empty arrays should return 0.

# These tests should pass: test.assert_equals(find_average([1, 2, 3]), 2, "Failed for [1, 2, 3]")
# test.assert_equals(find_average([]), 0, "Failed for []") 
# test.assert_approx_equals(find_average([1, 2]), 1.5, margin=1e-3, message="Failed for [1, 2]")

#Response:
def find_average(numbers):
    if not numbers:
        return 0
    return sum(numbers) / len(numbers)

#there was also a bunch of code that tested various examples, not important enough though
#as this AI just steals code from github, codewars etc, it can "solve" a lot of problems easily
#however, its first attempt at solving this problem was unsuccessful either because it didn't think
#about the possibility of the list being empty or because the code it stole didn't take that into account
#so the most usable code is probably the one it sent me on its second try
