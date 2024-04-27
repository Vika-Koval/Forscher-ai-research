"""
This function sorts a list of songs by their length, length of their name or a position \
of last word of name in the alphabet
"""
from collections.abc import Callable

def song_length(x: tuple[str]) -> float:
    """
    This function converts length of song to float
    >>> song_length (('Той день', '3.58'))
    3.58
    """
    len_song = float(x[1])
    return float(len_song)

def title_length(x) -> int:
    """
    This function return the length of the title of the song. 
    >>> title_length (('Янанебібув', '3.19'))
    10
    """
    return len(x[0])

def last_word(x) -> str:
    """
    This function returns the first letter of last word of the title
    >>> last_word (('Янанебібув', '3.19'))
    'Я'
    >>> last_word (('Поясни', '3.39'))
    'П'
    """
    x2 = x[0].split()
    result = x2[-1][0]
    return result

def sort_songs(
    song_titles: list[str],
    length_songs: list[str],
    key_: Callable[[tuple], int | str | float]) -> list[tuple] | None:
    """
    sorting a list of songs
    >>> (sort_songs(['Янанебібув', 'Той день', 'Мало мені', 'Сосни', 'Кавачай', \
'Відпусти', 'Африка', 'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'],\
['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', \
'3.43', '3.17', '2.21'], song_length))
    [('Етюд', '2.21'), ('Коли тебе нема', '3.17'), ('Янанебібув', '3.19'), ('Поясни', '3.39'), \
('Фіалки', '3.43'), ('Відпусти', '3.52'), ('Той день', '3.58'), \
('Африка', '4.24'), ('Сосни', '4.31'), \
('Кавачай', '4.39'), ('Мало мені', '5.06')]
    >>> (sort_songs(['Янанебібув', 'Той день', 'Мало мені', \
'Сосни', 'Кавачай', 'Відпусти', 'Африка', \
'Поясни', 'Фіалки', 'Коли тебе нема', 'Етюд'],\
['3.19', '3.58', '5.06', '4.31', '4.39', '3.52', '4.24', '3.39', \
'3.43', '3.17', '2.21'], title_length))
    [('Етюд', '2.21'), ('Сосни', '4.31'), ('Африка', '4.24'), \
('Поясни', '3.39'), ('Фіалки', '3.43'), \
('Кавачай', '4.39'), ('Той день', '3.58'), ('Відпусти', '3.52'), \
('Мало мені', '5.06'), ('Янанебібув', '3.19'), \
('Коли тебе нема', '3.17')]
    """
    if isinstance(song_titles,list) is False or isinstance(length_songs, list) is False\
        or key_ not in (song_length, title_length, last_word):
        return None
    songs = []
    for sng in range(len(song_titles)):
        song = song_titles[sng], length_songs[sng]
        songs.append(song)
    if key_ is song_length:
        songs.sort(key = song_length)
        return songs
    if key_ is title_length:
        songs.sort(key = title_length)
        return songs
    if key_ is last_word:
        songs.sort( key = last_word)
        return songs

