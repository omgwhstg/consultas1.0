from os import system as s
from time import sleep as t
s('cls')
s('python.exe -m pip install --upgrade pip')
s('pip install -r REQUIREMENTS.txt')
from colorama import *
g = Fore.GREEN
r = Fore.RESET
s('cls')
print(f'''
╰──>Todas bibliotecas foram instaladas.
Caso haja erro verifique {g}"REQUIREMENTS.txt"{r} e instale manualmente.''')
t(5)
s('cls')
s('cls')
print('╰──> Necessario executar apenas uma vez ')
t(2)