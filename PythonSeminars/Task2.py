# Дан список чисел. Определите, сколько в нем встречается различных чисел.

number = int(input('Введите количество чисел в списке: '))
import random
list_1 = []
set_1 = set()

for i in range(number):
    list_1.append(random.randint(0, 10))
    set_1.add(list_1[i])

print(list_1)

print(set_1)
print(len(set_1))

