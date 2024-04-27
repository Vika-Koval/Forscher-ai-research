#Request1:
#write unittests for this task
# unittests don't make sense

#Requets2:
# added another part of task explanation(with examples)

# we got tests that helped to improve the code
#so, for Happy, the explanation is not clear enought foor AI and it needs some examples

import unittest
from improved_happy import happy_number, happy_numbers, count_happy_numbers

class TestHappyFunctions(unittest.TestCase):

    def test_happy_number(self):
        self.assertTrue(happy_number(43211234))
        self.assertFalse(happy_number(1))

    def test_count_happy_numbers(self):
        self.assertEqual(count_happy_numbers(10001), 1)
        self.assertEqual(count_happy_numbers(10100), 12)

    def test_happy_numbers(self):
        self.assertEqual(happy_numbers(10001, 10010), [10001, 10010])
        self.assertEqual(happy_numbers(1, 3), [])

if __name__ == '__main__':
    unittest.main()
