# Требуется вывести все целые степени двойки
# (т.е. числа вида 2k), не превосходящие числа N.
# Пример:
# 10 -> 1 2 4 8

number = int(input('Введите целое число: '))
exp = 0
i = 0
result = str()

while exp < number - exp:
    exp = 2 ** i
    i += 1
    result = result + str(exp) + ' '

print(result)

