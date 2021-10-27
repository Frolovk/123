a = [int(input()) for i in range(10)]
print('ishodniy massiv: ', a)
for i in range(len(a)):
 if a[i] == 0:
	 a[i]=1
 else:
	 a[i]=0
print('phinalniy massiv: ', a)
