"""
Zadanie 5 - lab 9
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n
i wypełniający ją liczbami ciągu Fibonacciego po spirali.
Wymiar tablicy powinien być definiowany przez użytkownika.
"""

import numpy as np

def fibonacci_numbers(n):
    F = [1] * n
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F

while True:
    try:
        N = int(input("Enter size of your array: "))
        if N <= 0:
            raise ValueError
        else:
            break
    except:
        print("Your input should be natural number! Try again.")

Fib_Spiral = [[0 for _ in range(N)] for _ in range(N)]
Fib = fibonacci_numbers(N * N)

cnt = 0
low = 0
high = N - 1
layers = int((N + 1) / 2)
for i in range(layers):
    for j in range(low, high + 1):  # left to right
        Fib_Spiral[i][j] = Fib[cnt]
        cnt += 1
    for j in range(low + 1, high + 1):  # up to down
        Fib_Spiral[j][high] = Fib[cnt]
        cnt += 1
    for j in range(high - 1, low - 1, -1):  # right to left
        Fib_Spiral[high][j] = Fib[cnt]
        cnt += 1
    for j in range(high - 1, low, -1):  # down to up
        Fib_Spiral[j][low] = Fib[cnt]
        cnt += 1
    low += 1
    high -= 1
#    for element in Fib_Spiral:
#       print(element)
#    print("----------")

print("Your spiral of Fibonacci numbers: ")
print(np.matrix(Fib_Spiral))
