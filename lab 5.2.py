# Лабораторная работа №5
# Вариант 6
# Гаврилов Павел ФМ 11-25

# Задание 2
# Разработать программу для решения задачи определения места нахождения
# точки с произвольно заданными координатами на координатной плоскости. В случае
# если точка попадает в одну их выделенных областей (внутрь или на границу), про-
# грамма должна определять номер области или писать, что не попадает в нее. Границу
# области считать принадлежащей самой области и отдельно ее рассматривать не надо.
# При решении должны быть использованы условный оператор if.

import os

# (x - a)**2 - (y - b)**2 = R**2

# 0 - на границе
# 1 - внутри
# 2 - снаружи
def circle(x: float, y: float, a: float, b: float) -> int:
    inside = (x - a)**2 + (y - b)**2 < 1
    outside = (x - a)**2 + (y - b)**2 > 1
    bound = (x - a)**2 + (y - b)**2 == 1
    if bound: return 0
    elif inside: return 1
    elif outside: return 2
    else: return 3
# !circle(float, float, float, float) -> int

while True:
    os.system('cls')
    in_x = input()
    if in_x == 'exit':
        exit(0)
    in_y = input()

    in_x = float(in_x)
    in_y = float(in_y)

    first = circle(in_x, in_y, 0, 1)    
    second = circle(in_x, in_y, 1, 0)    
    third = circle(in_x, in_y, 0, -1)    
    forth = circle(in_x, in_y, -1, 0)    
    fifth = circle(in_x, in_y, 0, 0)    

    M1: float = ((-2 <= in_x < 0) and (0 < in_y <= 2)) and not(first == 1 and forth == 1)
    M2: float = ((1 <= in_x <= 2) and (0 <= in_y <= 2)) and not(first == 1 and second == 1)
    M3: float = ((0 <= in_y <= 1) and (0 <= in_x <= 1)) and (first == 1 and second == 1 and fifth == 1)
    M4: float = ((-1 <= in_y <= 1) and (-1 <= in_x <= 0)) and (fifth == 1 and not(third == 1 and forth == 1))
    M5: float = ((-2 <= in_y < 0) and (0 <= in_x <= 1)) and not(fifth == 1 and second == 1)

    print("M1:",M1)
    print("M2:",M2)
    print("M3:",M3)
    print("M4:",M4)
    print("M5:",M5)

    if (input() == 'exit'): exit(0) 
