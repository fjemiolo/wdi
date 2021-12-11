"""
Zadanie 3 - lab 10
Wykorzystując funkcje, napisz program tworzący plansze do sudoku (a przynajmniej w miarę).
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


def sudoku_maker(Tab):
    num = randint(1, 9)
    while True:
        step = randint(1, 9)
        if step % 3 != 0:
            break
    fill_part(Tab, 0, 0, num, step)
    num = increment(num, step)
    fill_part(Tab, 2, 2, num, step)
    num = increment(num, step)
    fill_part(Tab, 1, 0, num, step)
    num = increment(num, step)
    fill_part(Tab, 0, 2, num, step)
    num = increment(num, step)
    fill_part(Tab, 2, 1, num, step)
    num = increment(num, step)
    fill_part(Tab, 1, 2, num, step)
    num = increment(num, step)
    fill_part(Tab, 0, 1, num, step)
    num = increment(num, step)
    fill_part(Tab, 2, 0, num, step)
    num = increment(num, step)
    fill_part(Tab, 1, 1, num, step)


def sudoku_remover(Tab, cnt):
    while cnt > 0:
        a, b = randint(0, 8), randint(0, 8)
        if Tab[a][b] != 0:
            Tab[a][b] = 0
            cnt -= 1


def expand_line(line):
    return line[0] + line[5:9].join([line[1:5] * (3 - 1)] * 3) + line[9:13]


def print_board(board):
    line0 = expand_line("╔═══╤═══╦═══╗")
    line1 = expand_line("║ . │ . ║ . ║")
    line2 = expand_line("╟───┼───╫───╢")
    line3 = expand_line("╠═══╪═══╬═══╣")
    line4 = expand_line("╚═══╧═══╩═══╝")
    symbol = " 1234567890ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    nums = [[""] + [symbol[n] for n in row] for row in board]
    print(line0)
    for r in range(1, 10):
        print("".join(n + s for n, s in zip(nums[r - 1], line1.split("."))))
        print([line2, line3, line4][(r % 9 == 0) + (r % 3 == 0)])


amount = int(input("Enter amount of remaining numbers: "))
print("\n")
Sudoku = [[0]*9 for _ in range(9)]

sudoku_maker(Sudoku)
print("Solved Sudoku:")
print_board(Sudoku)
print()
sudoku_remover(Sudoku, 81 - amount)
print("Unsolved Sudoku:")
print_board(Sudoku)
