a = [ int(input()) for i in range(10) ]
print(a)
v = []
k = 0
for i in range(len(a) - 1):
   if a[i] not in v:
     if a.count(a[i]) > 1:
       v.append(a[i])
       k = a.index(a[i])
       print('chislo: ', a[i], 'index: ', k, end=' ')
       for j in range(a.count(a[i]) - 1):
         k = a.index(a[i], k + 1)
         print(k, end=' ')
       print()
