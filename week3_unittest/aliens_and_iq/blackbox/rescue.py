# Problem:https://cms.ucu.edu.ua/mod/vpl/forms/submissionview.php?id=306723&userid=9849
# My version of the code(it does not pass 5 last tests)
'''The module'''
def read_file(file_path):
    '''
    str -> dict
    Read the file at file_path and return a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].strip()) for line in file if len(line.split(',')) == 2}
def rescue_people(smarties, limit_iq):
    '''
    (dict, int) -> tuple
    Returns the number of required trips and a list of lists representing each trip.
    '''
    trips = []
    remaining_iq = limit_iq
    if not smarties:
        return 0, trips
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    sorted_smarties = sorted(smarties.items(), key=lambda x: x[1], reverse=True)
    while sorted_smarties:
        trip = []
        for name, iq in sorted_smarties[:]:
            if iq <= remaining_iq:
                trip.append(name)
                remaining_iq -= iq
                sorted_smarties.remove((name, iq))
        trips.append(trip)
        remaining_iq = limit_iq
    return len(trips), trips

# Request1:
# Please, write me unittests for this task:
#(here is the full condition for the task)

# Blackbox's answer:
import unittest
def setUpModule():
    global smart_people_txt
    smart_people_txt = """\
Steve Jobs: 160
Albert Einstein: 160
Sir Isaac Newton: 195
Nikola Tesla: 189"""
class TestBlackboxAI(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file('smart_people.txt'),
                         {"Steve Jobs": 160, "Albert Einstein": 160,
                          "Sir Isaac Newton": 195, "Nikola Tesla": 189})
    def test_rescue_people(self):
        smarties = {"Steve Jobs": 160, "Albert Einstein": 160,
                    "Sir Isaac Newton": 195, "Nikola Tesla": 189}
        self.assertEqual(rescue_people(smarties, 500), (2, [["Sir Isaac Newton", "Nikola Tesla"],
                                                            ["Albert Einstein", "Steve Jobs"]]))
        self.assertEqual(rescue_people(smarties, 600), (1, [["Steve Jobs", "Albert Einstein",
                                                            "Sir Isaac Newton", "Nikola Tesla"]]))
        self.assertEqual(rescue_people({}, 500), (0, []))
if __name__ == '__main__':
    unittest.main(module=__name__, exit=False)

# Request2:
# This tests are really great but this one is incorrect 
# self.assertEqual(rescue_people(smarties, 600), (1, [["Steve Jobs", "Albert Einstein","Sir Isaac Newton", "Nikola Tesla"]])) 
# because the sum of IQ of this people is 704 and you wrote that maximum limit of IQ is 600, so they can not be in on race

# Blackbox's answer:
self.assertEqual(rescue_people(smarties, 600), (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Steve Jobs", "Albert Einstein"]]))

# Request3:
# You again made a mistake because our maximum iq limit is 600 we add to first race 'Sir Isaac Newton', 'Nikola Tesla'
# and their summary IQ is 384, so we can add also one more person to this race because we still have 216 free IQ places

# Blackbox's answer:
# (Blackbox just tried to change his own code)

# Request4:
# No, i do not need to change code I need you to change this assert 
# self.assertEqual(rescue_people(smarties, 600), (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Steve Jobs", "Albert Einstein"]])) 
# with one more person in first race

# Blackbox's answer:
assert rescue_people(smarties, 600) == (2, [["Sir Isaac Newton", "Nikola Tesla", "Steve Jobs"], ["Albert Einstein"]])

# Request5:
# Oh, it is great but you forgot about this condition:
# Якщо люди мають однаковий рівень IQ, то порядок вибору у лексикографічному порядку за іменем,
# so we can not chose first "Steve Jobs" because a is the first letter of alphabet

# Blackbox's answer:
assert rescue_people(smarties, 600) == (2, [["Nikola Tesla", "Sir Isaac Newton", "Steve Jobs"], ["Albert Einstein"]])

# Request6:
# No you did not get me you chose between "Steve Jobs" and "Albert Einstein" and they have the same IQ,
# so you need to sort them by alphabet and chose to first race that person who is first through alphabet


# Blackbox's answer:
assert rescue_people(smarties, 600) == (2, [["Nikola Tesla", "Sir Isaac Newton", "Albert Einstein"], ["Steve Jobs"]])

# Request7:
# Great but make it as unittest not assert

# Blackbox's answer:
result = rescue_people(smarties, 600)
self.assertEqual(result, (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]]))

# Request8:
# No, I mean that make from this assert a unittest 
# assert rescue_people(smarties, 600) == (2, [["Nikola Tesla", "Sir Isaac Newton", "Albert Einstein"], ["Steve Jobs"]])

# Blackbox's answer:
result = rescue_people(smarties, 600)
self.assertEqual(result, (2, [["Nikola Tesla", "Sir Isaac Newton", "Albert Einstein"], ["Steve Jobs"]]))

# Request9:
# Great, but you need firstly sort people by IQ and if their IQ is equal by alphabet

# Blackbox's answer:
assert rescue_people(smarties, 600) == (2, [["Nikola Tesla", "Sir Isaac Newton", "Albert Einstein"], ["Steve Jobs"]])

# Request10:
# No, you still made the same assert but Issac Newton has bigger IQ than Tesla

# Blackbox's answer:
self.assertEqual(rescue_people(smarties, 600), (2, [["Sir Isaac Newton", "Nikola Tesla", "Albert Einstein"], ["Steve Jobs"]]))

# Hurray, blackbox already made correct tests, and I got this error:
# ======================================================================
# FAIL: test_rescue_people (__main__.TestBlackboxAI)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_rescue.py", line 25, in test_rescue_people
#     self.assertEqual(rescue_people(smarties, 500), (2, [["Sir Isaac Newton", "Nikola Tesla"],
# AssertionError: Tuples differ: (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']]) != (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])

# First differing element 1:
# [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']]
# [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']]

# - (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']])
# ?                                             --------------

# + (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
# ?                                                              ++++++++++++++


# ----------------------------------------------------------------------
# Ran 2 tests in 0.000s

# FAILED (failures=1)

# So, I managed to find my mistace, I made wrong algorithm for sorting dictionary by alphabet.

# Finally, the correct code:
'''The module'''
def read_file(file_path):
    '''
    str->dict
    The function takes the path to the corresponding file 
    and returns a dictionary.
    '''
    with open(file_path, 'r', encoding='utf-8') as file:
        return {line.split(',')[0]: int(line.split(',')[1].\
strip()) for line in file if len(line.split(',')) == 2}
def rescue_people(smarties, limit_iq):
    '''
    (dict,int)->tuple
    The function returns a tuple of the number of required trips and a list of lists,
    where each inner list represents a trip and contains the names of the people 
    transported on that trip in the order in which they were chosen by the aliens.
    >>> rescue_people({"Albert Einstein": 160, "Sir Isaac Newton": 195, "Nikola Tesla": 189},500)
    (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein']])
    '''
    smarties = {name: iq for name, iq in smarties.items() if iq >= 130}
    if not smarties:
        return 0, []
    smarties = dict(sorted(smarties.items(), key=lambda x: (-x[1], x[0])))
    lst2 = []
    while smarties:
        lst1 = []
        remaining_iq = limit_iq
        for key, value in smarties.items():
            if value <= remaining_iq:
                lst1.append(key)
                remaining_iq -= value
        lst2.append(lst1)
        smarties = {key: value for key, value in smarties.items() if key not in lst1}
    count = len(lst2)
    return count, lst2

# And the correct unittests, which cover all code:
import unittest
from rescue import read_file
from rescue import rescue_people
def setUpModule():
    global smart_people_txt
    smart_people_txt = """\
Steve Jobs: 160
Albert Einstein: 160
Sir Isaac Newton: 195
Nikola Tesla: 189"""
class TestBlackboxAI(unittest.TestCase):
    def test_read_file(self):
        self.assertEqual(read_file('smart_people.txt'),
                         {"Steve Jobs": 160, "Albert Einstein": 160,
                          "Sir Isaac Newton": 195, "Nikola Tesla": 189})
    def test_rescue_people(self):
        smarties = {"Steve Jobs": 160, "Albert Einstein": 160,
                    "Sir Isaac Newton": 195, "Nikola Tesla": 189}
        self.assertEqual(rescue_people(smarties, 500), (2, [["Sir Isaac Newton", "Nikola Tesla"],
                                                            ["Albert Einstein", "Steve Jobs"]]))
        self.assertEqual(rescue_people({}, 500), (0, []))
        self.assertEqual(rescue_people(smarties, 600), (2, [["Sir Isaac Newton", "Nikola Tesla", "Albert Einstein"],
                                                             ["Steve Jobs"]]))
if __name__ == '__main__':
    unittest.main(module=__name__, exit=False)
