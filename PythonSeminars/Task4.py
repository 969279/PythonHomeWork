# Написать программу вывода уникальных значений из словаря

list_1 = [{"V": "S001"}, {"V": "S002"}, {"VI": "S001"},
          {"VI": "S005"}, {"VII": " S005 "},
          {" V ":" S009 "}, {" VIII ":" S007 "}]

set_key = set()
set_value = set()
print(list_1)

for new_dict in list_1:
    for key, value in new_dict.items():
        set_key.add(key.strip())
        set_value.add(value.strip())
print(set_value)
print(set_key)

#for i in range(len(list_1)):
#    print(*list_1[i].values())
#    set_1.add(*list_1[i].values())

