"""
Zadanie 6 - lab 8
Dana jest N-elementowa lista wypełniona liczbami naturalnymi.
Proszę napisać funkcję, która zwraca długość najdłuższego, spójnego podciągu rosnącego dla którego suma jego elementów jest równa sumie indeksów tych elementów.
Do funkcji należy przekazać listę, funkcja powinna zwrócić długość znalezionego podciągu lub 0 jeżeli taki podciąg nie istnieje.
"""

list = [15, 12, 4, 8, 11, 17, 2, 1, 1, 2, 24]
print(list)
N = len(list)

for i in range(N):
    try:
        if type(list[i]) != int or list[i] < 0:
            raise ValueError
    except:
        print("All numbers should be natural!")
        exit()

max_length = 0

for i in range(N-1):
    sum = list[i]
    sum_idx = i
    length = 1
    for j in range(i+1, N):
        if list[j-1] < list[j]:
            sum += list[j]
            sum_idx += j
            length += 1
            if sum == sum_idx:
                max_length = max(length, max_length)
        else:
            break

print(max_length)

# [0 ,1, 2, 3, -1] => error
# [0 ,1, 2, 3, '5'] => error
# [0, 1, 2, 3, 4, 5] => 6 (0 -> 6)
# [0, 1, 2, 3, 7, 9, 3, 7, 8, 9, 10, 11, 12, 13, 6, 8, 3, 314, 75, 96, 3] => 7 (7 -> 13)
# [15, 12, 4, 8, 11, 17, 2, 1, 1, 2] => 0
# [15, 12, 4, 8, 11, 17, 2, 1, 1, 2, 24] => 3 (1 -> 24)

