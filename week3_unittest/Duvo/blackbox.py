# https://cms.ucu.edu.ua/mod/vpl/view.php?id=306599&userid=10167
# My version of the code
def dyvo_insert(sentence:str, flag:str):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert('Кит кота по хвилях катав - кит у воді, кіт на киті.', 'ки')
        Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті.
    >>> dyvo_insert('Пилип прилип, прилип Пилип. Пилип плаче. Пилип посіяв просо, просо поспіло, пташки прилетіли, просо поїли.', 'пи')
        Дивопилип прилип, прилип Дивопилип. Дивопилип плаче. Дивопилип посіяв просо, просо поспіло, пташки прилетіли, просо поїли.
   
    """
    c = 0
    re = ''
    between = sentence.lower()
    n = between.count(flag)
    for i in range(n):
        index = between.index(flag)
        c += index
        if sentence[c].isupper():
            rez = between[0:(index+3)].replace(flag, 'Диво' + flag)
            re=re + rez
        else:
            rez = between[0:(index+3)].replace(flag, 'диво' + flag)
            re=re + rez
        between = between[(index+3)::]
    re=re + sentence[len(between):]
    return re

# Request1:
# Please, write me unittests for this task:
#(here is the full condition for the task)

# Blackbox's answer and the correct unittests(Blackbox managed to do it from first time, I am shocked):
import unittest
from dyvo import dyvo_insert
class TestDyvoInsert(unittest.TestCase):
    def test_basic(self):
        sentence = "Кит кота по хвилях катав - кит у воді, кіт на киті"
        result = dyvo_insert(sentence, "ки")
        expected = "Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті"
        self.assertEqual(result, expected)
    def test_no_matches(self):
        sentence = "no matches here"
        result = dyvo_insert(sentence, "ki")
        expected = "no matches here"
        self.assertEqual(result, expected)
    def test_flag_at_beginning(self):
        sentence = "кит кота по хвилях катав - кит у воді, кіт на киті"
        result = dyvo_insert(sentence, "ки")
        expected = "дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті"
        self.assertEqual(result, expected)
    def test_flag_in_middle(self):
        sentence = "Кот кита по хвилях катав - кит у воді, кіт на киті"
        result = dyvo_insert(sentence, "ки")
        expected = "Кот дивокита по хвилях катав - дивокит у воді, кіт на дивокиті"
        self.assertEqual(result, expected)
    def test_flag_at_end(self):
        sentence = "кота кита по хвилях катав - кит у воді, кіт на киті"
        result = dyvo_insert(sentence, "ки")
        expected = "кота дивокита по хвилях катав - дивокит у воді, кіт на дивокиті"
        self.assertEqual(result, expected)
    def test_none(self):
        sentence = "кота кита по хвилях катав - кит у воді, кіт на киті"
        result = dyvo_insert(sentence, 34)
        expected = None
        self.assertEqual(result, expected)
if __name__ == "__main__":
    unittest.main()

# I got this errors after running my code:

# ======================================================================
# FAIL: test_basic (__main__.TestDyvoInsert)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_dyvo.py", line 23, in test_basic
#     self.assertEqual(result, expected)
# AssertionError: 'Диво[44 chars]іт на дивокитит кота по хвилях катав - кит у воді, кіт на киті' != 'Диво[44 chars]іт на дивокиті'
# - Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокитит кота по хвилях катав - кит у воді, кіт на киті
# + Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті


# ======================================================================
# FAIL: test_flag_at_beginning (__main__.TestDyvoInsert)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_dyvo.py", line 35, in test_flag_at_beginning
#     self.assertEqual(result, expected)
# AssertionError: 'диво[44 chars]іт на дивокитит кота по хвилях катав - кит у воді, кіт на киті' != 'диво[44 chars]іт на дивокиті'
# - дивокит кота по хвилях катав - дивокит у воді, кіт на дивокитит кота по хвилях катав - кит у воді, кіт на киті
# + дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті


# ======================================================================
# FAIL: test_flag_at_end (__main__.TestDyvoInsert)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_dyvo.py", line 47, in test_flag_at_end
#     self.assertEqual(result, expected)
# AssertionError: 'кота[46 chars]т на дивокитота кита по хвилях катав - кит у воді, кіт на киті' != 'кота[46 chars]т на дивокиті'
# - кота дивокита по хвилях катав - дивокит у воді, кіт на дивокитота кита по хвилях катав - кит у воді, кіт на киті
# + кота дивокита по хвилях катав - дивокит у воді, кіт на дивокиті


# ======================================================================
# FAIL: test_flag_in_middle (__main__.TestDyvoInsert)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_dyvo.py", line 41, in test_flag_in_middle
#     self.assertEqual(result, expected)
# AssertionError: 'кот [44 chars]іт на дивокитот кита по хвилях катав - кит у воді, кіт на киті' != 'кот [44 chars]іт на дивокиті'
# - кот дивокита по хвилях катав - дивокит у воді, кіт на дивокитот кита по хвилях катав - кит у воді, кіт на киті
# + кот дивокита по хвилях катав - дивокит у воді, кіт на дивокиті


# ======================================================================
# FAIL: test_no_matches (__main__.TestDyvoInsert)
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File "/home/vika/Desktop/op/test_dyvo.py", line 29, in test_no_matches
#     self.assertEqual(result, expected)
# AssertionError: '' != 'no matches here'
# + no matches here

# ----------------------------------------------------------------------
# Ran 5 tests in 0.001s

# I found my mistake and fixed my code

# Finally, the correct code:
'''The module inserts word "диво" before every word that starts with flag.'''
def dyvo_insert(sentence, flag):
    """
    (str, str) -> str
    Inserting word "диво" before every word that starts with flag.
    >>> dyvo_insert("кит", "ки")
    'дивокит'
    >>> dyvo_insert("Кит кота по хвилях катав - кит у воді, кіт на киті.", "ки")
    'Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті.'
    >>> dyvo_insert("Босий хлопець сіно косить, роса росить ноги босі.", "сі")
    'Босий хлопець дивосіно косить, роса росить ноги босі.'
    """
    v=[]
    lowercase='абвгґдеєжзиіїйклмнопрстуфхцчшщьюя'
    uppercase='АБВГҐДЕЄЖЗІЇЙКЛМНОПРСТУФХЦЧШЩЮЯ'
    if isinstance(sentence,str) and isinstance(flag,str):
        l1=sentence.split()
        for i in range(0,len(l1)):
            w=l1[i]
            l2=list(w)
            if l2[0] in lowercase:
                if len(w) >=len(flag):
                    l3=l2[:len(flag)]
                    s1= ''.join(l3)
                    if s1==flag:
                        s2=f"диво{w}"
                        v.append(s2)
                    else:
                        v.append(w)
                else:
                    v.append(w)

            elif l2[0] in uppercase:
                if len(w) >=len(flag):
                    l3=l2[:len(flag)]
                    s1= ''.join(l3)
                    s1=s1.lower()
                    if s1==flag:
                        w=w.lower()
                        s2=f"Диво{w}"
                        v.append(s2)
                    else:
                        v.append(w)
            else:
                v.append(w)
        k1= ' '.join(v)
        return k1
    return None
