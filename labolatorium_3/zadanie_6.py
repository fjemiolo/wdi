a = int(input('Wprowadź pierwszą liczbę: '))
b = int(input('Wprowadź drugą liczbę: '))
#komentarz krótki

if a < 0 and b < 0:
    print ("Obie liczby są mniejsze od 0 :(")
    exit()

if a > 0 and b > 0:
    print(f'suma liczb: {a+b}, różnica liczb: {a-b}, iloczyn liczb: {a*b}, iloraz liczb: {a/b}, kwadraty liczb: {a*a}, {b*b}, pierwiastki kwadratowe: {a**(1/2)}, {b**(1/2)}')

if a < 0:
    print(f'suma liczb: {a + b}, różnica liczb: {a - b}, iloczyn liczb: {a * b}, iloraz liczb: {a / b}, kwadraty liczb: {abs(a) * abs(a)}, {b * b}, pierwiastki kwadratowe: {abs(a) ** (1 / 2)}, {b ** (1 / 2)}')

if b < 0:
    print(
        f'suma liczb: {a + b}, różnica liczb: {a - b}, iloczyn liczb: {a * b}, iloraz liczb: {a / b}, kwadraty liczb: {a * a}, {b * b}, pierwiastki kwadratowe: {a ** (1 / 2)}, {abs(b) ** (1 / 2)}')

if a*b == 10:
    print ("Yay!")
'''
komentarz
troche 
dłuższy
'''
