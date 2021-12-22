"""
Zadanie 9 - lab 7
Proszę napisać program, który pobierze od użytkownika 5 różnych liczb całkowitych i doda je do listy.
Program ma za zadanie uzupełnić listę liczbami całkowitymi znajdującymi się pomiędzy kolejnymi liczbami a następnie wypisać listę.
Przykładowe dane wejściowe:
[0,7,13,8,12]
pożądane wyjście:
[0,1,2,3,4,5,6,7,8,9,10,11,12,13,12,11,10,9,8,9,10,11,12].
Należy obsłużyć wyjątek, w którym dwie sąsiadujące ze sobą wprowadzone przez użytkownika liczby są takie same.
"""

class SameNumberError(Exception):
    pass


list = []

while True:
    try:
        for i in range(5):
            num = int(input(f"Enter {i + 1} number: "))
            if i > 0 and num == list[i - 1]:
                raise SameNumberError
            list.append(num)
        break

    except SameNumberError:
        print("Adjacent numbers should be different, try again.")
        list = []

print(list)

i = 0
while i <= len(list) - 2:
    if list[i] > list[i + 1] + 1:
        list.insert(i + 1, list[i] - 1)
        # print(list)
    elif list[i] < list[i + 1] - 1:
        list.insert(i + 1, list[i] + 1)
        # print(list)
    i += 1

print(list)
