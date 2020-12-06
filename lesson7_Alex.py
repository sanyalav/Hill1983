# 1)
from random import randint
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
triangle = {"A":randomize(), "B":randomize(), "C":randomize()}
print(triangle)
##########################################################
# 3)
print("3)")
def my_print():
    return f"***{my_str}***"
my_str = "I am the string"
print(my_print())
##########################################################
# 4)
print("4)")
persons = [{"name": "John", "age": 35},
           {"name": "Jack", "age": 15},
           {"name": "Tom", "age": 16},
           {"name": "Axe", "age": 15}]
min_age_list = []
min_age = min(person["age"] for person in persons)
[min_age_list.append(person["name"]) for person in persons if person["age"] == min_age]
print("Самые молодые люди:", min_age_list)
longest_name_list = []
longest_name = max(len(person["name"]) for person in persons)
[longest_name_list.append(person["name"]) for person in persons if len(person["name"]) == longest_name]
print("Самое длинное имя:", longest_name_list)
sum_age = 0
for person in persons:
    age = person.get("age")
    sum_age += age
print(f"Средний возраст людей: {sum_age/len(persons)} лет")
###########################################################
# 5)
print("5)")
my_dict_1 = {"A": 10, "B": 15, "C": 20, "D": 25}
my_dict_2 = {"E": 30, "B": 35, "F": 40, "C": 45}
same_keys = list(set(my_dict_1.keys()).intersection(my_dict_2.keys()))
print("Список общих ключей:", same_keys)
diff_keys = list(set(my_dict_1.keys()).difference(my_dict_2.keys()))
print("Список ключей, которые есть в первом списке, но нет во втором:", diff_keys)
new_dict = {key: my_dict_1[key] for key in diff_keys}
print("Новый словарь:", new_dict)
my_dict_3 = list(my_dict_1.keys() ^ my_dict_2.keys())
print(my_dict_3)
new_dict_1 = {key: value for key, value in my_dict_1.items() if key in my_dict_3}
print(new_dict_1)
new_dict_2 = {key: value for key, value in my_dict_2.items() if key in my_dict_3}
print(new_dict_2)
same_keys_dict = {key: [my_dict_1[key], my_dict_2[key]] for key in same_keys}
print(same_keys_dict)
merge_dict = {**new_dict_1, **new_dict_2, **same_keys_dict}
print("Объединенный список:", merge_dict)