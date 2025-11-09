# Лабораторная работа №10
# Вариант 6
# Гаврилов Павел ФМ-11-25

import random as rnd    # для 'seed()' и 'randint()'
import time             # для 'time()' - для получения случайного seed'а

EXIT_CODES = ['exit', 'q', 'close']

def clear_console() -> None:
    print('\033c', end='')
# !clear_console() -> None

def rand_list(
        elem_count: int = 10,
        _seed:      int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin
    rnd.seed(_seed)
    return [rnd.randint(min_value, max_value) for _ in range(elem_count)]
# !rand_list(int, int, int, int) -> list

def rand_matrix(
        row:        int = 2,
        colomn:     int = 2,
        _seed:      int = 0,
        min_value:  int = -10,
        max_value:  int = 10
        ) -> list:
# begin 
    rnd.seed(_seed)
    res = []
    for i in range(row):
        res += [[rnd.randint(min_value, max_value) for _ in range(colomn)]]
    return res
# !rand_matrix(int, int, int, int, int) -> list

def rand_serial_list(
        elem_count:     int = 10,
        seed:           int = 0,
        min_value:      int = -10,
        max_value:      int = 10,
        max_series_len: int = 3
        ) -> list:
    rnd.seed(seed)
    tmp_series_values = rand_list(elem_count, seed, min_value, max_value)
    result = []
    for i in range(elem_count):
        for j in range(rnd.randint(1, max_series_len)):
            result += [tmp_series_values[i]]

    # удаление ссылок на уже ненужные объекты
    del result[elem_count:], tmp_series_values
    return result
# !rand_serial_list(int, int, int, int, int) -> list

def rand_serial_matrix(
        row:            int = 4,
        colomn:         int = 10,
        _seed:          int = 0,
        max_series_len: int = 5,
        min_value:      int = -10,
        max_value:      int = 10
        ) -> list:
    res = []
    for i in range(row):
        res += [rand_serial_list(colomn, _seed + i, min_value, max_value, max_series_len)]
    return res
# !rand_serial_matrix(int, int, int, int, int, int) -> list

def get_seed() -> int:
    clear_console()
    
    print("Введите сид для генерации случайных списков / многомерных списков")
    print("Нужно ввести просто любое целочисленное значение")
    print("Либо нажмите [Enter], и будет применено значение по умолчанию - 0")
    
    cmd = input("> ")
    
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
    seed = int(time.time() * 10000) % 100000
    mtx = rand_matrix(2, 10, seed)
    print("\tЗадание 1\n")
    print(f"Сид для генерации: {seed} - за основу взято время в unix-time")
    print(f"Случайная матрица в 2 строки и 10 столбцов\n\tx: {mtx[0]}\n\ty: {mtx[1]}\n")
    print("Номера столбцов, в которых представлены координаты точек I четверти:")
    print("\t(отсчёт начинается с 1)")

    count = 0

    for i in range(10):
        if mtx[0][i] > 0 and mtx[1][i] > 0:
            count += 1
            print(i + 1, end=' ')

    if count == 0: print("Нет таких точек")
    else: print(f"\nКоличество таких точек - {count}")
# !task_1() -> None

def task_2() -> None:
    seed = int(time.time() * 10000) % 100000
    arr = rand_serial_matrix(2, 10, seed, 5, 1, 10)
    
    print("\tЗадание 2\n")

    print(f"Сид для генерации: {seed} - за основу взято время в unix-time")
    print(f"Случайная матрица в 2 строки и 10 столбцов\n\tx: {arr[0]}\n\ty: {arr[1]}\n")

    t = arr[0][0] / arr[1][0]

    for i in range(1, 10):

        a = arr[0][i]
        b = arr[1][i]
        rel = a / b

        print(f"======= Колонна {i} =======\
              \n\tпервый элемент:\t{a}\n\tвторой элемент:\t{b}\n\tотношение:\t{rel}")
        if rel != t:
            print("\t=== не OK ===\n")
            break
        print("\t=== OK ===\n")
    # endloop
# !task_2() -> None

def main():
    print("\tЛабораторная работа №10\n")
    print("Количество заданий - 3")
    print("Выберите задание:")
    cmd = input('→ ')
    if cmd in EXIT_CODES or cmd == '': exit(0)
    
    try:
        cmd = int(cmd)
    except ValueError:
        return

    while True:
        clear_console()
        if 1 <= cmd <= 3:
            match cmd:
                case 1: task_1()
                case 2: task_2()
        else:
            continue
        l_cmd = input('→ ')
        if l_cmd in EXIT_CODES: break

    # end

while True:
    clear_console()
    main()
    