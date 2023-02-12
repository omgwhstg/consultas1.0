from os import system as s
from time import sleep as t
s('pip install requests')
s('python.exe -m pip install --upgrade pip')
s('cls')
print('''
│Requests
╰──>Instalado.''')
t(1)
s('cls')
s('cls')
print('╰──> Necessario executar apenas uma vez ')
t(1.3)
s('cls')
s('pip install colorama')
s('cls')
t(1)
print('''
│Coloramas
╰──>Instalado.''')
t(1)
s('pip install pyfiglet')
s('cls')
print('''
│Pyfiglet
╰──>Instalado.''')
t(1)
s('pip install crcmod')
s('cls')
print('''
│Crcmod
╰──>Instalado.''')
t(1)
s('pip install qrcode')
s('cls')
print('''
│Qrcode
╰──>Instalado.''')
t(1)
s('pip install pickle')
s('cls')
print('''
│Pickle
╰──>Instalado.''')
t(1)
s('cls')
from menu import menu_main
menu_main()