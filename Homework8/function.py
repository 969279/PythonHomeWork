import config
def main_menu():
     print('Телефонный справочник. Выберите действие: \n'
          '1. Открыть файл \n'
          '2. Сохранить файл\n'
          '3. Показать контакты\n'
          '4. Добавить контакт\n'
          '5. Изменить контакт\n'
          '6. Найти контакт\n'
          '7. Удалить контакт\n'
          '8. Выход')
     if len(config.content) != 0:
         print('Открыт файл: text.txt')
     action = int(input('Введите номер действия: '))
     return action

def open_file():
    with open('text.txt', 'r', encoding='utf-8') as text:
        config.content = text.readlines()
        return config.content
def save_file(item):
    if len(item) == 0:
        print('Требуется сначала открыть файл.')
    else:
        with open('text.txt', 'w', encoding='utf-8') as text:
            for i in item:
                text.write(str(i))
        config.content = []
def show_contact():
    with open('text.txt', 'r', encoding='utf-8') as text:
        content = text.readlines()
        for line in content:
            line.split(',')
            print(line)
def add_fone():# Добавить контакт
    name = input('Введите имя: ')
    fone = input('Введите номер телефона: ')
    note = input('Введите примечание к номеру телефона: ')
    message = [name, fone, note]
    with open('text.txt', 'a', encoding='utf-8') as text:
        text.write(', '.join(message) + '\n')
def change_contact():# Изменить контакт
    count = 0
    if len(config.content) == 0:
        print('Требуется сначала открыть файл.')
    else:
        name = input('Введите имя: ')
        for i in range(len(config.content)):
            line = config.content[i].split(',')
            if line[0].strip() == name:
                fone = input('Введите новый номер телефона: ')
                note = input('Введите примечание: ')
                line[1] = fone
                line[2] = note
                message = [name, fone, note]
                config.content[i] = (', '.join(message) + '\n')
                print(f'Изменен контакт: {config.content[i]} Требуется сохранить файл.')
                count += 1
        if count == 0:
            print('Контакт не найден')
def find_contact():# Найти контакт
    value = input('Введите имя или номер телефона: ')
    count = 0
    with open('text.txt', 'r', encoding='utf-8') as text:
        find = text.readlines()
        for i in range(len(find)):
            line = find[i].split(',')
            if line[0].strip() == value or line[1].strip() == value:
                print(f'Найден контакт, имя: {line[0]}, {line[2].strip()} телефон:{line[1]}')
                count += 1
        if count == 0:
            print('Контакт не найден')
def delete_contact():# Удалить контакт
    if len(config.content) == 0:
        print('Требуется сначала открыть файл.')
    else:
        name = input('Введите имя: ')
        count = 0
        for i in range(len(config.content)):
            line = config.content[i].split(',')
            if line[0].strip() == name:
                print(f'Удален контакт: {config.content[i]} Требуется сохранить файл.')
                config.content.pop(i)
                count += 1
        if count == 0:
            print('Контакт не найден')
