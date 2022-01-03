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


class ChessBoard:
    def __init__(self, data, size):
        self.size = size
        self.data = data
        self.chess_board = [['⬛', '⬜'] * (size // 2) for _ in range(size)]
        for i in range(1, size, 2):
            self.chess_board[i].reverse()
        for i in range(len(data)):
            self.chess_board[data[i][0]][data[i][1]] = '♛'

    def queen_check(self):
        for i in range(len(self.data)):
            for j in range(i + 1, len(self.data)):
                if self.data[i][0] == self.data[j][0] or self.data[i][1] == self.data[j][1]:
                    return False
                elif abs(self.data[i][0] - self.data[j][0]) == abs(self.data[i][1] - self.data[j][1]):
                    return False
        return True

    def print_board(self):
        for i in range(self.size):
            for j in range(self.size):
                print(self.chess_board[i][j], end=" ")
            print()
        print("\n")


board_1 = ChessBoard([(1, 2), (6, 2), (7, 7)], 8)
board_2 = ChessBoard([(4, 7), (1, 1), (7, 2), (2, 8), (9, 6)], 10)
board_3 = ChessBoard([(randint(0, 9), randint(0, 9)) for _ in range(3)], 10)
board_4 = ChessBoard([(15, 24), (12, 21), (1, 16), (25, 26), (4, 8)], 30)
board_5 = ChessBoard([(16, 81), (19, 50), (1, 0), (28, 73), (77, 42), (0, 80), (90, 8)], 100)

print("board 1: ", board_1.queen_check())
board_1.print_board()
print("board 2: ", board_2.queen_check())
board_2.print_board()
print("board 3: ", board_3.queen_check())
board_3.print_board()
print("board 4: ", board_4.queen_check())
board_4.print_board()
print("board 5: ", board_5.queen_check())
