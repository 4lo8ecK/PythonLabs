# Лабораторная работа №8
# Вариант 6
# Гаврилов Павел ФМ 11-25

# для генерации случайных списков
import random

# Генерация случайного списка с размером n и со значениями от 0 до n
def rand_list(elem_count: int, seed: int) -> list:
    random.seed(seed)
    return [random.randint(0, elem_count) for _ in range(elem_count)]
# !rand_list(int, int) -> list
def linear_list(elem_count: int) -> list:
    return [x for x in range(0, elem_count)]
# !linear_list(int) -> list

# Задание 1
def task_1() -> None:
    print("Задание 1")
    print("Программа выдаёт максимально приближенный к введённому числу элемент массива")
    
    r = input("Искомое число: ")
    if r == '' or r == 'exit': return
    
    n = input("Размер массива: ")
    if n == '' or n == 'exit': return
    
    try:
        r = int(r)
        n = int(n)
    except ValueError:
        print("Нужно ввести числа!")
        input("Нажмите [Enter]")
        return
    
    lst = rand_list(n, 0)
    print("Массив чисел:\n->",lst)

    min_delta = n
    number = 0

    for i in range(0, n):
        local_delta = abs(lst[i] - r)
        if local_delta < min_delta:
            min_delta = local_delta
            number = lst[i]
    
    print(f"Максимально приближенное к {n} число - {number}")
# !task_1() -> None

# Задание 2
def task_2() -> None:
    print("Задание 2")
    print("Программа выдаёт изначальный массив случайных чисел")
    print("А после - удаляет из него элементы с нечётным индексом и выводит полученный список")
    print("Размер - не менее 2-ух элементов")
    lst_len = input("Введите размер массива: ")
    if lst_len == '' or lst_len == 'exit': return

    try:
        lst_len = int(lst_len)
    except ValueError:
        print("Нужно ввести числа!")
        input("Нажмите [Enter]")
        return

    if lst_len < 2: return

    lst1 = rand_list(lst_len, 1)
    print(f"Полученный случайным образом массив:\n-> {lst1}")
    
    lst = []
    for i in range(0, lst_len, 2):
        lst += [lst1[i]]
    del lst1
    
    print(f"Итоговый массив:\n-> {lst}")
# !task_2() -> None

# Задание 3
points_count = int(input())
lst = []
for i in range(0, points_count):
    lst += [rand_list(2, i)]
print(lst)


