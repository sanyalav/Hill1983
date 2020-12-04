# 1)
from random import randint  # загрузил не весь модуль, а только нужный randint
print("1)")
my_list = []
for index in range(20):
    my_list.append(randint(1,100))
print(my_list)
##########################################################
# 2)
print("2)")
def randomize():
    return (randint(-10, 10), randint(-10,10))
    # объединил две строки 12 и 13 в одну
triangle = {"A":randomize(), "B":randomize(), "C":randomize()}
print(triangle)
##########################################################
# 3)
print("3)")
def my_print():
    return f"***{my_str}***"
    # объединил две строки 20 и 21 в одну и сделал через f-строку
my_str = "I am the string"
print(my_print())
##########################################################
# 4)
print("4)")
persons = [{"name": "John", "age": 16},
           {"name": "Jack", "age": 15},
           {"name": "Tomiiii", "age": 16},
           {"name": "Axe", "age": 15}]
name_list_a = ["I"]
name_list_b = ["I"]
age_list = [200]
sum_age = 0
for index in range(len(persons)):
    if persons[index]['age'] < age_list[0]:
        age_list.pop()
        name_list_a.pop()
        age_list.append(persons[index]['age'])
        name_list_a.append(persons[index]['name'])
    elif persons[index]['age'] == age_list[0]:
        name_list_a.append(persons[index]['name'])
    if len(persons[index]['name']) > len(name_list_b[0]):
        name_list_b.pop()
        name_list_b.append(persons[index]['name'])
    elif len(persons[index]['name']) == len(name_list_b[0]):
        name_list_b.append(persons[index]['name'])
    sum_age += persons[index]['age']
print("a) Самые молодые люди:", name_list_a)
print("b) Самые длинное имя:", name_list_b)
print("c) Среднее количество лет:", sum_age / len(persons))
###############################################################
# 5)
print("5)")
my_dict_1 = {"A": 100, "B": 150, "D": 200, "E": 500}
my_dict_2 = {"D": 250, "E": 300, "B": 350, "F": 400}
my_list_a = []
my_list_b = []
my_list_c = []
new_dict = {}
my_dict_3 = {}
my_dict_4 = {}
x = -2    # Это счетчики, чтобы взять срез списка из двух значений [0,2]..[2,4] и т.д
z = 0     #
my_list_1 = list(my_dict_1)
my_list_2 = list(my_dict_2)
for index_1 in range(len(my_list_1)):
   for index_2 in range(len(my_list_2)):
       if my_list_1[index_1] == my_list_2[index_2]:
           my_list_a.append(my_list_1[index_1])
           a1 = my_dict_1.get(my_list_1[index_1])
           b1 = my_dict_2.get(my_list_2[index_2])
           c1 = my_list_1[index_1]
           my_list_c.append(a1)
           my_list_c.append(b1)
           x += 2    # Счетчики для среза
           z += 2    #
           d1 = {c1:my_list_c[x:z]}   # Здесь срез
           my_dict_4.update(d1)
print(my_list_a)
print(my_list_c)
print(my_dict_4)
for index in range(len(my_list_1)):
    if my_list_1[index] not in my_list_2:
        my_list_b.append(my_list_1[index])
print(my_list_b)
for index in range(len(my_list_b)):
    if my_list_b[index] in my_dict_1:
        a = my_list_b[index]
        b = my_dict_1.get(my_list_b[index])
        c = {a:b}
        new_dict.update(c)
print(new_dict)
my_dict_3.update(my_dict_1)
my_dict_3.update(my_dict_2)
my_dict_3.update(my_dict_4)
print(my_dict_3)


