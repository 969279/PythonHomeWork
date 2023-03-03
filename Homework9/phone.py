
class Phone_book:

    def __init__(self, path: str = 'data.txt'):
        self.path = path
        self.phone_book = []
        self.old_book = []

    def open_file(self):# Открыть файл п.1
        with open(self.path, 'r', encoding='utf-8') as file:
            data = file.readlines()
        for contact in data:
            phone_name = {}
            new = contact.strip().split(';')
            phone_name['name'] = new[0]
            phone_name['phone'] = new[1]
            phone_name['comment'] = new[2]
            self.phone_book.append(phone_name)
            self.old_book.append(phone_name)


    def save_file(self, messege: str):# Сохранить файл, п.2
        if messege:
            with open(self.path, 'w', encoding='utf-8') as file:
                file.write(messege)
                self.phone_book = []
        else:
            print('Файл не открыт')

    def get(self):# Показать контакты п.3
        return self.phone_book

    def new_contact(self, contact: dict):# Добавить контакт п.4
        self.phone_book.append(contact)
        print(f'\nКонтакт {contact.get("name")} записан.\n')

    def search(self, word: str) -> list | dict: # Найти контакт п.5
        result = []
        for contact in self.phone_book:
            for field in contact.values():
                if word in field:
                    result.append(contact)
        return result

    def change(self, i: int, new_value: dict): # Изменить контакт п.6
        self.phone_book[i] = new_value

    def deiete(self, i: int): # Удалить контакт п.7
        contact = self.phone_book.pop(i)
        print(f'Контакт {contact.get("name")} удален.')

    def old(self):
        return self.old_book

    def out(self):
        count = 0
        if range(len(self.phone_book)) == range(len(self.old_book)):
            for i in range(len(self.old_book)):
                res = all((self.old_book[i].get(key) == value for key, value in self.phone_book[i].items()))
                #print(res)
                if res == False:
                    count += 1
        return count
