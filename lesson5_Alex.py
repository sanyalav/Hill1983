# 1)
try:
    my_int = int(input("Введите целое число: "))
    my_str = str(my_int)
    count = 0
    for i in range(len(my_str)):
        if my_str[i] == "0":
            count += 1
    print("В этом числе нулей:", count)
except:
    print("Это не целое число")
###################################################
# 2)
try:
    my_int = int(input("Введите целое число: "))
    my_str = str(my_int)
    count = 0
    i = 1
    while my_str[-i] == "0":
        count += 1
        i += 1
    print("У этого числа в конце нулей:", count)
except:
    print("Это не целое число")
###################################################
# 3)
my_list_1 = [1,2,3,4,5]
my_list_2 = [10,15,20,25]
my_result = []
for i_1 in range(len(my_list_1)):
    if not my_list_1[i_1] % 2:
        my_result.append(my_list_1[i_1])
for i_2 in range(len(my_list_2)):
    if my_list_2[i_2] % 2:
        my_result.append(my_list_2[i_2])
print(my_result)
###################################################
# 4)
my_list = [1,2,3,4]
new_list = []
for i in range(len(my_list)):
    if i != 0:
        new_list.append(my_list[i])
new_list.append(my_list[0])
print(new_list)
###################################################
# 5)
my_list = [1,2,3,4]
my_list.append(my_list[0])
my_list.pop(0)
print(my_list)
###################################################
# 6)
my_str = "43 больше чем 34 но меньше чем 56"
a = my_str.split()
result = 0
print(a)
for i in range(len(a)):
  try:
    b = int(a[i])
    result += b
  except:
    pass
print(result)
###################################################
# 7)
my_str = input("Введите что-нибудь: ")
my_list = []
if len(my_str) % 2:
  my_str += "_"
for i in range(len(my_str)):
  a = my_str[i:i+2]
  my_list.append(a)
print(my_list[::2])
###################################################
# 8)
my_str = "abcdefghijklmnopqrstuvwxyz"
l_limit = input("Введите левую букву: ")
r_limit = input("Введите правую букву: ")
sub_str = ""
i = 0
try:
    while l_limit != my_str[i]:
        i += 1
    i += 1
    while r_limit != my_str[i]:
        sub_str += my_str[i]
        i +=1
    print("Между этими буквами находится:", sub_str)
except:
    print("Извините, что-то пошло не так!")
#####################################################
# 9)
my_str = "My long string"
l_limit = "o"
r_limit = "g"
sub_str = ""
for i in range(len(my_str)):
  if my_str[i] == l_limit:
    l = i+1
  elif my_str[i] == r_limit:
    r = i
sub_str = my_str[l:r]
print(sub_str)
#####################################################
# 10)
my_list = [2,4,1,5,3,9,0,7]
result = 0
i = 1
while i != len(my_list) - 1:
    if my_list[i] > my_list[i-1] + my_list[i+1]:
        result += 1
    i += 1
print(result)
