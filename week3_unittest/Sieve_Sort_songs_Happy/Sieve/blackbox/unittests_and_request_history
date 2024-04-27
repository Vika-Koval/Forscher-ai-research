#Request1:
#write unittest for the task 
# some unittest din't seem correct

#request2:
# some tests are not correct, think what might be wrong
# now unittests are better

#after fixing the code, so it would pass this tests, all tests at CMS pass


from improved_sieve import sieve_flavius
import unittest

class TestSieveFlavius(unittest.TestCase):
    def test_sieve_flavius_small_numbers(self):
        self.assertEqual(sieve_flavius(10), [1, 3, 7, 9])
        self.assertEqual(sieve_flavius(20), [1, 3, 7, 9, 13, 15])
        self.assertEqual(sieve_flavius(30), [1, 3, 7, 9, 13, 15, 21, 25])

  
if __name__ == '__main__':
    unittest.main(verbosity=2)
