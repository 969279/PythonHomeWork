# На столе лежат n монеток. Некоторые из них лежат вверх решкой, а некоторые – гербом.
# Определите минимальное число монеток, которые нужно перевернуть, чтобы все монетки
# были повернуты вверх одной и той же стороной.
# Выведите минимальное количество монет, которые нужно перевернуть

# *Пример:
# 5 -> 1 0 1 1 0
# 2

number = int(input('Введите количество монет: '))
import random
coins = str()
count0 = 0
count1 = 0

for i in range(number):
    num = random.randint(0, 1)
    if num == 1:
        count1 += 1
    else:
        count0 += 1
    coin = str(num)
    coins = coins + coin + ' '

print(coins)
print(f'Выпало: орёл - {count1}, решка - {count0}')

if count1 == count0:
    print(f'Монет выпало поровну.')
elif count1 > count0:
    print(f'Нужно перевернуть {count0} монет(ы)')
else:
    print(f'Нужно перевернуть {count1} монет(ы)')


