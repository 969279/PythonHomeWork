# Для числа А>1 определть позицию n ряда чисел Фибоначчи
# Если А не число Фибоначчи то вывести -1

number = int(input('Введите натуральное число: '))
result = 0
num1 = 0
num2 = 1
count = 2

while result < number:
    result = num1 + num2
    num1 = num2
    num2 = result
    count += 1
#    print(result, count)
    if result == number:
        print(f'Число {number} на позиции {count} в ряду чисел Фибоначчи.')
    elif result > number:
        #print(f'Число {number} не принадлежит ряду чисел Фибоначчи.')
        print(-1)






