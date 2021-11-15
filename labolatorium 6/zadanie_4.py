"""
Zadanie 4
Proszę napisać program wczytujący liczbę naturalną z klawiatury i odpowiadający na pytanie,
czy liczba ta jest wielokrotnością dowolnego wyrazu ciągu danego wzorem: A(n)=n∗n+n+1.
Należy sprawdzić przypadki użycia dla kilku wczytywanych liczb naturalnych.
Należy obsłużyć wyjątek wczytania danej niebędącej liczbą naturalną.
"""

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

#for i in range (20):
#    print (A(i))

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))

is_multiple(num1)
is_multiple(num2)
is_multiple(num3)

"""
maks = max(num1,num2,num3)
h1 = h2 = h3 = 0
n = 1

while A(n) <= max(num1, num2, num3):
    if num1 / A(n) == int(num1 / A(n)):
        print (f"{num1} is a multiple of A({n}) = {A(n)}")
        h1 = 1
    if num2 / A(n) == int(num2 / A(n)):
        print (f"{num2} is a multiple of A({n}) = {A(n)}")
        h2 = 1
    if num3 / A(n) == int(num3 / A(n)):
        print (f"{num3} is a multiple of A({n}) = {A(n)}")
        h3 = 1
    n += 1

if h1 == 0:
    print (f"{num1} is not a multiple")
if h2 == 0:
    print (f"{num2} is not a multiple")
if h3 == 0:
    print (f"{num3} is not a multiple")
"""

