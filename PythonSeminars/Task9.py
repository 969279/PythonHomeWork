# Классы и объекты

class Car:
    def __init__(self, model:str, color: str, year: int, volume: float):
        self.model = model
        self.color = color
        self.year = year
        self.volume = volume
    def gas(self):
        print('Ббррррр-бррр')
    def present(self):
        return print(f' Это автомобиль: {self.model}, {self.year} года, цвет: {self.color}')
    def __str__(self):
        return f' Это автомобиль: {self.model}, {self.year} года, цвет: {self.color}'

ferrari = Car('F355', 'red', 2016, 6.0)
bmw = Car('X6', 'blak', 2019, 5.2)

# print(ferrari.model)
# print(ferrari.year)
# ferrari.type = 'Спорт'
# print(ferrari.type)
# ferrari.gas()
# print()
# print(bmw.model)
# print(bmw.year)
# print(bmw.color)
# bmw.color = 'geen'
# print(bmw.color)

print(ferrari)
bmw.present()


