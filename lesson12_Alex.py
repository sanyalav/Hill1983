import requests
from random import randint
import csv
import json
import os
import re

# 1)

print("1)")

my_list = []

def create_quote():
    key = randint(1, 100)
    url = "http://api.forismatic.com/api/1.0/"
    params = {"method": "getQuote",
              "format": "json",
              "key": key,
              "lang": "ru"}
    r = requests.get(url, params=params)
    quote = r.json()
    quote_text = quote["quoteText"]
    quote_author = quote["quoteAuthor"]
    return [quote_text, quote_author]

def create_quote_list(number):
    item = 1
    while item < number + 1:
        quotes = create_quote()
        if quotes[1] != "" and quotes not in my_list:
            my_list.append(quotes)
            item += 1
    print(my_list)
    return my_list

list_my = create_quote_list(10)

def sort_quote_list():
    sorted_list = sorted(list_my, key=lambda name: name[1])
    print(sorted_list)
    return sorted_list

list_sorted = sort_quote_list()

def write_csv_file(filename="quotes.csv"):
    with open(filename, "w", encoding="UTF-8", newline = "") as csv_file:
        writer = csv.writer(csv_file)
        writer.writerows(list_sorted)

result = write_csv_file()

# 2)

print("2)")

date_list = []
name_list = []
sub_list = []
correct_date_list = []
dict_list = []

def read_file(filename="authors.txt"):
    with open(filename, "r") as file:
        data = []
        for line in file.readlines():
            if len(line.split()) > 1:
                data.append(line.strip())
    print(data)
    return data

my_list = read_file()

def create_date_list():
    for element in my_list:
        if "'s" in element:
            sub_date = element[:element.rfind("-")]
            date_list.append(sub_date)
    print(date_list)
    return date_list

list_date = create_date_list()

def create_name_list():
    for element in my_list:
        if "'s" in element:
            sub_name = element[element.find("-") + 2 : element.find("'s")]
            name_list.append(sub_name)
    print(name_list)
    return name_list

list_name = create_name_list()

def create_sub_list():
    month = "January"
    number = 1
    for date in list_date:
        if date.split()[1] == month:
            date_ = date.replace(date.split()[1], str(number))
            sub_list.append(date_)
        else:
            date_ = date.replace(date.split()[1], str(number + 1))
            month = date.split()[1]
            number += 1
            sub_list.append(date_)
    print(sub_list)
    return sub_list

list_sub = create_sub_list()

def replace_date():
    pattern = r"[0-9]+"
    for numbers in list_sub:
        result = re.findall(pattern, numbers)
        new_date = f"{result[0]}/{result[1]}/{result[2]}"
        correct_date_list.append(new_date)
    print(correct_date_list)
    return correct_date_list

correct_list = replace_date()

def create_dict_list():
    for index in range(len(correct_list)):
        date = correct_date_list[index]
        name = name_list[index]
        my_dict = {"date": date, "name": name}
        dict_list.append(my_dict)
    print(dict_list)
    return dict_list

list_dict = create_dict_list()

def write_json_file(filename="result.json"):
    with open(filename, "w") as file:
        json.dump(list_dict, file)

my_file = write_json_file()