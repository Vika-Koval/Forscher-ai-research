"""puzzle function"""

import time
from memory_profiler import memory_usage

def validate_board(board:list) -> bool:
    """
    (board) -> bool
    The function checks if our board is ready for the game, if so,\n 
    then returns True, otherwise - False
    The board is ready to play if 
    1) none of the coloured rows contains duplicate digits
    2) no digits are repeated in any of the coloured columns
    3) no coloured patch of the same colour has triple digits 
    >>> validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****",\
    "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    False
    """
    for j in range(5):
        elements = set()
        for i in range(5+j):
            if board[i][4-j] != '*' and board[i][4-j] != ' ':
                if board[i][4-j] in elements:
                    return False
                elements.add(board[i][4-j])
        for i in range(4+j):
            if board[4+j][8-i] != '*' and board[4+j][8-i] != ' ':
                if board[4+j][8-i] in elements:
                    return False
                elements.add(board[4+j][8-i])
    # Для стовпців
    for j in range(9):
        elements = set()
        for i in range(9):
            if board[i][j] != '*' and board[i][j] != ' ':
                if board[i][j] in elements:
                    return False
                elements.add(board[i][j])
    # Для рядків
    for i in range(9):
        elements = set()
        for j in range(9):
            if board[i][j] != '*' and board[i][j] != ' ':
                if board[i][j] in elements:
                    return False
                elements.add(board[i][j])
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

# Використано пам'яті: 257120 KB
# Час виконання: 2.0
