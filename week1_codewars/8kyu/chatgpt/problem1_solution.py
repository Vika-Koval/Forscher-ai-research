#Problem: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

#Request 1:
#Hi. Solve this problem for me.
#Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

#Response:
def reverse_array(number):
    # Convert number to string
    num_str = str(number)
    # Split the string into a list of characters, reverse it, and convert back to integers
    reversed_array = [int(char) for char in num_str[::-1]]
    return reversed_array

#Request 2:
# Nice. Now this:
# Convert number to reversed array of digits
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output):
# 35231 => [1,3,2,5,3]
# 0 => [0]

# The tests provided next should be passed by the code (the test.assert_equals function is similar to the == operator):
         # test.assert_equals(digitize(35231),[1,3,2,5,3])
         # test.assert_equals(digitize(0),[0])
         # test.assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2])
         # test.assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9])
         # test.assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4])
         # test.assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])

#Response:
def digitize(number):
    # Special case: if the number is 0, return [0]
    if number == 0:
        return [0]
    # Convert number to string
    num_str = str(number)
    # Split the string into a list of characters, reverse it, and convert back to integers
    reversed_array = [int(char) for char in num_str[::-1]]
    return reversed_array


