# Напишите программу, которая принимает на вход строку,
# и отслеживает, сколько раз каждый символ уже встречался.
# Количество повторов добавляется к символам с помощью постфикса формата _n.

# d g h t r g r h t j h b v f d s d f

# d g h t r g_2 r_2 h_2 t_2 j h_3 b v f d_2 s d_3 f_2

simbol = 'd g h t r g r h t j h b v f d s d f'

list_1 = simbol.split()
print(list_1)
dict_1 = {}
new_list = []

for letter in list_1:
    dict_1[letter] = dict_1.get(letter, 0) + 1
    if dict_1.get(letter) > 1:
        new_list.append(letter + '_' + str(dict_1.get(letter)))
    else:
        new_list.append(letter)

print(' '.join(new_list))
