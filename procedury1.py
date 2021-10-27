a = int(input('vvedite diapazon: '))
for i in range(1, a + 1):
 b = len(str(i))
 summ = 0
 for j in str(i):
  summ += int(j) ** b
 if i == summ:
  print(i, end=' ')
