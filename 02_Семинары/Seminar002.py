# i = 1
# while i < 11:
#     print(i)
#     i += 1
# # continue    - не дает продолжать дальше
# else:
#     print('Hi!')

# while (i:=input('-> ')) != '2':
#     print('NO')
# else:
#     print('Good')

# 1. Напишите программу, которая принимает на вход число N и выдаёт
# последовательность из N членов. 
#     *Пример:*  
#     - Для N = 5: 1, -3, 9, -27, 81

# n = int(input("Введите число N: "))
temp = 0

# for i in range(1, n+1):
#     print(i, end=', ')
#     i *= -3
#print('Для N =', n, i, end=' ,')



# 2. Для натурального n создать словарь индекс-значение, состоящий из 
# элементов последовательности 3n + 1.
    
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}

#     - Для n = 6: 
#         1: 4,
#         2: 7, 
#         3: 10, 
#         4: 13, 
#         5: 16, 
#         6: 19

# 3. Напишите программу, в которой пользователь будет задавать две строки, 
# а программа - определять количество вхождений одной строки в другой.
# "Я люблю питон!"
# "лю" -> 2

# srting1 = str(input("Введите строку 1: "))
# srting2 = str(input("Введите строку 2: "))
# S.find(str, [start],[end])

# if (b == a*a) or (a == b*b):
#     print("да")
# else:
#     print("нет")

# sentence = "Я люблю питон!"
# index = sentence.find("лю")
# print(index)

string = 'Я люблю лютерансие лютики'
t = 'лю'
i = 0
for first in range(len(string) - len(t) + 1):
    if string[first:first+len(t)] == t:
        i += 1
print(i)


str1 = input('Введите строку 1: ')
str2 = input('Введите строку 2: ')
print(len(str1.split(str2)) - 1)

exit()
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
