# 1)
import os
from random import randint
print("1)")
def create_domains_list():
    with open("domains.txt", 'r') as file:
        data = []
        my_list = []
        for line in file.readlines():
            data.append(line.strip())
        for element in data:
            new_element = element.replace(".", "")
            my_list.append(new_element)
    return my_list
domains_list = create_domains_list()
print(domains_list)
#######################################################
# 2)
print("2)")
def create_surnames_list():
    with open("names.txt", 'r') as file:
        data_1 = []
        for line in file.readlines():
            data_1.append(line.split()[1])
    return data_1
surnames_list = create_surnames_list()
print(surnames_list)
#######################################################
# 3)
print("3)")
def create_email():
    try:
        my_symbol = ""
        rand_surname = randint(0, len(surnames_list))
        rand_number = randint(100, 999)
        for symbol in range(randint(5, 7)):
            rand_symbol = chr(randint(97, 122))
            my_symbol += rand_symbol
        rand_domain = randint(0, len(domains_list))
        my_email = f"{surnames_list[rand_surname]}.{rand_number}@{my_symbol}.{domains_list[rand_domain]}"
        return my_email
    except:
        pass
print(create_email())