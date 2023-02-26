from function import *
import config

while True:
    choice = main_menu()
    match choice:
        case 1:# Открыть файл
            open_file()
        case 2:# Сохранить файл
            save_file(config.content)
        case 3:# Показать контакты
            show_contact()
        case 4:# Добавить контакт
            add_fone()
        case 5:# Изменить контакт
            change_contact()
        case 6:# Найти контакт
            find_contact()
        case 7:# Удалить контакт
            delete_contact()
        case 8:
            print('Выход')
            break

