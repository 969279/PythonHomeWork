# Вводим максимальную степень многочлена и формируем многочлен в виде строки
# koef*x**n + koef*x**n - ..... = 0
# Сгенерировать второй многочлен и сложить оба многочлена с учетом степеней.

degree = int(input('Введите степень многочлена: '))
#d = [int(input('Введите степень первого многочлена: ')), int(input('Введите степень второго многочлена: '))]

polinome = dict()
polinome_1 = list()
result = list()
pol = dict()
import random
message = str()

"""
for i in range(2):
    print(d[i])
    for l in range(d[i], -1, -1):
        pol[l] = random.randint(1, 30)
    print(pol)
print()


for n in range(degree, -1, -1):
    pol[n] = (random.randint(1, 30), '*x**')
print(pol)
#print(pol[1])
"""

for n in range(degree, -1, -1):
    polinome[n] = random.randint(1, 30)
print(polinome)

for key, value in polinome.items():
    if key == 1:
        polinome_1.append(f'{value}*x')
    elif key == 0:
        polinome_1.append(f'{value}')
    else:
        polinome_1.append(f'{value}*x**{key}')
    if key != 0:
        polinome_1.append('+')
    else:
        polinome_1.append('= 0')
print(*polinome_1)
print(polinome_1[-2])

for i in range(len(polinome_1)):
    message = polinome_1[i]
    for num in message:
        if num == '*' or num == '+' or num == '=':
            break
        else:
            print(num)

#print(d)

