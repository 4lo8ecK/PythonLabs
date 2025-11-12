# Лабораторная работа №11
# Гаврилов Павел ФМ-11-25
# Вариант 6

EXIT_KEYS = ['exit', 'q', 'й', 'учше', 'quit', 'йгшк']

def print_dict(inp: dict) -> None:
    keys = list(inp.keys())
    items = list(inp.values())

    for i in range(len(keys)):
        print(f"{keys[i]}: {items[i]}")
# !print_dict(dict) -> None

# Задание 1
_dict = {
    'судно 1': 'рыба',
    'судно 2': 'не рыба, а мясо',
    'судно 3': 'техника',
    'судно 4': 'футбольные мячи',
    'судно 5': 'бутсы',
    'судно 6': 'обычная обувь',
    'судно 7': 'всё подряд'}

'''def task_1() -> None:
    print(_dict)
'''
def task_1() -> None:
    print("\tЗадание 1\n")
    print("Вывод словаря из 7 элементов")
    print("Все осальные задания так же работают с этим словарём")
    
    print("Ключ: значение")
    print_dict(_dict)

# !task_1() -> None

# Задание 2
def task_2() -> None:
    print("\tЗадание 2\n")
    print("Эта программа выводит список ключей")
    print("После чего выдаёт по запросу пользователя значение этого словаря по ключу")
    print("Необходимо ввести перечисленные ключи")
    print("Ключи: ")
    keys = list(_dict.keys())
    for i in keys:
        print(i)
    cmd = input("Ключ: ")
    print(_dict.get(cmd, "Нет такого варианта"))
# !task_2() -> None

def task_3() -> None:
    print('\tЗадание 3\n')
    print("Эта программа меняет местами ключи и значения словаря")
    
    keys = list(_dict.keys())
    items = list(_dict.values())

    res = {}
    for i in range(len(keys)):
        res[items[i]] = keys[i]
    
    print_dict(res)
# !task_3() -> None

def main():
    print("\033c", end='')
    print("\n\tЛабораторная работа №11\n")
    print("Выберите задание")

    cmd = input("-> ")
    if cmd in EXIT_KEYS:
        print("\033c", end='')
        exit(0)
    try:
        cmd = int(cmd)
    except ValueError:
        return

    print("\033c", end='')
    match cmd:
        case 1: task_1()
        case 2: task_2()
        case 3: task_3()

    cmd = input("-> ")
    if cmd in EXIT_KEYS: exit(0)

    pass

# main loop
while True:
    print('\033c', end='')
    main()
