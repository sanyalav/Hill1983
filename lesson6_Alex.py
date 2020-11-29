# 1)
print("1)")
my_list = ["qwerty", "internet", "asdfgh", "superpuper", "twenty", "blablabla", "123456" ]
print(my_list)
new_list = []
for index, value in enumerate(my_list):
    if not index % 2:
        new_list.append(value)
    else:
        new_list.append(value[::-1])
print(new_list)
##########################################################################################
# 2)
print("2)")
my_list = ["qwerty", "internet", "asdfgh", "asuperpuper", "twenty", "ablablabla", "123456" ]
print(my_list)
new_list = []
for element in my_list:
    if element[0] == "a":
        new_list.append(element)
print(new_list)
##########################################################################################
# 3)
print("3)")
my_list = ["qwerty", "interneta", "asdfgh", "superpuper", "twenty", "blablabla", "123456" ]
print(my_list)
new_list = []
template = "a"
for element in my_list:
    if template in element:
        new_list.append(element)
print(new_list)
##########################################################################################
# 4)
print("4)")
my_list = ["qwerty", 123456, "abcdef", "internet", 555555, "098765"]
print(my_list)
new_list = []
for element in my_list:
    if type(element) == str:
        new_list.append(element)
print(new_list)
##########################################################################################
# 5)
print("5)")
my_str = "qwertyblablainternet12345555"
my_list = []
print(my_str)
for symbol in my_str:
    count = my_str.count(symbol)
    if count == 1:
        my_list.append(symbol)
print(my_list)
#########################################################################################
# 6)
print("6)")
my_str1 = "qwertyblablainternet12345555"
my_str2 = "suvxz098763jjopqtrsmnvcxzopy"
my_set1 = set(my_str1)
my_set2 = set(my_str2)
print(my_set1)
print(my_set2)
intersect = my_set1.intersection(my_set2)
my_list = list(intersect)
print(my_list)
#########################################################################################
# 7)
print("7)")
my_str1 = "qwertyblablainternet12345555"
my_str2 = "suvxz098763jjopqtrsmnvcxzopy"
my_list1 = []
my_list2 = []
print(my_str1)
for symbol in my_str1:
    count = my_str1.count(symbol)
    if count == 1:
        my_list1.append(symbol)
print(my_list1)
print(my_str2)
for symbol in my_str2:
    count = my_str2.count(symbol)
    if count == 1:
        my_list2.append(symbol)
print(my_list2)
my_set1 = set(my_list1)
my_set2 = set(my_list2)
intersect = my_set1.intersection(my_set2)
my_list = list(intersect)
print(my_list)
##############################################################################
# 8)
print("8)")
address = {"Страна": "Украина",
           "Город": "Одесса",
           "Улица": "Пушкина"}
work = {"Наличие": "Есть",
        "Должность": "Бухгалтер"}
person = {"Фамилия": "Иванов",
          "Имя": "Иван",
          "Возраст": 35,
          "Проживание": address,
          "Работа": work}
print(person)
##############################################################################
# 9)
print("9)")
korj = {"Мука": 500,
        "Молоко": 200,
        "Масло": 50,
        "Яйцо": 30}
krem = {"Сахар": 30,
        "Масло": 40,
        "Ваниль": 5,
        "Сметана": 70}
glazur = {"Какао": 60,
          "Сахар": 40,
          "Масло": 30}
tort = {"Корж": korj,
        "Крем": krem,
        "Глазурь": glazur}
print(tort)