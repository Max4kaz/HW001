# Задайте строку из набора чисел. Напишите программу, которая покажет большее и меньшее число. В качестве символа-разделителя используйте пробел.

# numbers = input().split()
# numbers = list((map(int, numbers)))
# print(min(numbers), max(numbers), sep='\n')


user_string = input("Введите строку из чисел с разделителем в виде пробела: ").split(" ")
numbers = list(map(int, user_string))
print(max(numbers), min(numbers))

stroka = input("Введите строку чисел через пробел: ")
def min_max_value(input_str):
    list1 = input_str.split(' ')
    list2 = []
    for i in list1:
        list2.append(int(i))
    min = list2[0]
    max = list2[1]
    for i in list2:
        if i > max: max = i
        if i < min: min = i
    return (min, max)

print(min_max_value(stroka))



# Найдите корни квадратного уравнения Ax² + Bx + C = 0 двумя способами:
# 1) с помощью математических формул нахождения корней квадратного уравнения
# 2) с помощью дополнительных библиотек Python Задайте два числа.

a = int(input('Введите А: '))
b = int(input('Введите В: '))
c = int(input('Введите С: '))
x1 = 0
x2 = 0
d = b ** 2 - 4*a*c
if d > 0:
    x1 = (-b + sqrt(d)) / 2*a
    x2 = (-b - sqrt(d)) / 2*a
    print(x1)
    print(x2)
elif d == 0:
    x1 = -b / 2*a
    print(x1)
else: print('Корней нет')

from math import *

# другой вариант
from math import *


def square_root(a: int = 0, b: int = 0, c: int = 0) -> list:
    discriminant = (b ** 2) - (4 * a * c)
    if discriminant < 0:
        return []
    elif discriminant == 0:
        x = - (b / (2 * a))
        return [x]
    x1 = (-b + sqrt(discriminant)) / (2 * a)
    x2 = (-b - sqrt(discriminant)) / (2 * a)
    return [x1, x2]

print('Ax² + Bx + C = 0')
a = int(input('A= '))
b = int(input('B= '))
c = int(input('C= '))
print(square_root(a, b, c))

# Напишите программу, которая найдёт НОК (наименьшее общее кратное) этих двух чисел.

def NOK(a, b):
    for i in range(a, (a*b+1), a):
        for j in range(b, (a*b+1), b):
            if i == j:
                return(i)
a = int(input('Введите А:  '))
b = int(input('Введите B:  '))
print(NOK(a, b))

import math
a = int(input("a = "))
b = int(input("b = "))
print(math.lcm(a, b))

exit()
def NOD(a,b):
    while True:
        if a > b:
            a = a - b
        else:
            b = b - a

        if a % b == 0:
            return b
        elif b % a == 0:
            return a


def NOK(a:int, b:int) -> int:
        return int((a * b) / NOD(a,b))


print(NOK(126, 70))



exit()
def less_common_div(first_number: int, second_number: int) -> int:
    if first_number < second_number:
        temp = first_number
        first_number = second_number
        second_number = temp
    for i in range(2, first_number + 1):
        if (first_number % i == 0) and (i % second_number % i == 0):
            return i
    return None

print(less_common_div(int(input('Введите первое число ')), int(input('Введите второе число '))))


exit()
a = int(input("Введите число A: "))
b = int(input("Введите число B: "))

def nok_value(a: int = 0, b: int = 0):

    nok = 1
    while ((nok % a) + (nok % b) != 0):
        nok += 1
        print(nok)
    return nok

print(nok_value(a, b))