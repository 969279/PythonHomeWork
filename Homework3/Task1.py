# Задаем длину списка наполненного рандомными числами от 1 до 100.
# Вводим искомое число X
# Программа должна вывести в консоль сколько раз встречается в заданном списке искомое число X,
# которое мы вводим с клавиатуры, либо выводим на экран, максимально близкое ему по значению.

import random
listNumbers = [random.randint(1, 100) for i in range(int(input('Введите длину списка: ')))]
number = int(input('Введите искомое число: '))
num, count = 100, 0
print(listNumbers)

for i in range(len(listNumbers)):
    if listNumbers[i] == number:
        count += 1
    elif abs(listNumbers[i] - number) < num:
        num = abs(listNumbers[i] - number)
        foundNum = listNumbers[i]

if count > 0:
    print(f'Искомое число {number} присутствует в списке {count} раз(а).')
else:
    print(f'Ближайшее число к искомому: {foundNum}')
