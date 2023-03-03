import view
import phone

pb = phone.Phone_book()

def start_menu():
    while True:
        choice = view.main_menu()
        match choice:
            case 1:  # Открыть файл
                pb.open_file()
            case 2:  # Сохранить файл
                contacts = pb.phone_book
                pb.save_file(view.save_contact(contacts))
            case 3:  # Показать контакты
                book = pb.get()
                view.show_contact(book)
            case 4:  # Добавить контакт
                new_record = view.new_contact()
                pb.new_contact(new_record)
            case 5:  # Найти контакт
                word = view.input_request('искомый контакт')
                result = pb.search(word)
                view.show_contact(result)
            case 6:  # Изменить контакт
                new_value = view.change_contact(pb.get())
                pb.change(*new_value)
            case 7:  # Удалить контакт
                index = view.delete_contact(pb.get())
                pb.deiete(index)
            case 8: # Выход
                view.good_bye(pb.out())
                if pb.out() == 0:
                    break

