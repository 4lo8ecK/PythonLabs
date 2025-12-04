# Лабораторная работа №15
# Вариант 6
# Гаврилов Павел ФМ-11-25

import os

COMMANDS_STR = ['DEPOSIT', 'WITHDRAW', 'BALANCE', 'TRANSFER', 'INCOME']
ERR_MSG = 'ERROR'


DIR_NAME = 'lab15-files'
DATA_BASE_FILE = 'comands'

g_clients = {}

#region MAIN METHODS
def deposit(client: str, balance: int = 0) -> bool:
    try:
        balance = int(balance)
        g_clients.update({client: balance})
        return True
    except:
        return False
# !add_client(str, int) -> bool

def withdraw(client: str, summ: int = 0) -> bool:
    try:
        summ = int(summ)
        balance = g_clients.get(client)
        balance -= summ
        g_clients.update({client: balance})
        return True
    except:
        return False
# !withdraw(str, int) -> bool

def balance(client: str) -> int:
    try:
        return g_clients.get(client)
    except:
        return None
# !balance(str) -> int

def transfer(name1: str, name2: str, summ: int) -> bool:
    try:
        summ = int(summ)
        clients_list = list(g_clients.keys())
        if name1 not in clients_list:
            deposit(name1)
        if name2 not in clients_list:
            deposit(name2)
    
        n1_balance = balance(name1) - summ
        n2_balance = balance(name2) + summ
    
        deposit(name1, n1_balance)
        deposit(name2, n2_balance)

        return True
    except:
        return False
# !transfer(str, str, int) -> bool

def income(proc: int) -> bool:
    try:
        proc = int(proc)
        clients = list(g_clients.keys())
        for c in clients:
            bal = balance(c)
            bal = int(bal * (1 + proc/100))
            g_clients.update({c: bal})
        return True
    except:
        return False
# !income(int) -> bool
#endregion
#region INIT
def read_file() -> list:
    cmdlines = []
    with open(file=os.path.join(DIR_NAME, DATA_BASE_FILE), mode='r', encoding='utf-8') as file:
        cmdlines = file.readlines()
    return cmdlines

def init_prog(commands: list = []) -> None:
    if not os.path.exists(DIR_NAME):
        os.mkdir(DIR_NAME)
    for i in range(len(commands)):
        commands[i] += '\n'
    with open(file=os.path.join(DIR_NAME, DATA_BASE_FILE), mode='w', encoding='utf-8') as file:
        file.writelines(commands)
#endregion
#region PARCER
def exec_comands() -> None:
    for _cmd in read_file():
        if _cmd == '': continue
        _cmd = _cmd.split()
        if _cmd[0] in COMMANDS_STR:
            # deposit
            if _cmd[0] == COMMANDS_STR[0]:
                deposit(_cmd[1], int(_cmd[2]))
            # withdraw
            elif _cmd[0] ==  COMMANDS_STR[1]:
                withdraw(_cmd[1], int(_cmd[2]))
            # balance
            elif _cmd[0] == COMMANDS_STR[2]:
                bal = balance(_cmd[1])
                if bal == None:
                    print(ERR_MSG)
                else:
                    print(bal)
            # transfer
            elif _cmd[0] == COMMANDS_STR[3]:
                transfer(_cmd[1], _cmd[2], int(_cmd[3]))
            # income
            elif _cmd[0] == COMMANDS_STR[4]:
                income(int(_cmd[1]))
            else:
                continue
# deposit('Ivanov', 100)
# income(5)
# print(balance('Ivanov'))
# transfer('Ivanov', 'Petrov', 50)
# withdraw('Petrov', 100)
# print(balance('Petrov'))
# print(balance('Sidorov'))
#endregion

commands = [
    'DEPOSIT Ivanov 100',
    'INCOME 5',
    'BALANCE Ivanov',
    'TRANSFER Ivanov Petrov 50',
    'WITHDRAW Petrov 100',
    'BALANCE Petrov',
    'BALANCE Sidorov'
]
init_prog(commands)
exec_comands()