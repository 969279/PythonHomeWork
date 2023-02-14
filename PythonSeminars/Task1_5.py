# Дан список чисел. Посчитайте, сколько в нем пар элементов, равных друг другу.
# Считается, что любые два элемента, равные друг другу образуют одну пару, которую необходимо посчитать.

import random

number = int(input('Укажите количество элементов: '))
list_1 = []

for i in range(number):
    list_1.append(random.randint(1, 10))
print(list_1)

dict_1 = {}
new_list = []

for i in range(len(list_1)):
    dict_1[i] = dict_1.get(list_1[i], 0) + 1
    if dict_1.get(list_1[i]) == 1:
        new_list.append(list_1[i])
    else:
        new_list.append(list_1[i])



for j in range(len(list_1)):
    num = list_1.count(list_1[j])


print(list_1[j], list_1.count(list_1[j]))




