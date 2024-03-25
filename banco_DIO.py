from getpass import getpass
import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def login_UI():
    clear()
    print("==================================")
    print("       Banco Python Central")
    print()
    login = print("Login: ", end=''), input()
    password = getpass() 
    print()
    print("==================================")

def UI(user):
    clear()
    print("==================================")
    print(f"      Seja bem vindo {user}!")
    print()
    print("[1] Depósito")
    print("[2] Saque")
    print("[3] Extrato")
    print()
    print("[4] Sair")
    print()
    print("==================================")
    option = int(input(": ").strip())
    return option

def deposit():
    global account_balance
    global account_extract
    global account_id
    clear()
    print("==================================")
    print()
    deposit_value = print("Valor do depósito: ", end=''), int(input())
    deposit_destination = print("ID da conta destinada: ", end=''), int(input())
    print()
    print("==================================")
    if account_id != deposit_destination[1]:
        if account_balance < deposit_value[1]:
            clear()
            print("Não foi possível realizar a transação! Saldo insuficiente!")
            print("Aperte ENTER para continuar:", end=''), input()
            return False
        else:
            account_balance -= deposit_value[1]
            clear()
            print("Transação realizada com sucesso!")
            print("Aperte ENTER para continuar:", end=''), input()
            account_extract.append(f'DEPÓSITO: R${deposit_value[1]:.2f} ID{deposit_destination[1]}')
            return True
    else:
        account_balance += deposit_value[1]
        clear()
        print("Transação realizada com sucesso!")
        print("Aperte ENTER para continuar:", end=''), input()
        account_extract.append(f'DEPÓSITO: R${deposit_value[1]:.2f} ID{deposit_destination[1]}')
        return True

def withdraw():
    global account_balance
    global account_extract
    global account_id
    global withdraw_limit
    clear()
    print("==================================")
    print()
    withdraw_value = print("Valor do saque: ", end=''), int(input())
    print()
    print("==================================")
    if withdraw_value[1] > account_balance or withdraw_value[1] > 500 or withdraw_limit == 0:
        clear()
        print("Não foi possível realizar a transação! Limite de saque excedido!")
        print("Aperte ENTER para continuar:", end=''), input()
        return False
    else:
        account_balance -= withdraw_value[1]
        clear()
        print("Transação realizada com sucesso!")
        print("Aperte ENTER para continuar:", end=''), input()
        account_extract.append(f'SAQUE: R${withdraw_value[1]:.2f}')
        withdraw_limit -= 1
        return True

def extract():
    global account_balance
    global account_extract
    global account_id
    clear()
    print("==================================")
    print()
    for e in account_extract:
        print(f'{e}\n')
    print()
    print("==================================")
    print("Aperte ENTER para continuar:", end=''), input()



login_UI()
account_id = 1921821
account_balance = 2500
account_extract = []
withdraw_limit = 3

while True:
    valid_options = 1, 2, 3, 4
    try:
        option = UI('Renato')
    except ValueError:
        continue
    if option not in valid_options:
        continue
    elif option == 1:
        deposit()
    elif option == 2:
        withdraw()
    elif option == 3:
        extract()
    else:
        break
    