# 1)
import os
import string
import random
print("1)")
def create_domains_list():
    with open ("domains.txt", 'r') as file:
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
    with open ("names.txt", 'r') as file:
        data_1 = []
        for line in file.readlines():
            data_1.append(line.split()[1])
    print(data_1)
create_surnames_list()
#######################################################
# 3)
print("3)")
def create_email():
    with open ("domains.txt", 'r') as file:
        data = []
        for line in file.readlines():
            data.append(line.strip())
    with open ("names.txt", 'r') as file:
        data_1 = []
        for line in file.readlines():
            data_1.append(line.split()[1])
    my_symbol = ""
    rand_surname = random.randint(0,len(data_1))
    rand_number = random.randint(100,999)
    alphabet = string.ascii_lowercase
    for index in range(random.randint(5,7)):
        rand_symbol = random.randint(0,24)
        symbol = alphabet[rand_symbol:rand_symbol + 1]
        my_symbol += symbol
    rand_domain = random.randint(0,len(data))
    print(f"{data_1[rand_surname]}.{rand_number}@{my_symbol}{data[rand_domain]}")
create_email()