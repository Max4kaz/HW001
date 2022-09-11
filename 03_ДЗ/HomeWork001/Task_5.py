# 5. Напишите программу, которая принимает на вход координаты двух точек и находит расстояние между ними в 2D пространстве.
# *Пример:*
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

def input_coordinates(x):
    coordinate = ['X', 'Y']
    a = []
    for i in range(x):
        a.append(int(input(f"- по {coordinate[i]}: ")))
    return a

def calc_distance(a, b):
    distance = ((b[0] - a[0]) ** 2 + (b[1] - a[1]) ** 2) ** 0.5
    return distance

print("Введите координаты точки А")
point_a = input_coordinates(2)
print("Введите координаты точки В")
point_b = input_coordinates(2)
print(f"Расстояние между точками: {format(calc_distance(point_a, point_b), '.2f')}")