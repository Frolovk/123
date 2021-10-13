a = int(input("vvedite chislo: "))
b = int(input("vvedite chislo menshe pervogo: "))
if a <= b:
    b += 1
    for i in range(a, b):
        print(i)
