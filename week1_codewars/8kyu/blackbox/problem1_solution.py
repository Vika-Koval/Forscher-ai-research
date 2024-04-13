#Problem: https://www.codewars.com/kata/5583090cbe83f4fd8c000051/train/python

#Request 1:
#Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

#Response:
def convert_to_reversed_array(num):
    return [int(digit) for digit in str(num)[::-1]]
#As the code was usable from the first attempt and all the tests were passed,
#there was no point in changing the wording of the request. However, I did exactly
#that just to make sure.

#Request 2:
# Convert number to reversed array of digits
#Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output): 35231 => [1,3,2,5,3] 0 => [0]

#Response:
def convert_to_reversed_array(num):
    return [int(digit) for digit in str(num)[::-1]]

# Request 3:
# Convert number to reversed array of digits 
# Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

# Example(Input => Output): 35231 => [1,3,2,5,3] 0 => [0] 
# These tests should pass: test.assert_equals(digitize(35231),[1,3,2,5,3]) 
# test.assert_equals(digitize(0),[0]) 
# test.assert_equals(digitize(23582357),[7,5,3,2,8,5,3,2]) 
# test.assert_equals(digitize(984764738),[8,3,7,4,6,7,4,8,9]) 
# test.assert_equals(digitize(45762893920),[0,2,9,3,9,8,2,6,7,5,4]) 
# test.assert_equals(digitize(548702838394),[4,9,3,8,3,8,2,0,7,8,4,5])

#Response:
def digitize(n):
    return [int(digit) for digit in str(abs(n))[::-1]]

#on this try, the AI took the possibility of the number being negative into account and added an abs() to the function
#as it was said before, the first function worked perfectly, so did the later ones
