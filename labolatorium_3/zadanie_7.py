a = int(input("Podaj mniejszą z granic zakresu: "))
b = int(input("Podaj większą z granic zakresu: "))
avg = (a+b)/2
x = -2.5 #pomocnicza zmienna
if b - a > 20:
    if avg % 2 == 0:
        for i in range(7):
            if i == 3:
                continue
            print (avg - 3 + i)

    else:
        while x != 3.5:
            print (avg + x)
            x += 1

else:
    for i in range(a, b+1):
        print(i)
