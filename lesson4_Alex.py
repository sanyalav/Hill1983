# 1)
my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
for new_list in my_list:
  if new_list > 100:
    print(new_list)
############################################################################
# 2)
my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144, 233, 377, 610, 987, 1597]
my_results = []
for new_list in my_list:
  if new_list > 100:
    my_results.append(new_list)
print(my_results)
############################################################################
# 3)
my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
if len(my_list) < 2:
    my_list.append(0)
    print(my_list)
else:
    my_list.append(my_list[-1] + my_list[-2])
    print(my_list)
############################################################################
# 4)
value = input("Введите число с точкой: ")
try:
    value = float(value)
    print(value ** -1)
except ZeroDivisionError:
    print("Ошибка деление на 0")
except ValueError:
    print("Это совсем не число")
############################################################################
# 5)
my_list = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in my_indexes:
    print(my_list[index])
############################################################################
# 6)
my_list_1 = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
my_list_2 = [89, 144, 233, 377, 610, 987, 1597, 2584, 4181, 6765, 10946]
my_indexes = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for index in my_indexes:
    print("(", my_list_1[index],",", my_list_2[index], ")")
############################################################################
# 7)
my_string_1 = "0123456789"
my_string_2 = "0123456789"
result = []
for symb_1 in my_string_1:
    for symb_2 in my_string_2:
        result.append(int(symb_1 + symb_2))
print(result)

