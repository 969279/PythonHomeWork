# Определить индексы элементов массива (списка), значения которых принадлежат
# заданному диапазону (т.е. не меньше заданного минимума и не больше заданного максимума)

import random

sart_num = int(input('Введите начало диапазона чисел: '))
end_num = int(input('Введите конец диапазона чисел: '))
list_1 = []
resuli_list = []

for i in range(20):
    list_1.append(random.randint(-20, 20))
    if sart_num < list_1[i] < end_num:
        resuli_list.append(list_1[i])

print(list_1)
print(resuli_list)


