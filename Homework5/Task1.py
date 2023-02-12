# Напишите программу, которая на вход принимает два числа A и B,
# и возводит число А в целую степень B с помощью рекурсии.

number = int(input('Введите число: '))
degree = int(input('Введите степень числа: '))

def degree_Number(num, deg):
    if deg == 1:
        return num
    return degree_Number(num, deg - 1) * num

print(f'{number} ** {degree} = {degree_Number(number, degree)}')

