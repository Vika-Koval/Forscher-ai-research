# https://cms.ucu.edu.ua/mod/vpl/view.php?id=306599&userid=10167
# Мій початковий код
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

# Промпт
# Привітик, дивись, у мене є задачка, нижче буде її текст

# Мені не потрібен код до неї, лише unittest до неї
# Подумай добре нед всіма можливими найпакоснішими варіантами, і пропиши всі corncase тести, і надішли мені

# Умова задачі:
# Розробити функцію dyvo_insert(sentence, flag) для додавання рядка у потрібну позицію іншого рядка. Наприклад, створіть змінну sentence і присвойте їй значення "Кит кота по хвилях катав - кит у воді, кіт на киті". Розроблена функція, повинна створити новий рядок, шляхом додавання рядка "диво", перед кожним зі слів, які починаються з "ки" (flag). Аргумент flag не чутливий до регістру речення. Результатом має бути стрічка "Дивокит кота по хвилях катав - дивокит у воді, кіт на дивокиті."
# Рішення потрібно знайти без використання операцій зі списками.

# Нагадую, мені не потрібен код розв'язку, лише unittest

import unittest
from your_module import dyvo_insert  # Підставте сюди ім'я вашого модуля та функції

class TestDyvoInsert(unittest.TestCase):
    def test_empty_string(self):
        result = dyvo_insert("", "ки")
        self.assertEqual(result, "")

    def test_no_words_starting_with_flag(self):
        result = dyvo_insert("Це тестовий рядок", "ки")
        self.assertEqual(result, "Це тестовий рядок")

    def test_empty_flag(self):
        result = dyvo_insert("Кит кота по хвилях катав", "")
        self.assertEqual(result, "Кит кота по хвилях катав")

    def test_words_with_similar_start(self):
        result = dyvo_insert("Кит кота по хвилях катав, китайці його дивилися", "ки")
        self.assertEqual(result, "Дивокит кота по хвилях катав, китайці його дивилися")

    def test_words_with_different_cases(self):
        result = dyvo_insert("КИт кота по хвилях катав", "ки")
        self.assertEqual(result, "Дивокит кота по хвилях катав")

    def test_words_separated_by_non_space_characters(self):
        result = dyvo_insert("Кит-кот кота по хвилях катав", "ки")
        self.assertEqual(result, "Дивокит-кот кота по хвилях катав")

    def test_large_input_data(self):
        sentence = " ".join(["Кит кота по хвилях катав"] * 1000)
        result = dyvo_insert(sentence, "ки")
        self.assertTrue("Дивокит" in result)  # Перевірка наявності декількох вставок
# У unittest я виявила помилку тому уточнила в gpt чи це є правильно
# def test_words_with_similar_start(self):
        # result = dyvo_insert("Кит кота по хвилях катав, китайці його дивилися", "ки")
        # self.assertEqual(result, "Дивокит кота по хвилях катав, китайці його дивилися")
# Gpt виправив свою помилку
def test_words_with_similar_start(self):
    result = dyvo_insert("Кит кота по хвилях катав, китайці його дивилися", "ки")
    self.assertEqual(result, "Дивокит кота по хвилях катав, дивокитайці його дивилися")
# Можеш перевірити мій код, і переправити його, аби він проходив ці asserts
if isinstance(sentence, str) and isinstance(flag, str):
        re = ''
        between = sentence.lower()
        n = between.count(flag.lower())  # Ensure case insensitivity
        index = 0
        for i in range(n):
            index = between.find(flag.lower(), index)  # Find next occurrence
            if sentence[index].isupper():
                rez = between[0:(index + len(flag))].replace(flag.lower(), 'Диво' + flag)
            else:
                rez = between[0:(index + len(flag))].replace(flag.lower(), 'диво' + flag)
            re += rez
            index += len(flag)  # Move index to next position
            between = between[(index)::]  # Update between for next iteration
        re += between  # Add remaining part after last occurrence
        return re
    else:
        return ""
# are you shoure it pass def test_empty_flag(self):
        # result = dyvo_insert("Кит кота по хвилях катав", "")
        # self.assertEqual(result, "Кит кота по хвилях катав")
if not isinstance(sentence, str) or not isinstance(flag, str):
        return ""
    if flag == "":
        return sentence  # Return input string unchanged for empty flag
    if isinstance(sentence, str) and isinstance(flag, str):
        re = ''
        between = sentence.lower()
        n = between.count(flag.lower())  # Ensure case insensitivity
        index = 0
        for _ in range(n):
            index = between.find(flag.lower(), index)  # Find next occurrence
            if sentence[index].isupper():
                rez = between[0:(index + len(flag))].replace(flag.lower(), 'Диво' + flag)
            else:
                rez = between[0:(index + len(flag))].replace(flag.lower(), 'диво' + flag)
            re += rez
            index += len(flag)  # Move index to next position
            between = between[(index)::]  # Update between for next iteration
        re += between  # Add remaining part after last occurrence
        return re
    else:
        return ""




