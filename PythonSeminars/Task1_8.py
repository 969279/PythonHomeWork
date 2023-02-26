# Создать телефонный справочник с возможностью импорта и экспорта данных в формате .txt.
# Фамилия, имя, отчество, номер телефона - данные, которые должны находиться в файле.
# 1. Программа должна выводить данные
# 2. Программа должна сохранять данные в текстовом файле
# 3. Пользователь может ввести одну из характеристик для поиска определенной записи
#   (Например имя или фамилию человека)
# 4. Использование функций. Ваша программа не должна быть линейной

    # МЕНЮ
# 1. Открыть файл
# 2. Сохранить файл
# 3. Показать контакты
# 4. Добавить контакт
# 5. Изменить контакт
# 6. Найти контакт
# 7. Удалить контакт
# 8. Выход

# menu = {1:'Открыть файл', 2:'Сохранить файл', 3:'Показать контакты',
#         4:'Добавить контакт', 5:'Изменить контакт', 6:'Найти контакт',
#         7:'Удалить контакт', 8: 'Выход'}

# имя файла
# file_name = "messages.txt"
# определяем пустой список
# messages = list()

# for i in range(4):
#         message = input("Введите строку " + str(i + 1) + ": ")
#         messages.append(message + "\n")

# запись списка в файл
# with open(file_name, "a", encoding='utf-8') as file:
#         for message in messages:
#                 file.write(message)

# считываем сообщения из файла
content = []
def main_menu():
        print('Телефонный справочник. Выберите действие: \n'
        '1. Открыть файл\n'
        '2. Сохранить файл\n'
        '3. Показать контакты\n'
        '4. Добавить контакт\n'
        '5. Изменить контакт\n'
        '6. Найти контакт\n' 
        '7. Удалить контакт\n'
        '8. Выход')
        action = int(input('Введите номер действия: '))
        return action

while True:
        choice = main_menu()
        match choice:
                case 1:# Открыть файл
                        with open('text.txt', 'r', encoding='utf-8') as text:
                                content = text.readlines()
                                print(content)

                case 2:# Сохранить файл
                        if len(content) == 0:
                                print('Требуется сначала открыть файл.')
                        else:
                                with open('text.txt', 'w', encoding='utf-8') as text:
                                        for item in content:
                                                text.write(str(item))

                case 3:# Показать контакты
                        with open('text.txt', 'r', encoding='utf-8') as text:
                                content = text.readlines()
                                for line in content:
                                        line.split(',')
                                        print(line)

                case 4:# Добавить контакт
                        name = input('Введите имя: ')
                        fone = input('Введите номер телефона: ')
                        note = input('Введите примечание к номеру телефона: ')
                        message = [name, fone, note]
                        with open('text.txt', 'a', encoding='utf-8') as text:
                                 text.write(', '.join(message) + '\n')

                case 5:# Изменить контакт
                        name = input('Введите имя: ')
                        with open('text.txt', 'r', encoding='utf-8') as text:
                                content = text.readlines()
                                for i in range(len(content)):
                                        line = content[i].split(',')
                                        if line[0].strip() == name:
                                                print(content[i])

                case 6:# Найти контакт
                        name = input('Введите имя: ')
                        fone = input('Введите номер телефона: ')
                        with open('text.txt', 'r', encoding='utf-8') as text:
                                content = text.readlines()
                                for i in range(len(content)):
                                        line = content[i].split(',')
                                        if line[0].strip() == name or line[1].strip() == fone:
                                                print(f'Найден контакт, имя: {line[0]}, {line[2].strip()} телефон: {line[1]}')
                                                line = []
                                        else:
                                                line = []

                case 7:
                        print('Удалить контакт')
                case 8:
                        print('Выход')
                        break
