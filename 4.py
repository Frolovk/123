b = int(input("vvedite kol-vo chisel:  "))
a = []
for i in range(1, b + 1):
    v = int(input(i))
    a.append(v)
print("summa: ", (sum(a)))
