def main_menu() -> int:
    print('''Главное меню
    1. Открыть файл
    2. Сохранить файл
    3. Показать контакты
    4. Добавить контакт 
    5. Найти контакт
    6. Изменить контакт
    7. Удалить контакт
    8. Выход''')
    choise = int(input('Введите номер действия: '))
    return choise

def show_contact(phone_book): # показать контакты №3
    if phone_book:
        for i, contact in enumerate(phone_book, 1):
            print(f'{i}. {contact.get("name"):<20}'
                  f'{contact.get("phone"):<20}'
                  f'{contact.get("comment"):<20}')
    else:
        print('Телефонная книга не открыта или пуста.')

def new_contact():# Добавить контакт п.4
    name = input('Введите имя: ')
    phone = input('Введите номер телефона: ')
    comment = input('Введите комментарий: ')
    return {'name': name, 'phone': phone, 'comment': comment}

def input_request(text: str) -> str:# Найти контакт п.5
    return input(f'Введите {text}: ')

def change_contact(book: list) -> tuple:# Изменить контакт п.6
    show_contact(book)
    choise = int(input('Введите контакт который хотите изменить: '))
    name = input('Введите имя: ')
    phone = input('Введите телефон: ')
    comment = input('Введите комментарий: ')
    return choise - 1, {'name': name if name else book[choise - 1].get('name'),
                        'phone': phone if phone else book[choise - 1].get('phone'),
                        'comment': comment if comment else book[choise - 1].get('comment')}

def delete_contact(book: list):# Удалить контакт п.5
    show_contact(book)
    return int(input('Выберите контакт для удаления:')) - 1

def good_bye():
    print('Телефонный справочник закрыт. До свидания!')



