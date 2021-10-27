def a(a1, a2):
 tan = a2 / a1
 return tan
x1 = int(input('1 koord 1 tochki: '))
x2 = int(input('2 koord 1 tochki: '))
y1 = int(input('1 koord 2 tochki: '))
y2 = int(input('2 koord 2 tochki: '))
z1 = int(input('1 koord 3 tochki: '))
z2 = int(input('2 koord 3 tochki: '))
if a(x1, x2) < a(y1, y2) < a(z1, z2):
 print(f'X({x1, x2})')
elif a(y1, y2) < a(x1, x2) < a(z1, z2):
 print(f'Y({y1, y2})')
else:
 print(f'Z({z1, z2}')
