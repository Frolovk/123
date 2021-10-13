n = int(input("Vvedite n: "))
a = 1
b = 1
c = 0
for i in range(1, n + 1):
    a = b * i
    c += a
    b = a
print(c)
