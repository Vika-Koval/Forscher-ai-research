"""
puzzle function
"""
import time
import psutil

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
        elements = {}
        for k in range(9):
            elements[str(k+1)] = 0
        keylist = list(elements.keys())
        for i in range(5+j):
            if board[i][4-j] == '*' :
                # Це для j>1, верхні і праві елементи пропускати
                pass
            elif board[i][4-j] == ' ':
                # Коли нема числа
                pass
            else:
                n = keylist.index(str(board[i][4-j]))
                if str(board[i][4-j]) == elements[str(n+1)]:
                    # Перевіряєм чи вже існує такий елемен в лісті, якщо існує,
                    # то ми отримали повтор, тому False
                    return False
                elements[str(n+1)] = str(board[i][4-j])
        for i in range(4+j):
            if board[4+j][8-i] == '*':
                pass
            elif board[4+j][8-i] == ' ':
                pass
            else:
                n = keylist.index(str(board[4+j][8-i]))
                if str(board[4+j][8-i]) == elements[str(n+1)]:
                    return False
                elements[str(n+1)] = str(board[4+j][8-i])
    # Для стовпців
    for j in range(9):
        elements = {}
        for k in range(9):
            elements[str(k+1)] = 0
        keylist = list(elements.keys())
        for i in range(9):
            if board[i][j] == '*' :
                pass
            elif board[i][j] == ' ':
                pass
            else:
                n = keylist.index(str(board[i][j]))
                if str(board[i][j]) == elements[str(n+1)]:
                    return False
                elements[str(n+1)] = str(board[i][j])
    # Для рядків
    for i in range(9):
        elements = {}
        for k in range (9):
            elements[str(k+1)] = 0
        keylist = list(elements.keys())
        for j in range(9):
            if board[i][j] == '*' :
                pass
            elif board[i][j] == ' ':
                pass
            else:
                n = keylist.index(str(board[i][j]))
                if str(board[i][j]) == elements[str(n+1)]:
                    return False
                elements[str(n+1)] = str(board[i][j])
    return True

if __name__ == "__main__":
    t0 = time.monotonic()
    cpu0 = psutil.cpu_percent()
    memory0 = psutil.virtual_memory().percent
    validate_board(["**** ****", "***1 ****", "**  3****", "* 4 1****", "     9 5 ", " 6  83  *", "3   1  **", "  8  2***", "  2  ****"])
    t1 = time.monotonic()
    cpu1 = psutil.cpu_percent()
    memory1 = psutil.virtual_memory().percent
    dt = t1-t0
    dcpu = cpu1-cpu0
    dmemory = memory1-memory0
    print(dt)
    print(dcpu)
    print(dmemory)

    # 0.015000000013969839
    # 7.1
    # 0.0
