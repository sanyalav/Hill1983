import os
import json
import csv
from random import randint
def create_txt():
    """ Create random text"""
    signs = ".,!:?;.,!?"
    my_text = ""
    text_length = randint(100, 1000)
    while len(my_text) < text_length:
        a = randint(1,10)
        b = randint(1,10)
        if a % 2 == 1:      # берет половину случайных значений для генерации чисел или слов
            for number in range(a):
                my_text += chr(randint(48, 57))   # генерация чисел
        else:
            for symbol in range(b):
                if b > 7 and symbol == 0:   # просто берет 3 случайных значения
                    my_text += "\n"
                    my_text += chr(randint(97, 122)).upper()   # генерация перевода строки и слов с большой буквой
                elif b < 4 and symbol == 0:  # берет 3 других случайных значения
                    my_text += chr(randint(97, 122)).upper()   # генерация слов с первой буквой большой
                else:                         # берет оставшиеся значения
                    my_text += chr(randint(97, 122))  # генерация слов с маленькими буквами
        my_text += signs[a:a+1]   # добавляет в конце слова случайный знак препинания
        my_text += " "            # слова отделяются пробелами
    return my_text
new_text = create_txt()
def create_json():
    """ Create random dict"""
    my_dict = {}
    my_key = ""
    c = randint(5, 20)
    for key in range(c):
        for symbol in range(5):
            my_key += chr(randint(97, 122))
        d = randint(1,3)    # чтобы получить случайным образом значения с равными вероятностями 1:3
        if d == 1:
            value = randint(-100, 100)
        elif d == 2:
            value = randint(0, 100)/100
        else:               # если d == 3
            value = bool(randint(0,1))
        my_dict.update({my_key:value})
        my_key = ""
    return my_dict
new_json = create_json()
def create_csv():
    """ Create random list of lists for table"""
    my_column_list = []
    my_list = []
    n = randint(3, 10)    # генерирует ряды
    m = randint(3, 10)    # генерирует столбцы
    # print(f"Rows: {n}, Columns: {m}")
    for row in range(n):
        for column in range(m):
            v = randint(0, 1)
            my_column_list.append(v)
        my_list.append(my_column_list)
        my_column_list = []
    return my_list
new_csv = create_csv()
def generate_and_write_file(filename):
    """ Generate and write different files depends on user's request"""
    if ".txt" in filename:
        print(new_text)
        with open(filename, "w") as file:
            file.write(new_text)
    elif ".json" in filename:
        print(new_json)
        with open(filename, "w") as file:
            json.dump(new_json, file)
    elif ".csv" in filename:
        print(new_csv)
        with open(filename, "w", newline = "") as csv_file:
            writer = csv.writer(csv_file)
            writer.writerows(new_csv)
    else:
        print("Unsupported file format")
filename = input("Input file name: ")
generate_and_write_file(filename)