#requst1:
#write unittest for the task:
# we received unittests, but chat gpt understood some part of the tasks wrong
# also, instead of importing callable str was used

#request2:
# reread the task:
# we got correct unittsts,but they were passing our code, and the coverage was not full
# since chat gpt didn't write tests for sort_songs

#request2:
# write tests for sort_songs:
# we received unittests
# one of the tests was not passing
# it was about invalif input, so after adding this case to the code, it passes all tests on CMS.



from improved_sort_songs import song_length, sort_songs, title_length, last_word
import unittest
from collections.abc import Callable
class TestSortSongs(unittest.TestCase):

    def test_song_length(self):
        songs = [('Song1', '3.19'), ('Song2', '4.31'), ('Song3', '2.58')]
        sorted_songs = sorted(songs, key=song_length)
        self.assertEqual(sorted_songs, [('Song3', '2.58'), ('Song1', '3.19'), ('Song2', '4.31')])

    def test_title_length(self):
        songs = [('Song1', '3.19'), ('Song2 Is Longer', '4.31'), ('Song3', '2.58')]
        sorted_songs = sorted(songs, key=title_length)
        self.assertEqual(sorted_songs, [('Song1', '3.19'), ('Song3', '2.58'), ('Song2 Is Longer', '4.31')])

    def test_last_word(self):
        songs = [('Song1', '3.19'), ('Song2 Longer', '4.31'), ('The Last Song', '2.58')]
        sorted_songs = sorted(songs, key=last_word)
        self.assertEqual(sorted_songs, [ ('Song2 Longer', '4.31'),('Song1', '3.19'), ('The Last Song', '2.58')])
    def test_sort_songs_invalid_input(self):
        song_titles = ['Song1', 'Song2 Longer', 'The Last Song']
        length_songs = ['3.19', '4.31', '2.58', 4.05]  # Неправильний вхідний формат
        self.assertIsNone(sort_songs(song_titles, length_songs, song_length))

    def test_sort_songs_song_length(self):
        song_titles = ['Song1', 'Song2 Longer', 'The Last Song']
        length_songs = ['3.19', '4.31', '2.58']
        expected_output = [('The Last Song', '2.58'), ('Song1', '3.19'), ('Song2 Longer', '4.31')]
        self.assertEqual(sort_songs(song_titles, length_songs, song_length), expected_output)

    def test_sort_songs_title_length(self):
        song_titles = ['Song1', 'Song2 Longer', 'The Last Song']
        length_songs = ['3.19', '4.31', '2.58']
        expected_output = [('Song1', '3.19'), ('Song2 Longer', '4.31'),('The Last Song', '2.58')]
        self.assertEqual(sort_songs(song_titles, length_songs, title_length), expected_output)

    def test_sort_songs_last_word(self):
        song_titles = ['Song1', 'Song2 Longer', 'The Last Song']
        length_songs = ['3.19', '4.31', '2.58']
        expected_output =  [('Song2 Longer', '4.31'), ('Song1', '3.19'), ('The Last Song', '2.58')]
        self.assertEqual(sort_songs(song_titles, length_songs, last_word), expected_output)
    
    def test_sort_songs_invalid_key(self):
        song_titles = ['Song1', 'Song2 Longer', 'The Last Song']
        length_songs = ['3.19', '4.31', '2.58']
        self.assertIsNone(sort_songs(song_titles, length_songs, 'invalid_key'))


if __name__ == '__main__':
    unittest.main()
