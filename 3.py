a = int(input("vvedite chislo: "))
b = int(input("vvedite chislo menshe pervogo: "))
for i in range(b, a + 1)[::-1]:
    if i % 2 == 0:
        continue
    print(i)
