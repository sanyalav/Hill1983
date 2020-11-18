# 1)
value = int(input("Введите любое целое число: "))
new_value = value / 2 if value < 100 else -value
print(new_value)
##################################################
# 2)
value = int(input("Введите любое целое число: "))
new_value = 1 if value < 100 else 0
print(new_value)
##################################################
# 3)
value = int(input("Введите любое целое число: "))
new_value = 1 if value < 100 else 0
print(bool(new_value))
##################################################
# 4)
my_str = input("Введите что-нибудь: ")
my_str1 = my_str.upper()
print(my_str1)
##################################################
# 5)
my_str = input("Введите что-нибудь: ")
my_str1 = my_str.lower()
print(my_str1)
##################################################
# 6)
my_str = input("Введите что-нибудь: ")
new_str = my_str * 2 if len(my_str) < 5 else my_str
print(new_str)
##################################################
# 7)
my_str = input("Введите что-нибудь: ")
new_str = my_str + my_str [::-1] if len(my_str) < 5 else my_str
print(new_str)
##################################################
# 8)
my_str = input("Введите что-нибудь: ")
for new_str in my_str:
    if new_str.isalnum():
        print(new_str)
##################################################
# 9)
my_str = input("Введите что-нибудь: ")
for new_str in my_str:
    if not new_str.isalnum():
        print(new_str)
##################################################
# 10)
my_str = input("Введите что-нибудь: ")
for new_str in my_str:
    if not new_str.isalnum() and not new_str.isspace():
        print(new_str)










