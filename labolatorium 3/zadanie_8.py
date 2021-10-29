a = int(input('wprowadź wysokość choinki: '))

for i in range(a):
    if i == 0:
        print(' ' * (a - 1) + '^')
    else:
        print(' ' * (a - i - 1) + '*' * (i * 2 + 1))

print(' ' * (a - 1) + 'U')