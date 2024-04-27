#requst1:
#write unittest for the task:
# we received unittests, but blackbox understood some part of the tasks wrong
# also, instead of importing callable str was used

#request2:
# reread the task:
# we got correct unittsts, but our code passed all of them

#request2:
# make sure the coverage would be 100%. think about all possible cases
# we received unittests
# one of the tests was not passing
# it was about different length of 2 lists, so after adding this case to the code, it passes all tests on CMS.



import unittest
from improved_sort_songs import song_length, sort_songs, last_word, title_length
class TestSortSongs(unittest.TestCase):

    def setUp(self):
        self.song_titles = ['Янанебібув', 'Той день', 'Сосни', 'Кавачай', 'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд']
        self.length_songs = ['3.19', '3.58', '4.31', '4.39', '3.52', '4.24', '3.39', '3.43', '3.17', '2.21']
        self.sorted_songs_song_length = [('Етюд', '2.21'),  ('Коли тебе нема', '3.17'), ('Янанебібув', '3.19'), ('Поясни', '3.39'), ('Фіалки', '3.43'), ('Відпусти', '3.52'), ('Той день', '3.58'), ('Африка', '4.24'), ('Сосни', '4.31'), ('Кавачай', '4.39')]
        self.sorted_songs_title_length = [('Етюд', '2.21'),('Сосни', '4.31'), ('Африка', '4.24'), ('Поясни', '3.39'), ('Фіалки', '3.43'),  ('Кавачай', '4.39'), ('Той день', '3.58'), ('Відпусти', '3.52'), ('Янанебібув', '3.19'), ('Коли тебе нема', '3.17')]
        self.sorted_songs_last_word = [('Африка', '4.24'), ('Відпусти', '3.52'), ('Етюд', '2.21'), ('Кавачай', '4.39'), ('Поясни', '3.39'), ('Сосни', '4.31'), ('Фіалки', '3.43'), ('Янанебібув', '3.19'), ('Той день', '3.58'), ('Коли тебе нема', '3.17')]

    def test_sort_songs_song_length(self):
        result = sort_songs(self.song_titles, self.length_songs, song_length)
        self.assertEqual(result, self.sorted_songs_song_length)

    def test_sort_songs_title_length(self):
        result = sort_songs(self.song_titles, self.length_songs, title_length)
        self.assertEqual(result, self.sorted_songs_title_length)

    def test_sort_songs_last_word(self):
        result = sort_songs(self.song_titles, self.length_songs, last_word)
        self.assertEqual(result, self.sorted_songs_last_word)

    def test_sort_songs_different_length(self):
        short_song_titles = ['Янанебібув', 'Той день', 'Мало мені']
        short_length_songs = ['3.19', '3.58', '5.06']
        result = sort_songs(short_song_titles, short_length_songs, "song_length")
        self.assertIsNone(result)

    def test_sort_songs_different_type(self):
        wrong_length_songs = ['3.19', '5.06']
        result = sort_songs(self.song_titles, wrong_length_songs, song_length)
        self.assertIsNone(result)

if __name__ == '__main__':
    unittest.main()
