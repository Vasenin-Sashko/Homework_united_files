from ntpath import join


res_count = {}
res_count_text = {}
n_1txt = 0 # n_1txt - количество строк в тексте 1
n_2txt = 0 # n_2txt - количество строк в тексте 2
n_3txt = 0 # n_3txt - количество строк в тексте 3

with open('1.txt', encoding='utf_8' ) as f1, open('2.txt', encoding='utf_8' ) as f2, open('3.txt', encoding='utf_8' ) as f3:
    text_1 = f1.readlines()
    for line in text_1:
        n_1txt += 1
    res_count['1.txt'] = n_1txt
    res_count_text['1.txt'] = text_1
    
    text_2 = f2.readlines()
    for line in text_2:
        n_2txt += 1
    res_count['2.txt'] = n_2txt
    res_count_text['2.txt'] = text_2

    text_3 = f3.readlines()
    for line in text_3:
        n_3txt += 1
    res_count['3.txt'] = n_3txt
    res_count_text['3.txt'] = text_3

# Отсортируем словарь "sorted_res_count" по значению количества строк
sorted_values = sorted(res_count.values())
sorted_res_count = {}

for i in sorted_values:
    for k in res_count.keys():
        if res_count[k] == i:
            sorted_res_count[k] = res_count[k]
            break

# Преобразуем словарь "sorted_res_count" в список
sorted_list =[]
for key, value in sorted_res_count.items():
    sorted_list.append(key)
    sorted_list.append(value)

# Отсортируем словарь "res_count_text" в соответсвии со словарем "sorted_res_count" по ключу
res_count_text_sortes = {}
for ks in sorted_res_count.keys():
    for kr in res_count_text.keys():
        if ks == kr:
            res_count_text_sortes[ks] = res_count_text[kr]
            break

# Преобразуем словарь "res_count_text_sortes" в список c текстами в необходимом для задания порядке
res_count_text_list =[]
for key, value in res_count_text_sortes.items():
    res_count_text_list.append(value)

# Преобразуем список текстов "res_count_text_list" в строки
text_sort_1 = ' '.join(res_count_text_list[0])
text_sort_2 = ' '.join(res_count_text_list[1])
text_sort_3 = ' '.join(res_count_text_list[2])

# Запишем текст в новый файл согласно заданию
with open('united_file.txt', 'w', encoding='utf_8') as f:
    f.write(f'{sorted_list[0]}\n')
    f.write(f'{sorted_list[1]}\n')
    f.write(f'{text_sort_1}\n')
    f.write(f'{sorted_list[2]}\n')
    f.write(f'{sorted_list[3]}\n')
    f.write(f'{text_sort_2}\n')
    f.write(f'{sorted_list[4]}\n')
    f.write(f'{sorted_list[5]}\n')
    f.write(f'{text_sort_3}\n')