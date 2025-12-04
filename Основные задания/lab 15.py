# Лабораторная работа №15
# Вариант 6
# Гаврилов Павел ФМ-11-25

COMMANDS_STR = ['DEPOSIT', 'WITHDRAW', 'BALANCE', 'TRANSFER', 'INCOME']
ERR_MSG = 'ERROR'

DIR_NAME = 'lab15-files'
DATA_BASE_FILE = 'comands'


g_clients = {}

def deposit(client: str, balance: int = 0) -> bool:
    try:
        g_clients.update({client: balance})
        return True
    except:
        return False
# !add_client(str, int) -> bool

def withdraw(client: str, summ: int = 0) -> bool:
    try:
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
        clients = list(g_clients.keys())
        for c in clients:
            bal = balance(c)
            bal = bal * (1 + proc/100)
            g_clients.update({c: bal})
        return True
    except:
        return False
# !income(int) -> bool

def get_commands_list() -> list:
    cmdlines = []
    with open(file=os.path.join(DIR_NAME, DATA_BASE_FILE), mode='r', encoding='utf-8') as file:
        cmdlines = file.readlines()

    
    
    
    
    
    pass

deposit('Ivanov', 100)
income(5)
print(balance('Ivanov'))
transfer('Ivanov', 'Petrov', 50)
withdraw('Petrov', 100)
print(balance('Petrov'))
print(balance('Sidorov'))


