# В фермерском хозяйстве в Карелии выращивают чернику.
# Она растет на круглой грядке, причем кусты высажены только по окружности.
# Таким образом, у каждого куста есть ровно два соседних. Всего на грядке растет N кустов.
# Эти кусты обладают разной урожайностью, поэтому ко времени сбора на
# них выросло различное число ягод – на i-ом кусте выросло ai ягод.
# В этом фермерском хозяйстве внедрена система автоматического сбора черники.
# Эта система состоит из управляющего модуля и нескольких собирающих модулей.
# Собирающий модуль за один заход, находясь непосредственно перед некоторым
# кустом, собирает ягоды с этого куста и с двух соседних с ним.
# Напишите программу для нахождения максимального числа ягод, которое
# может собрать за один заход собирающий модуль, находясь перед некоторым
# кустом заданной во входном файле грядки.


import random
bush = int(input('Введите количество кустов на грядке: '))
harvest = [random.randint(1, 10) for _ in range(bush)]
maxHarvest = 1
summHarvest = 0
numBush = ''
print(harvest)

for i in range(len(harvest)):
    first, last = 0, 0
    if summHarvest > maxHarvest:
        maxHarvest = summHarvest
        print(maxHarvest)
    if i == 0:
        first = len(harvest) - 1
        last = i + 1
    elif i == len(harvest) - 1:
        first = i - 1
        last = 0
    else:
        first = i - 1
        last = i + 1

    summHarvest = harvest[first] + harvest[i] + harvest[last]
    numBush = [first, i, last]

print(numBush)
print(maxHarvest)













"""
harvest = [1, 1, 1, 4, 1]
#if bush < 3:
#    print('Количество не сожет быть меньше 3.')
#else:
#    print(harvest)

harv = tuple(harvest)
maxHarvest = 0
numberBush = 0
leftBush = 0
rightBush = 0


print(harv)

for i in range(len(harvest) + 2):
    summHarvest = harvest[0] + harvest[1] + harvest[2]
    harvest.append(harvest.pop(0))
    #print(summHarvest)
    if summHarvest > maxHarvest:
        maxHarvest = summHarvest
        numberBush = i + 1
        if numberBush > len(harvest) - 1:
            numberBush = 0
leftBush = numberBush
rightBush = numberBush + 2
if leftBush < 0:
    leftBush = len(harvest) - numberBush
if rightBush > len(harvest) - 1:
    rightBush = rightBush - len(harvest)
print(f'Максимальный урожай {maxHarvest} ягод при сборе с кустов №№ {leftBush}, {numberBush + 1}, {rightBush}')



key = 1
for key in range(1, bush + 1):
    harv[key] = random.randint(1, 10)
print(harv)
#print(*harv.values())
harv_list = list(harv.values())
print(harv_list)
"""