from colorama import *
import random
import pyfiglet
from time import sleep as s
from os import system as sy

lg = Fore.LIGHTGREEN_EX
w = Fore.WHITE
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
g = Fore.GREEN
p = Fore.MAGENTA
b = Fore.BLUE
colors = [lg, r, cy,b,p]

def pisca():
    sy('cls')
    for i in range(15):
        f = pyfiglet.Figlet(font='slant')
        banner = f.renderText('CONSULTAS')
        print(f'{random.choice(colors)}{banner}{n}')
        print(f'              Feito por: {random.choice(colors)}</whs?>{w}\n')
        s(0.1)
        sy('cls')
        i+1
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('CONSULTAS')
    print(f'{random.choice(colors)}{banner}{n}')
    print(f'              Feito por: {random.choice(colors)}</whs?>{w}\n')
    print(f'''{ye}
╰──>  APERTE ENTER PARA INICIAR{w}''')




def banner1():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('CONSULTAS')
    print(f'{r}{banner}{n}')
    print(f'              Feito por: {random.choice(colors)}</whs?>{w}\n')
    print(f'''{ye}
''')




def banner_ip():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('IP')
    print(f'{g}{banner}{n}')

def banner_cep():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('CEP')
    print(f'{random.choice(colors)}{banner}{n}')

def banner_cnpj():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('CNPJ')
    print(f'{random.choice(colors)}{banner}{n}')

def banner_placa():
    f = pyfiglet.Figlet(font='slant')
    banner = f.renderText('PLACA')
    print(f'{random.choice(colors)}{banner}{n}')