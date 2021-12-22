from random import randint

def calc():
    tmp = str(input("Czy wylosować pierwszą liczbę? [ T | N ] "))
    if tmp == 'T':
        l = int(input("Podaj mniejszą z granic zakresu losowania: "))
        p = int(input("Podaj większą z granic zakresu losowania: "))
        a = randint(l,p)
    elif tmp == 'N':
        a = int(input("Wprowadź pierwszą liczbę: "))
    else:
        print("Błąd!")

    tmp = str(input("Czy wylosować drugą liczbę? [T/N] "))
    if tmp == 'T':
        l = int(input("Podaj mniejszą z granic zakresu losowania: "))
        p = int(input("Podaj większą z granic zakresu losowania: "))
        b = randint(l,p)
    elif tmp == 'N':
        b = int(input("Wprowadź drugą liczbę: "))
    else:
        print("Błąd!")

    tmp = str(input("Wprowadź działanie [ + | - | * | / | ** | ^ ] "))
    if tmp == '+':
        print(f"{a}+{b}={a+b}\n")
        decision = str(input('Czy chcesz wprowadzić nowe dane? [ T | N ] '))
        if decision == 'T':
            calc()
        else:
            exit()

    if tmp == '-':
        print(f"{a}-{b}={a-b}\n")
        decision = str(input('Czy chcesz wprowadzić nowe dane? [ T | N ] '))
        if decision == 'T':
            calc()
        else:
            exit()

    if tmp == '*':
        print(f"{a}*{b}={a*b}\n")
        decision = str(input('Czy chcesz wprowadzić nowe dane? [ T | N ] '))
        if decision == 'T':
            calc()
        else:
            exit()

    if tmp == '/':
        print(f"{a}/{b}={a/b}\n")
        decision = str(input('Czy chcesz wprowadzić nowe dane? [ T | N ] '))
        if decision == 'T':
            calc()
        else:
            exit()

    if tmp == '**':
        print(f"{a}**{b}={a**b}\n")
        decision = str(input('Czy chcesz wprowadzić nowe dane? [ T | N ] '))
        if decision == 'T':
            calc()
        else:
            exit()

    if tmp == '^':
        print(f"pierwiastek {a} stopnia z {b} = {b**(1/a)}\n")
        decision = str(input('Czy chcesz wprowadzić nowe dane? [ T | N ] '))
        if decision == 'T':
            calc()
        else:
            exit()

calc()