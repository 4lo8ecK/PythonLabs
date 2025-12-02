# Дополнительное задание №1
# Вариант 6 
# Гаврилов Павел ФМ-11-25

import math

#region TASK 1 
def func_t1(x: float = 0, a: float = 0) -> float:
    if x < 0:
        res = (a ** 2/3) - (x ** 2/3)
        if res < 0:
            return None
        return math.sqrt(res)
    
    else:
        if (a * 2 - x) == 0:
            return None
        res = (x ** 3) / (a * 2 - x)
        if res < 0:
            return None
        return a + math.sqrt(res)
# !func_t1(float, float) -> float

def task_1() -> None:

    print("\x1bc", end='')
    print("\x1b[2mДополнительное задание №2")
    print("Задание 1\x1b[0m")

    a = 0.8
    x = -a
    dx = round(a / 4, 1)

    print(f"a = {a}\ndx = {dx}")
    n = input("Введите x: ")
    if n == '': n = 12
    else: n = int(n)

    for i in range(n):
        res = func_t1(x=x, a=a)

        if res != None:
            res = round(res, 4)

        print(f"{i+1}\t\x1b[4Dres = {res}\tx = {x}")
        x = round(x + dx, 1)
    return
# !task_1() -> None
#endregion

#region TASK 2
def func_t2(k: float = 0) -> float:
    return k**3 + 25*(k**2) + 50*k + 1000

def task_2() -> None:
    print("\x1bc", end='')
    print("\x1b[2mДополнительное задание №2")
    print("Задание 2\x1b[0m")

    # константы
    A = 3 * (10 ** 4)
    B = 6 * (10 ** 4)
    M = 4
    T1 = math.sqrt(A * B * M)
    T2 = A + B + M

    rng_beg = -30
    rng_end = 60
    rng_count = 20
    rng_step: int = int((rng_end - rng_beg) // rng_count)

    print("\nЗначения функции \x1b[1m\x1b[3mf(K)\x1b[0m при \x1b[1m\x1b[3mK\x1b[0m")

    print('\x1b[2m', end='')
    print('-'*19)
    print('\x1b[0m', end='')

    print("   \x1b[3mK\t\x1b[2m|\x1b[0m результат")

    print('\x1b[2m', end='')
    print('-'*19)
    print('\x1b[0m', end='')

    count = 0
    for i in range(rng_beg, rng_end, rng_step):
        value = func_t2(i)
        if (value > 0) and (value < T1) and (value < T2):
            print(f"  {i}\t\x1b[2m|\x1b[0m  {value}\t")
        else:
            count += 1

    print('\x1b[2m', end='')
    print('-'*19)
    print('\x1b[0m', end='')

    print(f'количество исключений - {count}\n')
#endregion

#region TASK 3

x0 = 0
n = 10

z0 = 0
m = 10



#endregion