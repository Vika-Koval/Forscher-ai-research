# Problem: https://www.codewars.com/kata/56b2abae51646a143400001d/train/python


# Request1:
#  Help to write this task in python: The mystery function is defined over the non-negative integers
#Assume n has m bits. Then mystery(n) is the number whose binary representation
#is the entry in the table T(m) at index position n, where T(m) is defined recursively as follows:
#T(1) = [0, 1]
#T(m + 1) is obtained by taking two copies of T(m), reversing the second copy,
#prepending each entry of the first copy with 0 and each entry of the reversed copy with 1,
#and then concatenating the two.
#Your mission is to implement the function mystery, where the argument may have up to 63 bits.
#You are also asked to implement mystery_inv, the inverse of mystery.
# Finally, you are asked to implement a function name_of_mystery,
#which shall return the name that mystery is more commonly known as.

# Blackbox.ai's answer:
def mystery(n):
    return (n & 1) << (n.bit_length() - 1) | n >> 1
def mystery_inv(n):
    return (n << 1) | (n & 1)
def name_of_mystery():
    return "Gray code"
# name_of_mystery really is "Gray code"
# this code doesn't work, time out occurres



#Request2:
# The mystery and mystery_inv functions don't work, fix it

# Blackbox.ai's answer:
def mystery_inv(n):
    num = n
    shift = 0
    while num != 0:
        shift += 1
        num >>= 1
    result = n
    while shift != 0:
        shift -= 1
        result ^= result << shift
    return result
def mystery(n):
    if n == 0:
        return 0
    else:
        return (n ^ (n >> 1))
# after second attempt, all tests for mystery function passed



# Request3:
# That's way better! Mystery function is correct, but we still need to fix mystery inversion.
# More examples:
# mystery_inv(612) = 952,
#mystery_inv(112) =  95,
#mystery_inv(664) = 784,
#mystery_inv(26) = 19

# Blackbox.ai's answer:
def mystery_inv(n):
    if n == 0:
        return 0
    else:
        return (n >> 1) ^ n
# mystery_inv doesn't work properly with this code




# Request4:
#That's bettter, some examples for bigger numbers:
#mystery_inv(112) = 95 
#mystery_inv(465) = 353 
#mystery_inv(467) = 354 
#mystery_inv(361) = 433 
#mystery_inv(854) = 612 #mystery_inv(707) = 893 
#mystery_inv(251) = 173 #mystery_inv(528) = 992 
#mystery_inv(400) = 287 
#mystery_inv(470122877919647605) = 359121970357705305 
#mystery_inv(3778353360191015899) = 2861387101333917037 
#mystery_inv(2911524730926392109) = 3478292260854873545 
#mystery_inv(3878044520444438642) = 2782916013356142499 
#mystery_inv(3280096390030647016) = 3961430929726925647 
#mystery_inv(4501540649399093225) = 3147793576905407153 
#mystery_inv(741377403526524429) = 896573237782262793 
#mystery_inv(4193658947997069479) = 3180503479374356677 
#mystery_inv(502434893669474999) = 337208580278336730 
#mystery_inv(2892349842899668344) = 3475970302861511087

# Blackbox.ai's answer:
def mystery_inv(n):
    if n == 0:
        return 0
    else:
        return (n >> 1) ^ n
# the code didn't change




# Request5:
# think about another ways to solve it, make sure all provided tests pass

# Blackbox.ai's answer:
def mystery_inv(n):
    # Find the number of bits in n
    m = n.bit_length()

    # Initialize the first copy of T(m)
    first_copy = [0] * (1 << m)

    # Initialize the second copy of T(m)
    second_copy = [0] * (1 << m)
    for i in range(1 << m):
        second_copy[i] = first_copy[(1 << m) - i - 1]

    # Find the position of n in T(m)
    for i in range(1 << m):
        if first_copy[i] == n or second_copy[i] == n:
            return i
# This code is totally different, but it didn't improve anything






# Request6:
# mystery_inv function does not work properly, find regularity in the given examples,
#create new ideas to improve the code

# Blackbox.ai's answer:
def mystery_inv(n):
    return (n >> 1) ^ (n & 1)
# this code didn't improve anything either




# Request7:
# It seems like you don't understand what to do.
# Think about some new approaches.
# More examples, make sure they all pass:
# mystery_inv(12) = 8
# mystery_inv(51) = 34
# mystery_inv(375) =  421
# mystery_inv(140) = 247
#mystery_inv(112) = 95
#mystery_inv(465) = 353
#mystery_inv(467) = 354
#mystery_inv(361) = 433
#mystery_inv(854) = 612
#mystery_inv(707) = 893
#mystery_inv(251) = 173
#mystery_inv(528) = 992
#mystery_inv(400) = 287
#mystery_inv(470122877919647605) = 359121970357705305
#mystery_inv(3778353360191015899) = 2861387101333917037
#mystery_inv(2911524730926392109) = 3478292260854873545
#mystery_inv(3878044520444438642) = 2782916013356142499
#mystery_inv(3280096390030647016) = 3961430929726925647
#mystery_inv(4501540649399093225) = 3147793576905407153
#mystery_inv(741377403526524429) = 896573237782262793
#mystery_inv(4193658947997069479) = 3180503479374356677
#mystery_inv(502434893669474999) = 337208580278336730
#mystery_inv(2892349842899668344) = 3475970302861511087


# Blackbox.ai's answer:
def mystery_inv(n):
    if n == 0:
        return 0
    else:
        return (n ^ (n - 1)) >> 1
# Providing Blackbox.ai with examples didn't affect the result





# Request8:
# mystery_inv is an inversion of mystery function, 
# so think how to reverse mystery function


# Blackbox.ai's answer:
def mystery_inv(n):
    return n ^ (n >> 1)
# giving an explanation of fuction did not improve the code





# Request9:
# the code you provided is for mystery, not inversion, think about a new approach

# Blackbox.ai's answer:
def mystery_inv(n):
    if n == 0 or n == 1:
        return n
    else:
        return (mystery_inv(n & (n - 1)) << 1) | (n & 1)
# recursive function does not pass any tests





# Request10:
# You mention that the tests pass, but they don't. Improve mystery_inv

# Blackbox.ai's answer:
def mystery_inv(n):
    while n:
        n = n ^ (n >> 1)
    return n
# The logic of this code is almost correct, but Execution Timed Out occurred










# Request11:
# This code is better! But think about creating a new variable for result

# Blackbox.ai's answer:
def mystery_inv(n):
    result = 0
    while n:
        result ^= n
        n >>= 1
    return result
# Finally, after providing some clues, all tests passed








#Full code:
def mystery(n):
    if n == 0:
        return 0
    else:
        return (n ^ (n >> 1))
def mystery_inv(n):
    result = 0
    while n:
        result ^= n
        n >>= 1
    return result
def name_of_mystery():
    return "Gray code"


#Conclusion:
# Blackbox.ai was able to do the task of 4th level, but only after receiving some clues.
# The description and few examples are not enough for a task of this level.
# Even lots of examples didn't help Blackbox to write the code,
# The first half of the task was done without pretty quick,
# But lots pf problems occurred during the second half.
# This AI used different approaches to solve the task,
# but none of them passed even a few tests.
# Finally, one of the ideas was good,
# Blackbox.ai managed to rewrite it after one suggestion,
# And it passed all tests
# In general, this Ai can work with different ideas,
# but it can't find regularities in set of examples.

