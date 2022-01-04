"""
Zadanie 10.
Rozwiąż rekurencyjnie Problem Skoczka Szachowego.
Wskaż kolejne ruchy skoczka wypisując macierz.
"""


def is_move_possible(Tab, x, y, index):
    moves = [(1, 2), (2, 1), (2, -1), (1, -2), (-1, -2), (-2, -1), (-2, 1), (-1, 2)]
    x += moves[index][0]
    y += moves[index][1]
    if 0 <= x < len(Tab) and 0 <= y < len(Tab) and Tab[x][y] == 0:
        return x, y
    return None


def print_result(Tab):
    for i in range(len(Tab)):
        for j in range(len(Tab)):
            print(Tab[i][j], end="\t")
        print()


def knights_tour(Tab, x=0, y=0, cnt=1):
    Tab[x][y] = cnt
    if cnt == len(Tab) ** 2:
        print_result(Tab)
        exit()
    for i in range(8):
        tmp = is_move_possible(Tab, x, y, i)
        if tmp is not None:
            knights_tour(Tab, tmp[0], tmp[1], cnt + 1)
    Tab[x][y] = 0


size = 6
board = [[0] * size for _ in range(size)]
knights_tour(board)
