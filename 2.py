a = int(input("vvedite chislo: "))
b = int(input("vvedite chislo: "))
if a < b:
    b += 1
    for i in range(a, b):
        print(i)
else:
    a += 1
    for i in range(b, a)[::-1]:
        print(i)
