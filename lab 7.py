# Лабораторная работа №6
# Вариант 6
# Гаврилов Павел ФМ 11-25

import os

def clear_console():
    # если запускается на unix системах: macOS, linux
    if os.name == 'posix':
        os.system('clear')
    # если запускается на windows
    elif os.name == 'nt':
        os.system('cls')

# Задание 1
def task_1():
    clear_console()
    print("Задание 1")
    print("Возвращает буквосочетание из 2 и 4 символа введёного текста")
    input_string = input("Введите слово длиной более 4 символов: ")
    if len(input_string) < 4:
        print("Слово должно быть более 4 символов!")
        return False
    print(input_string[1] + input_string[3])
    return True
# Задание 2
def task_2():
    clear_console()
    print("Задание 2")
    print("Выдаёт количество букв 'н' и 'м'")
    input_string = input("Введите любой текст: ")

    n_count = 0
    m_count = 0
    n_big_count = 0
    m_big_count = 0

    for i in range(0, len(input_string)):
        if input_string[i] == 'н':
            n_count += 1
        elif input_string[i] == 'м':
            m_count += 1
        elif input_string[i] == 'Н':
            n_big_count += 1
        elif input_string[i] == 'М':
            m_big_count += 1

    print("Результат:")
    if n_count > 0 or n_big_count > 0:
        print(f"кол-во букв 'н' всего - {n_count + n_big_count}:\n\t{n_count} строчных\n\t{n_big_count} прописных")

    if m_count > 0 or m_big_count > 0:
        print(f"кол-во букв 'н' всего - {m_count + m_big_count}:\n\t{m_count} строчных\n\t{m_big_count} прописных")
    else:
        print("Нет букв 'н' и 'м'")
    input()

# Задание 3
def task_3():
    print("Задание 3")
    print("Возвращает количество прописных латинских символов")

    input_string = input("Ввод: ")
    big_sym_count = 0
    for i in range(0, len(input_string)):
        if input_string[i] in range(65, 91):
            big_sym_count += 1

    print(f"Ответ - {big_sym_count}")
    input()

# Задание 4
def task_4():
    clear_console()
    input_string = input("Введите строку: ")
    number = int(input("Введите число: "))

    if len(input_string) > number:
        print(input_string[(len(input_string) - number)::])
    elif len(input_string) < number:
        print( str('.' * (number - len(input_string))) + str(input_string))
    input()

# Задание 5
clear_console()
