# Problem: https://cms.ucu.edu.ua/mod/vpl/view.php?id=330760
"""
GPT створив додаткову функцію для перевірки валідності значень,
але іноді використовува її без потреби
Sudoku Puzzle Validation Module
This module provides functions to validate Sudoku puzzles.
"""
import time
from memory_profiler import memory_usage
# import psutil

def validate_board(board: list) -> bool:
    """
    Validate the Sudoku board.
    Args:
        board (list): The Sudoku board represented as a list of strings.
    Returns:
        bool: True if the board is valid, False otherwise.

    The function checks if the Sudoku board is valid for the game. The board is valid if:
    1) None of the colored rows contains duplicate digits.
    2) No digits are repeated in any of the colored columns.
    3) No colored patch of the same color has triple digits.

    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
        "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    def check_elements(elements, keylist, value):
        """
        Check if adding the value to the elements dictionary results in a valid board section.

        Args:
            elements (dict): Dictionary to store elements.
            keylist (list): List of keys for the elements dictionary.
            value (str): Value to check and add to elements.

        Returns:
            bool: True if the value can be added without duplication, False otherwise.

        >>> check_elements({'1': 0, '2': 0, '3': 0}, ['1', '2', '3'], '1')
        False
        >>> check_elements({'1': 0, '2': 0, '3': 0}, ['1', '2', '3'], '4')
        True
        """
        if value in ('*', ' '):
            return True
        n = keylist.index(value)
        if value == elements[str(n + 1)]:
            return False
        elements[str(n + 1)] = value
        return True

    for j in range(5):
        elements = {}
        for k in range(9):
            elements[str(k + 1)] = 0
        keylist = list(elements.keys())
        for i in range(5 + j):
            if check_elements(elements, keylist, board[i][4 - j]):
                pass
            else:
                return False
        for i in range(4 + j):
            if check_elements(elements, keylist, board[4 + j][8 - i]):
                pass
            else:
                return False
    # For columns
    for j in range(9):
        elements = {}
        for k in range(9):
            elements[str(k + 1)] = 0
        keylist = list(elements.keys())
        for i in range(9):
            if check_elements(elements, keylist, board[i][j]):
                pass
            else:
                return False
    # For rows
    for i in range(9):
        elements = {}
        for k in range(9):
            elements[str(k + 1)] = 0
        keylist = list(elements.keys())
        for j in range(9):
            if check_elements(elements, keylist, board[i][j]):
                pass
            else:
                return False
    return True

if __name__ == "__main__":
    t0 = time.monotonic()
    # Викликаємо функцію для вимірювання пам'яті
    mem_usage = memory_usage((validate_board, (["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"],)), interval=0.1)
    t1 = time.monotonic()
    dt = t1 - t0
    mem_used = max(mem_usage) - min(mem_usage)  # Різниця між максимальним та мінімальним значенням
    mem_usage_kb = [round(mem * 1024) for mem in mem_usage]
    total_memory_kb = sum(mem_usage_kb)
    print(f"Використано пам'яті: {total_memory_kb} KB")
    print("Час виконання:", dt)

# Використано пам'яті: 512680 KB
# Час виконання: 1.827999999979511
