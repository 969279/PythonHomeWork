# Петя, Катя и Сережа делают из бумаги журавликов.
# Вместе они сделали S журавликов.
# Сколько журавликов сделал каждый ребенок, если известно, что
# Петя и Сережа сделали одинаковое количество журавликов, а Катя
# сделала в два раза больше журавликов, чем Петя и Сережа вместе?
#Пример:
#6 -> 1  4  1
#24 -> 4  16  4
#60 -> 10  40  10

number = int(input('Введите число сделанных детьми журавликов: '))

if number % 6 == 0:
    print(round(number // 1.5))
    print(number // 6)
else:
    print('Такого быть не может :-)')