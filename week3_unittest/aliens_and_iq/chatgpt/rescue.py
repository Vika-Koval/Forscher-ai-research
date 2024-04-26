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

# GPT's answer:
import unittest
from rescue import read_file
from rescue import rescue_people
class TestRescuePeople(unittest.TestCase):
    def test_empty_input(self):
        # Test case for empty input file
        smarties = {}
        limit_iq = 500
        expected_result = (0, [])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_single_trip(self):
        # Test case for a single trip
        smarties = {"Sir Isaac Newton": 195, "Nikola Tesla": 189}
        limit_iq = 500
        expected_result = (1, [["Sir Isaac Newton", "Nikola Tesla"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_multiple_trips(self):
        # Test case for multiple trips
        smarties = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        limit_iq = 500
        expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        # Test case for reading file
        file_path = "test_smart_people.txt"
        expected_result = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        self.assertEqual(read_file(file_path), expected_result)
if __name__ == '__main__':
    unittest.main()
# This tests were good, but they did not covered all condition

# Request2:
# You forget to add tests for this condition:
# Для другої поїздки прибульці оберуть комбінацію з тих, що лишився у лексикографічному порядку ["Albert Einstein", "Steve Jobs"].

# GPT's answer:
import unittest
from rescue import read_file
from rescue import rescue_people
class TestRescuePeople(unittest.TestCase):
    def test_empty_input(self):
        # Test case for empty input file
        smarties = {}
        limit_iq = 500
        expected_result = (0, [])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_single_trip(self):
        # Test case for a single trip
        smarties = {"Sir Isaac Newton": 195, "Nikola Tesla": 189}
        limit_iq = 500
        expected_result = (1, [["Sir Isaac Newton", "Nikola Tesla"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_multiple_trips(self):
        # Test case for multiple trips
        smarties = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        limit_iq = 500
        expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_lexicographical_order(self):
        # Test case for lexicographical order in the second trip
        smarties = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        limit_iq = 500
        expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        # Test case for reading file
        file_path = "test_smart_people.txt"
        expected_result = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        self.assertEqual(read_file(file_path), expected_result)
if __name__ == '__main__':
    unittest.main()

# This tests already covered all function.
# After running tests I got this errors:

# ======================================================================
# FAIL: test_lexicographical_order (__main__.TestRescuePeople)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_rescue.py", line 41, in test_lexicographical_order
#     self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
# AssertionError: Tuples differ: (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']]) != (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])

# First differing element 1:
# [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']]
# [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']]

# - (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']])
# ?                                             --------------

# + (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
# ?                                                              ++++++++++++++


# ======================================================================
# FAIL: test_multiple_trips (__main__.TestRescuePeople)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_rescue.py", line 30, in test_multiple_trips
#     self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
# AssertionError: Tuples differ: (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']]) != (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])

# First differing element 1:
# [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']]
# [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']]

# - (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Steve Jobs', 'Albert Einstein']])
# ?                                             --------------

# + (2, [['Sir Isaac Newton', 'Nikola Tesla'], ['Albert Einstein', 'Steve Jobs']])
# ?                                                              ++++++++++++++


# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# FAILED (failures=2)

# So, I found where my solution was failing, I made wrong algorithm for sorting dictionary by alphabet.

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
class TestRescuePeople(unittest.TestCase):
    def test_empty_input(self):
        smarties = {}
        limit_iq = 500
        expected_result = (0, [])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_single_trip(self):
        smarties = {"Sir Isaac Newton": 195, "Nikola Tesla": 189}
        limit_iq = 500
        expected_result = (1, [["Sir Isaac Newton", "Nikola Tesla"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_multiple_trips(self):
        smarties = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        limit_iq = 500
        expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
    def test_lexicographical_order(self):
        smarties = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        limit_iq = 500
        expected_result = (2, [["Sir Isaac Newton", "Nikola Tesla"], ["Albert Einstein", "Steve Jobs"]])
        self.assertEqual(rescue_people(smarties, limit_iq), expected_result)
class TestReadFile(unittest.TestCase):
    def test_read_file(self):
        file_path = "test_smart_people.txt"
        expected_result = {
            "Steve Jobs": 160,
            "Albert Einstein": 160,
            "Sir Isaac Newton": 195,
            "Nikola Tesla": 189
        }
        self.assertEqual(read_file(file_path), expected_result)
if __name__ == '__main__':
    unittest.main()

