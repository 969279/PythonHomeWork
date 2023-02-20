# Составить список пар чисел где первое это четное число из спискаб второе - его квадрат.
# 1, 2, 3, 5, 8, 15, 23, 38

#numbers = [1, 2, 3, 5, 8, 15, 23, 38]
#result = list()

#sq = lambda x: x * x

#for i in numbers:
#    if i % 2 == 0:
#        result.append((i, i**2))

#print(result)

"""
#def select(f, num):
#    return [f(x) for x in num]

#def where(f, num):
#    return [x for x in num if f(x)]

numbers = [1, 2, 3, 5, 8, 15, 23, 38]

#result = select(int, numbers)
#print(result)

result = map(int, numbers)
print(result)

#result = where(lambda x: x % 2 == 0, result)
result = filter(lambda x: x % 2 == 0, result)
print(result)
#result = list(select(lambda x: (x, x**2), result))
result = list(map(lambda x: (x, x**2), result))
print(result)


list_1 = [x for x in range(1, 20)]
print(list_1)
list_1 = list(map(lambda x: x + 10, list_1))
print(list_1)


data = '9 2 3 5 8 15 23 38'
data = list(map(int, data.split()))
print(data)

"""
data = [9, 2, 3, 5, 8, 15, 23, 38, 55]
print(data)
data = list(filter(lambda x: x % 10 == 5, data))
print(data)
