# Лабораторная работа №10
# Вариант 6
# Гаврилов Павел ФМ-11-25

import random 

def clear_console() -> None:
    print('\033c', end='')
# !clear_console() -> None

def rand_list(
        elem_count: int,
        _seed:      int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin
    random.seed(_seed)
    return [random.randint(min_value, max_value) for _ in range(elem_count)]
# !rand_list(int, int, int, int) -> list

def rand_matrix(
        row:        int = 2,
        colomn:     int = 2,
        _seed:      int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin 
    random.seed(_seed)
    res = []
    for i in range(row):
        res += [[random.randint(min_value, max_value) for _ in range(colomn)]]
    return res
# !rand_matrix(int, int, int, int, int) -> list

def get_seed() -> int:
    clear_console()
    
    print("Введите сид для генерации случайных списков / многомерных списков")
    print("Нужно ввести просто любое целочисленное значение")
    print("Либо нажмите [Enter], и будет применено значение по умолчанию - 0")
    
    cmd = input(": ")
    
    if cmd == '':
        clear_console()
        return 0
    if cmd == "exit": exit(0)

    try:
        cmd = int(cmd)
    except ValueError:
        print("Нужно ввести целочисленное значение")
        print("Будет применено значение по умолчанию (0)")
        input("Нажмите [Enter]")
        cmd = 0
    
    clear_console()
    return cmd
# !get_seed() -> int

def task_1() -> None:
    seed = get_seed()
    mtx = rand_matrix(2, 10, seed)
    print("Задание 1")
    print(f"Случайная матрица в 2 строки и 10 столбцов\n->\tx: {mtx[0]}\n\ty: {mtx[1]}")
    print("Номера столбцов, в которых представлены координаты точек I четверти:")
    print("\t(отсчёт начинается с 1)")

    count = 0

    for i in range(10):
        if mtx[0][i] > 0 and mtx[1][i] > 0:
            count += 1
            print(i + 1, end=' ')

    print(f"\nКоличество таких точек - {count}")
# !task_1() -> None

def task_2() -> None:
    pass
