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

menu = {1:'Открыть файл', 2:'Сохранить файл', 3:'Показать контакты',
        4:'Добавить контакт', 5:'Изменить контакт', 6:'Найти контакт',
        7:'Удалить контакт', 8: 'Выход'}

for key, value in menu.items():
    print(key, value)

#num = int(input('Выберите пункт меню: '))

#data = open('tel_dir.txt', 'a')
#with open('tel_dir.txt', 'a') as file:
#    data.write(key, value for key, value in menu.items())

name_list_1 = {'Berlin': '1234'}
name_list_2 = {'Oslo': '2345'}


#with open('listfile.txt', 'w') as filehandle:
  #  filehandle.writelines(f'{name_list_1}\n')
  #  filehandle.writelines(f'{name_list_2}\n')
 #   filehandle.readlines()
data_read = (open('listfile.txt', 'r'))
print(type(data_read))

#for line in data_read:
  #  print(line)
# for key, value in data_read.item():
#     print(key, value)
