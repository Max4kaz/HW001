# my_age = int(input("Введите возраст: "))
# print("Вамtype(my_age))
# 10

# 1. Напишите программу, которая принимает на вход два числа и проверяет,
# является ли одно число квадратом другого.

#     *Примеры:*

#     - 5, 25 -> да
#     - 4, 16 -> да
#     - 25, 5 -> да
#     - 8,9 -> нет

# a = int(input("Введите число 1: "))
# b = int(input("Введите число 2: "))

# if (b == a*a) or (a == b*b):
#     print("да")
# else:
#     print("нет")

# my_list = [8, 'r', 7, True]
# print(my_list)

# range(5)          -> [0, 1, 2, 3, 4] до правой границы невключительно!!!
# range(1, 11)      -> [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# range(1, 10, 2)   -> [1, 3, 5, 7, 9]

# for i in range(1, 10,2):
#     print(i, end=', ')

# переменные +
# встроенные функции: print(), input(), int(), str()
# условия +
# списки
# for, range(), len()
# while

# 1. Напишите программу, которая на вход принимает 5 чисел и находит максимальное из них.
#     Примеры:
#     - 1, 4, 8, 7, 5 -> 8
#     - 78, 55, 36, 90, 2 -> 90

a_1 = int(input('Введите 1 число:'))
a_2 = int(input('Введите 2 число:'))
a_3 = int(input('Введите 3 число:'))
a_4 = int(input('Введите 4 число:'))
a_5 = int(input('Введите 5 число:'))
max = a_1
if max > a_2:
    max = a_2
if max > a_3:
    max = a_3
if max > a_4:
    max = a_4
else:
    max = a_5
print(max)

# Задача 1
amount_of_numbers = 5
number_list = []
# Николай - это Николай
# Это вам не это
for i in range(amount_of_numbers):
    number_list.append(int(input("Введите число: ")))

max_number = number_list[0]

for number in range(1, amount_of_numbers):
    if max_number < number_list[number]:
        max_number = number_list[number]

print(max_number)


# 2. Напишите программу, которая будет на вход принимать число N и выводить числа от -N до N
#     *Примеры:*
#     - 5 -> -5, -4, -3, -2, -1, 0, 1, 2, 3, 4, 5
n = int(input("Введите число N: "))
for i in range(-n, n+1):
    print(i, end=', ')

# Задача 2
n = int(input("ВВедите число N: "))
for i in range(-n, n + 1):
    print(i, end=' ')

print(list(range(-n, n + 1)))

# 3. Напишите программу, которая будет принимать на вход дробь и показывать первую цифру дробной части числа.
#     *Примеры:*
#     - 6,78 -> 7
#     - 5 -> нет
#     - 0,34 -> 3
number = int((float(input('Введите дробное число ')) * 10) % 10)
if number == 0:
    print('Нет')
else:
    print(number)

# Задача 3
x = float(input())
print(int(x * 10) % 10)

# Задача 3
x = input()
print(x.split('.')[1][0])


# 4. Напишите программу, которая принимает на вход число и проверяет, кратно ли оно (5 и 10) или (15, но не 30).
x = int(input('введите число '))
if (x % 5 == 0) and (x % 10 == 0):
    print('кратно 5 и 10')
if (x % 15 == 0) and (x % 30 != 0):
    print('кратно 15 но не 30')

# Задача 4
a = int(input('Введите число: '))
if ((a % 5 == 0) and (a % 10 == 0)) or ((a % 15 == 0) and (a % 30 != 0)):
    print("Yes")
else:
    print("No")

Дискорд:    https://discord.gg/3RPN3MGK
Телеграм:    @slavalk
Та самая соц. сеть:     @tochno_slava


# day_of_week = int(input("Проверь,является ли день выходным \nВведите номер дня: "))
# def check_day(num_day):
#     match num_day:
#         case 1 :
#             print("Нет")
#         case 2 :
#             print("Нет")
#         case 3 :
#             print("Нет")
#         case 4 :
#             print("Нет")
#         case 5 :
#             print("Нет")
#         case 6 :
#             print("Да")
#         case 7 :
#             print("Да")
#         case default :
#             print("Неверный номер дня")

# check_day(day_of_week)