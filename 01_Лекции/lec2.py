# МНОЖЕСТВА


exit()
# СЛОВАРИ
dictionary = {}
dictionary = \
{
'up': '↑',
'left': '←',
'down': '↓',
'right': '→'
}
print(dictionary) # {'up':'↑', 'left':'←', 'down':'↓', 'right':'→'}
print(dictionary['left']) # ←
# типы ключей могут отличаться
print(dictionary['up']) # ↑
# типы ключей могут отличаться
dictionary['left'] = '⇐'
print(dictionary['left']) # ⇐
#print(dictionary['type']) # KeyError: 'type'
del dictionary['left'] # удаление элемента
for item in dictionary: # for (k,v) in dictionary.items():
    print('{}: {}'.format(item, dictionary[item]))
# up: ↑
# down: ↓
# right: →

# КОРТЕЖИ
t = tuple(['red', 'green', 'blue'])
red, green, blue = t
print('r:{} g:{} b:{}'.format(red, green, blue))
# r:red g:green b:blue

t = ()
print(type(t)) # tuple
t = (1,)
print(type(t)) # tuple
t = (1)
print(type(t)) # int
t = (28, 9, 1990)
print(type(t)) # tuple
colors = ['red', 'green', 'blue']
print(colors) # ['red', 'green', 'blue']
t = tuple(colors)
print(t) # ('red', 'green', 'blue')

a = (3, 5)
print(a)
print(a[-1])

# РЕКУРСИЯ

def fib(n):
    if n in [1, 2]:
        return 1
    else:
        return fib(n - 1) + fib(n - 2)

list = []
for e in range(1, 10):
    list.append(fib(e))
print(list)  # 1 1 2 3 5 8 13 21 34


def concatenatio(*params):
    # res: int = 0
    res: str = ""
    for item in params:
        res += item
    return res


print(concatenatio('a', 's', 'd', 'w'))  # asdw
print(concatenatio('a', '1', 'd', '2'))  # a1d2


# print(concatenatio(1, 2, 3, 4))  # TypeError: ...


def new_string(symbol, count=5):
    return symbol * count


print(new_string('!', 5))  # !!!!!
print(new_string('!'))  # !!!
print(new_string(4))  # 12

import lec as l

print(l.f(1))

path = 'file1.txt'
data = open(path, 'r')
for line in data:
    print(line)
data.close()

colors = ['red', 'green', 'blue']
data = open('file.txt', 'w')
# data.writelines(colors)  # разделителей не будет
data.write('\nLINE 12\n')
data.write('LINE 13\n')
data.close()

with open('file1.txt', 'a') as data:
    data.write('line 1\n')
    data.write('line 2\n')  # происходит автомат.разрыв, т.е. не требуется принудительный разрыв типа data.close()
