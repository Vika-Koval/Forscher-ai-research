#requst1:
#write unittest for the task 
# at this point chat gpt wrote sth complitely wrong

#request2:
#reread the task
#after several attempts, nothing still makes sense.
# it is clerly visible that the test are not correct.


#Request3:
# I clearly explained the algorithm of the task to chat gpt
# still everything is wrong


#Request4:
#explain the logic for self.assertTrue(happy_number(12300678))
# turned out, chat gpt thought 3 == 6,

#Request5:
#but 3!= 6
# Chat gpt wrote I'm right,but still didn't change the asserts

#it was easier to count everythin myself, and after lots of explanations chat gpt 
#managed to change the unittests to the ones I told are correct
#but of course, that did not help at all, since the tests were working for my code.
# I had to actually send chat gpt the parts of the code I was sure are correct,
# only than better testcases appeared.
# since at the beginning, the code was almost working, only small change was required,
#and somehow, chat gpt hepled with it.
# but in case of this task, it is easier to do it on your own, than with chat gpt,
# since chat gpt does not understand the algorithm and makes mistakes in simple calculations
from improved_happy import happy_number, happy_numbers, count_happy_numbers
import unittest

class TestHappyModule(unittest.TestCase):
    
    def test_happy_number(self):
        # Перевірка для "щасливих" квитків
        self.assertFalse(happy_number(12300678))
        self.assertFalse(happy_number(45678901))
        # Перевірка для "несчасливих" квитків
        self.assertFalse(happy_number(12340000))
        self.assertFalse(happy_number(98765432))
        self.assertTrue(happy_number(32100123))
        self.assertTrue(happy_number(159123))
        self.assertFalse(happy_number(1234))
        self.assertFalse(happy_number(12340000))
    
    def test_count_happy_numbers(self):
        # Перевірка підрахунку "щасливих" квитків
        self.assertEqual(count_happy_numbers(100), 0)
        self.assertEqual(count_happy_numbers(10001), 1)
        self.assertEqual(count_happy_numbers(100000), 9999)
        self.assertEqual(count_happy_numbers(1), 0)

    def test_happy_numbers(self):
        # Перевірка списку "щасливих" квитків у діапазоні
        self.assertEqual(happy_numbers(1, 100), [])
        self.assertEqual(happy_numbers(10001, 10010), [10001, 10010])
        self.assertEqual(happy_numbers(1, 3), [])


if __name__ == '__main__':
    unittest.main()
