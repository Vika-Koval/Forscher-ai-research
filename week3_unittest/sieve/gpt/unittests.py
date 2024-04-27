#requst1:
#write unittest for the task 
# at this point chat gpt wrote sth complitely wrong

#request2:
# напиши юніттести для цієї задачі:
# surprisingly, when we wrote everything in one language, chat gpt's tests started to make sense
# however, we got asserts instead of unittests

#request3:
#change asserts into unittests
# we received unittests

# after fixing the code, so all the tests would pass, tests on cms pass as well. 

from improved_sieve import sieve_flavius
import unittest
from unittest import TestCase

class TestSieveFlavius(TestCase):
    def test_sieve_flavius_25(self):
        expected_output_25 = [1, 3, 7, 9, 13, 15, 21, 25]
        self.assertEqual(sieve_flavius(25), expected_output_25, f"Expected {expected_output_25}, but got {sieve_flavius(25)}")

    def test_sieve_flavius_50(self):
        expected_output_50 = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49]
        self.assertEqual(sieve_flavius(50), expected_output_50, f"Expected {expected_output_50}, but got {sieve_flavius(50)}")

    def test_sieve_flavius_100(self):
        expected_output_100 = [1, 3, 7, 9, 13, 15, 21, 25, 31, 33, 37, 43, 49, 51, 63, 67, 69, 73, 75, 79, 87, 93, 99]
        self.assertEqual(sieve_flavius(100), expected_output_100, f"Expected {expected_output_100}, but got {sieve_flavius(100)}")

if __name__ == '__main__':
    unittest.main(verbosity=2)
