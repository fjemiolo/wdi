"""
Zadanie 4
Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem: A(n)=n∗n+n+1.
Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.
"""

class NegativeNumberError(Exception):
    pass

def A(n):
    return n * n + n + 1

def is_multiple(num):
    n = 1
    while A(n) <= num:
        if num / A(n) == int(num / A(n)):
            print(f"{num} is a multiple of A({n}) = {A(n)}")
            return
        n += 1
    print(f"{num} is not a multiple")

while True:
    try:
        num = int(input("Enter your number: "))
        if type(num) != int:
            raise ValueError
        if num > 0:
            break
        else:
            raise NegativeNumberError
    except ValueError:
        print("Your input should be an integer.")
    except NegativeNumberError:
        print("Your number should be natural.")

is_multiple(num)



        

