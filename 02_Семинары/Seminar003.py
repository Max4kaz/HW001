# 1. Реализуйте алгоритм задания случайных чисел без использования встроенного генератора псевдослучайных чисел.

import time


def my_random(minn, maxx):
    time.sleep(0.3)
    return int((time.time() % 1 * (maxx - minn)) + minn)


#                     0.9                  7           1
for i in range(10):
    print(my_random(1, 9))


# другой вариант:
def random(a, b):
    the_set = set()
    list = []
    for i in range(a, b):
        the_set.add(str(i))
    for e in the_set:
        list.append(e)
        break
    print(list)


random(5, 10)

# другой вариант:
import time


def random():
    interval = int(input('Введите желаемый интервал рандома: '))
    ms = time.time() * 1000.0
    b = int(ms)
    d = ms - b
    answer = d * interval
    print(int(round(answer, 0)))
    return answer


random()


# 2. Задайте список. Напишите программу, которая определит, присутствует ли в заданном списке строк некое число.
# ['efg23', '79234gefg', 'sdgs', 'g53']
# '2'
# ['efg23', '79234gefg']

def search(lst, search_num):
    for i in range(len(lst)):
        if search_num in lst[i]:
            new_list.append(lst[i])
    return new_list


my_list = ['efg23', '79234gefg', 'sdgs', 'g53']
new_list = []
search_num = '2'
print(search(new_list, search_num))


# другой вариант:
def find(list, finddigit):
    for i in range(len(list)):
        if finddigit in list[i]:
            print(list[i])


my_list = ['efg23', '79234gefg', 'sdgs', 'g53']
finddigit = '2'

find(my_list, finddigit)


# другой вариант:


# 3. Напишите программу, которая определит позицию второго вхождения строки в списке либо сообщит, что её нет.
# *Пример:*
# - список: ["qwe", "asd", "zxc", "qwe", "ertqwe"], ищем: "qwe", ответ: 3
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"], ищем: "йцу", ответ: 5
# - список: ["йцу", "фыв", "ячс", "цук", "йцукен"], ищем: "йцу", ответ: -1
# - список: ["123", "234", 123, "567"], ищем: "123", ответ: -1
# - список: [], ищем: "123", ответ: -1

def search_position(lst, search_str):
    count = 0
    for i in range(len(lst)):
        if lst[i] == search_str:
            count += 1
            if count == 2:
                return i
    return -1


my_list = ["йцу", "фыв", "ячс", "цук", "йцукен", "йцу"]
search_str = "йцу"
print(search_position(my_list, search_str))

# другой вариант:
def findstr(my_list: list, find_string: str) -> int:  #!!! в этом коде применен тайпинг
    count = 0
    for i in range(len(my_list)):
        if find_string == my_list[i]:
            count += 1
            if count == 2:
                return i
    return -1

list_find = ["йцу", "фыв","йцу", "ячс", "цук", "йцукен"]
find_string = "йцу"

print(findstr(list_find, find_string))
