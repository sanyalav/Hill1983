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
    print(my_list)
create_domains_list()
#######################################################
# 2)
print("2)")
def create_surnames_list():
    with open("names.txt", 'r') as file:
        data_1 = []
        for line in file.readlines():
            data_1.append(line.split()[1])
    print(data_1)
create_surnames_list()
#######################################################
# 3)
print("3)")
def create_email():
    with open("domains.txt", 'r') as file:
        data = []
        for line in file.readlines():
            data.append(line.strip())
    with open("names.txt", 'r') as file:
        data_1 = []
        for line in file.readlines():
            data_1.append(line.split()[1])
    try:
        my_symbol = ""
        rand_surname = randint(0, len(data_1))
        rand_number = randint(100, 999)
        for symbol in range(randint(5, 7)):
            rand_symbol = chr(randint(97, 122))
            my_symbol += rand_symbol
        rand_domain = randint(0, len(data))
        print(f"{data_1[rand_surname]}.{rand_number}@{my_symbol}{data[rand_domain]}")
    except:
        pass
create_email()