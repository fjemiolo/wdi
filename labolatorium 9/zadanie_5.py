"""
Zadanie 5 - lab 9
Proszę napisać program wczytujący tablicę dwuwymiarową o ustalonym wymiarze n×n
i wypełniający ją liczbami ciągu Fibonacciego po spirali.
Wymiar tablicy powinien być definiowany przez użytkownika.
"""

def fibonacci_numbers(n):
    F = [1] * (n)
    for i in range(2, n):
        F[i] = F[i - 1] + F[i - 2]
    return F

while True:
    try:
        N = int(input("Enter size of your array: "))
        if type(N) != int or N <= 0:
            raise ValueError
        else:
            break
    except:
        print("Your input should be a natural number! Try again.")

A = [[0 for _ in range(N)] for _ in range(N)]
Fib = fibonacci_numbers(N * N)

cnt = 0
low = 0
high = N - 1
layers = int((N + 1) / 2)
for i in range(layers):
    for j in range(low, high + 1):  # left to right
        A[i][j] = Fib[cnt]
        cnt += 1
    for j in range(low + 1, high + 1):  # up to down
        A[j][high] = Fib[cnt]
        cnt += 1
    for j in range(high - 1, low - 1, -1):  # right to left
        A[high][j] = Fib[cnt]
        cnt += 1
    for j in range(high - 1, low, -1):  # down to up
        A[j][low] = Fib[cnt]
        cnt += 1
    low += 1
    high -= 1
#    for element in A:
#       print(element)
#    print("----------")

print("Your spiral of Fibonacci numbers: ")
for line in A:
    print(line)
