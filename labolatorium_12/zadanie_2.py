"""
Zadanie 2. - lab 12
Na szachownicy o wymiarach 100 na 100 umieszczamy N hetmanów (N<100).
Położenie hetmanów jest opisywane przez następującą listę:
dane = [(w1, k1),(w2, k2) ,(w3, k3), ...,(wN, kN)]
Proszę napisać funkcję, która odpowiada na pytanie: czy żadne dwa hetmany się nie szachują?
Do funkcji należy przekazać położenie hetmanów.
Należy zwizualizować rozkład hetmanów na szachownicy (w tym celu można wykorzystać pliki).
"""
from random import randint


class chess:
    def queen_check(self, Tab, N):
        for i in range(N):
            for j in range(i + 1, N):
                if Tab[i][0] == Tab[j][0] or Tab[i][1] == Tab[j][1]:
                    return False
                elif abs(Tab[i][0] - Tab[j][0]) == abs(Tab[i][1] - Tab[j][1]):
                    return False
        return True

    def print_board(self, Tab):
        for i in range(10):
            for j in range(10):
                print(chess_board[i][j], end="  ")
            print("")
        print("")

N = 3
data = [(randint(0, 9), randint(0, 9)) for _ in range(N)]
chess_board = [['.'] * 10 for _ in range(10)]

for i in range(N):
    chess_board[data[i][0]][data[i][1]] = 'X'

chess().print_board(chess_board)

print(chess().queen_check(data, N))
