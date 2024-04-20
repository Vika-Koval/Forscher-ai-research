# Цей код не має 1, але blackbox або просто надсилав мені мій ж код, або цей
# хочу також сказати, що цей код має деякі цікаві рішення, як, наприклад, спроба використати &,
# проте він не перевіряє чи на одному кольорі нема повторів чисел
"""Puzzle check"""
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
            row = board[i][4-j:]
            if len(row) < 3:
                continue
            if len(elements & set(row)) != 0:
                return False
            elements.update(row)

        for i in range(4+j):
            col = [board[i][j] for i in range(9)]
            if len(col) < 3:
                continue
            if len(elements & set(col)) != 0:
                return False
            elements.update(col)

    return True
