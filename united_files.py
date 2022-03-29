import os
import time

with open('1.txt', encoding='utf_8' ) as f1:
    text_1 = f1.read()
    n_1txt = 0 # n_1txt - количество строк в тексте 1
    for line in f1:
        n_1txt += 1

with open('2.txt', encoding='utf_8' ) as f2:
    text_2 = f2.read()
    n_2txt = 0 # n_2txt - количество строк в тексте 2
    for line in f2:
        n_2txt += 1

with open('3.txt', encoding='utf_8' ) as f3:
    text_3 = f3.read()
    n_3txt = 0 # n_3txt - количество строк в тексте 3
    for line in f3:
        n_3txt += 1

with open('united_file.txt', 'w', encoding='utf_8') as f:
    f.write('2.txt\n')
    f.write('1\n')
    f.write(f'{text_2}\n')
    f.write('1.txt\n')
    f.write('8\n')
    f.write(f'{text_1}\n')
    f.write('3.txt\n')
    f.write('9\n')
    f.write(f'{text_3}\n')
