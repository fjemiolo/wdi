"""
Zadanie 3 - lab 10
Wykorzystując funkcje, napisz program tworzący plansze do Sudoku_board (a przynajmniej w miarę).
Plansze należy następnie zapisać do osobnych plików.
Należy zapisać je w takiej formie, żeby były czytelne dla ludzkiego oka.
Ponadto trzeba obsłużyć niezbędne wyjątki.
"""

from random import randint


def increment(num, step):
    num += step
    if num > 9:
        num -= 9
    return num


def fill_part(Tab, row, col, num, step):
    for i in range(row, 9, 3):
        for j in range(col, 9, 3):
            Tab[i][j] = num
            num = increment(num, step)
    num = increment(num, step)
    return Tab, num


def transposition(Tab):
    tmp = randint(1, 2)
    if tmp == 1:
        return Tab
    else:
        Transposed_Tab = [[0] * 9 for _ in range(9)]
        for i in range(9):
            for j in range(9):
                Transposed_Tab[i][j] = Tab[j][i]
        return Transposed_Tab


def sudoku_generator(Tab):
    num = randint(1, 9)
    while True:
        step = randint(1, 9)
        if step % 3 != 0:
            break
    Tab, num = fill_part(Tab, 0, 0, num, step)
    Tab, num = fill_part(Tab, 2, 2, num, step)
    Tab, num = fill_part(Tab, 1, 0, num, step)
    Tab, num = fill_part(Tab, 0, 2, num, step)
    Tab, num = fill_part(Tab, 2, 1, num, step)
    Tab, num = fill_part(Tab, 1, 2, num, step)
    Tab, num = fill_part(Tab, 0, 1, num, step)
    Tab, num = fill_part(Tab, 2, 0, num, step)
    Tab, num = fill_part(Tab, 1, 1, num, step)
    return Tab


def sudoku_remover(Tab, cnt):
    while cnt > 0:
        a, b = randint(0, 8), randint(0, 8)
        if Tab[a][b] != '.':
            Tab[a][b] = '.'
            cnt -= 1


def save_board(board, file, x):
    try:
        with open(file, 'w') as f:
            f.write(f'{x} board: \n')
            f.write('\n')
            for i in range(9):
                if i == 3 or i == 6:
                    f.write("-------------------------------\n")
                for j in range(9):
                    if j == 3 or j == 6:
                        f.write("|  ")
                    f.write(str(board[i][j]))
                    f.write('  ')
                f.write('\n')
    except PermissionError:
        print("You don't have permission")
    except IsADirectoryError:
        pass


amount = int(input("Enter amount of remaining numbers: "))

Sudoku_board = [[0] * 9 for _ in range(9)]
Sudoku_board = sudoku_generator(Sudoku_board)
Sudoku_board = transposition(Sudoku_board)
save_board(Sudoku_board, 'solved_board.txt', 'Solved')
sudoku_remover(Sudoku_board, 81 - amount)
save_board(Sudoku_board, 'unsolved_board.txt', 'Unsolved')
