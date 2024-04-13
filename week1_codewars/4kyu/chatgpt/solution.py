# Problem: https://www.codewars.com/kata/56b2abae51646a143400001d/train/python


# Request1:
#  Hepl to write this task in python: The mystery function is defined over the non-negative integers
#Assume n has m bits. Then mystery(n) is the number whose binary representation \
#is the entry in the table T(m) at index position n, where T(m) is defined recursively as follows:
#T(1) = [0, 1]
#T(m + 1) is obtained by taking two copies of T(m), reversing the second copy, \
#prepending each entry of the first copy with 0 and each entry of the reversed copy with 1, and then concatenating the two.
#Your mission is to implement the function mystery, where the argument may have up to 63 bits. 
#You are also asked to implement mystery_inv, the inverse of mystery. 
# Finally, you are asked to implement a function name_of_mystery, 
#which shall return the name that mystery is more commonly known as.##

# GPT's answer:
def mystery(n):
    result = 0
    power_of_two = 1
    while n > 0:
        if n % 2 == 1:
            result += power_of_two
        power_of_two *= 2
        n //= 2
    return result

def mystery_inv(k):
    n = 0
    while k > 0:
        n += 1
        if k % 2 == 1:
            k -= 1
        k //= 2
    return n

def name_of_mystery():
    return "Gray code"
#This code only passed 4 tests;
# Chat GPT realised that the mystery is "Gray code"




# Request2:
#This code only works for 0 and 1, correct it, so it could work with other numbers

# GPT's answer:
def mystery(n):
    m = 1
    while m * 2 <= n:
        m *= 2
    return (n - m) * 2 + 1

def mystery_inv(k):
    n = 1
    while k > 1:
        k = (k - 1) // 2
        n *= 2
    return n
#Nothing really changed after this request, 1 5 tests passed



# Request3:
# Great, but it should work with all numbers.
#Test examples: mystery_inv(5): 4 should equal 6
#mystery(9) : 3 should equal 13
#mystery_inv(13): 8 should equal 9
#mystery(19) : 7 should equal 26
#mystery_inv(26): 16 should equal 19

# GPT's answer:
def mystery(n):
    m = 1
    while m * 2 <= n:
        m *= 2
    return (n - m) * 2 + 1

def mystery_inv(k):
    n = 1
    while k > 1:
        k -= 1
        n *= 2
    return n
#this code didn't work



# Request4:
#Unfortunelely, there is a time out, rewrite the code from scratch

# GPT's answer:
def mystery(n):
    result = 0
    power_of_two = 1
    while n > 0:
        if n % 2 == 1:
            result ^= power_of_two
        power_of_two <<= 1
        n >>= 1
    return result

def mystery_inv(k):
    n = 0
    while k > 0:
        k >>= 1
        n += 1
    return 1 << (n - 1)
#only 6 tests passed after this attempt



# Request5:
#Maybe an example of bigger numbers could help
# mystery(1495868364746886208) =  2207703312395291232

# GPT's answer:
def mystery(n):
    result = 0
    power_of_two = 1
    while n > 0:
        if n & 1:  # Check if the least significant bit is set
            result ^= power_of_two
        power_of_two <<= 1
        n >>= 1
    return result

def mystery_inv(k):
    n = 0
    while k > 0:
        k >>= 1
        n += 1
    return 1 << (n - 1)
# The improvements didn't change anything



# Request6:
# nothing changed, it seems you understood the task a bit wrong

# GPT's answer:
def mystery(n):
    if n == 0:
        return 0
    else:
        return (n ^ (n >> 1))

def mystery_inv(k):
    n = 0
    while k > 0:
        k >>= 1
        n += 1
    return (1 << n) - 1
# All tests for mystery function passed after this attempt, so now we will work only with mystery inversion



# Request7:
# That's way better! Mystery function is correct, but we still need to fix mystery inversion.
# More examples: 
# mystery_inv(612) = 952, 
#mystery_inv(112) =  95, 
#mystery_inv(664) = 784, 
#mystery_inv(26) = 19 

# GPT's answer:
def mystery_inv(k):
    n = 1
    while k > n:
        k >>= 1
        n = (n << 1) + 1
    return (n - k)
#nothing changed after this attempt




# Request8:
# That's way better! Mystery function is correct, but we still need to fix mystery inversion.
# More examples: 
# mystery_inv(612) = 952, 
#mystery_inv(112) =  95, 
#mystery_inv(664) = 784, 
#mystery_inv(26) = 19 

# GPT's answer:
def mystery_inv(k):
    n = 0
    while k > 1:
        n = ((n + 1) << 1) - (k & 1)
        k >>= 1
    return n
# 1 more test passed




# Request9:
#That's bettter, some examples for bigger numbers:
#mystery_inv(958) = 724
#mystery_inv(920) = 751
#mystery_inv(544) =960
#mystery_inv(883) = 605

# GPT's answer:
def mystery_inv(k):
    n = 0
    while k > 0:
        n = (n << 1) | (k & 1)
        k >>= 1
    return n
# mystery_inv doesn't work with this code




# Request10:
#think about separating different cases

# GPT's answer:
def mystery_inv(k):
    if k == 0:
        return 0
    n = 1
    while k > 0:
        n = (n << 1) | (k & 1)
        k >>= 1
    return n
# This code didn't improve anything






# Request11:
# mystery_inv function does not work properly, find regularity in the given examples, 
#create new ideas to improve the code

# GPT's answer:
def mystery_inv(k):
    if k == 0:
        return 0

    n = 1
    result = 0
    while k > 1:
        # Shift n to the left and add the least significant bit of k
        result |= n * (k & 1)
        # Remove the least significant bit of k
        k >>= 1
        # Double the value of n
        n <<= 1

    # At this point, k is 1, so we just need to add the current value of n
    result |= n

    return result
# this code didn't improve anything



# Request12:
#Think what might be wrong with the code

# GPT's answer:
def mystery_inv(k):
    if k == 0:
        return 0
    
    # Find the length m of the binary representation of k
    m = k.bit_length()

    # Initialize the result
    result = 0
    
    # Reconstruct the binary representation of n
    for i in range(m):
        if k & (1 << i):
            result |= (1 << (m - i - 1))

    return result
#nothing changed after this attempt


# Request13:
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

# GPT's answer:
def mystery_inv(k):
    n = 0
    while k:
        n ^= k
        k >>= 1
    return n

#Finally, everything is correct!




#Full code:
def mystery(n):
    if n == 0:
        return 0
    else:
        return (n ^ (n >> 1))

def mystery_inv(k):
    n = 0
    while k:
        n ^= k
        k >>= 1
    return n

def name_of_mystery():
    return "Gray code"

#Conclusion:
# Chat GPT was able to do the task of 4th level, but it was not easy.
# The description and few examples are not enough for a task of this level.
# The first half of the task was done without any serious issues,
# But chat GPT was barely capable of doing the second half.
# Only an extremely large amount of examples made the code work properly.
