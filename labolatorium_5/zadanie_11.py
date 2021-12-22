def nww(a,b):
    a_cp = a
    b_cp = b
    while a != b:
        if a > b:
            b += b_cp
        else:
            a += a_cp
    return b

print(nww(nww(1,2), 3))
print(nww(nww(10,25), 100))
print(nww(nww(111,2104), 312))
