from colorama import *
import requests
import random
from banner import banner_cep
from time import sleep as s
from os import system as sy
lg = Fore.LIGHTGREEN_EX
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
g = Fore.GREEN
p = Fore.MAGENTA
b = Fore.BLUE
w = Fore.WHITE
colors = [lg, r, cy, ye,b,p]



def cep1():
    banner_cep()
    cep = input(f'''{ye}[*] PARA VOLTAR AO MENU.
  ╰──>  DIGITE O IP QUE DESEJA BUSCAR: {r}''')
    cep = cep.replace("-", "")
    cep = cep.replace(".", "")
    if len(cep) == 8:
        request = requests.get(f'https://cep.awesomeapi.com.br/json/{cep}')
        address_data = request.json()
        print(f'''
{g}│ {w}TIPO: {g}{(address_data['address_type'])}          
{g}│ {w}CEP: {g}{(address_data['cep'])}          
{g}│ {w}RUA: {g}{(address_data['address_name'])}       
{g}│ {w}BAIRRO: {g}{(address_data['district'])}       
{g}│ {w}CIDADE/UF: {g}{(address_data['city'])}/{g}{(address_data['state'])}
{g}│ {w}DDD: {g}{(address_data['ddd'])}                
{g}│ {w}LAT: {g}{(address_data['lat'])}                
{g}│ {w}LNG: {g}{(address_data['lng'])}                
{g}│ {w}IBGE: {g}{(address_data['city_ibge'])}    ''')
        input(f'''{g}│
╰──>    APERTE ENTER PARA CONTINUAR.{w}''')
    elif cep == '*':
        pass
    
    elif len(cep) == 0:
        print(f'''{r}
│ ERRO!
╰──>    FAVOR INSERIR ALGUM VALOR.{w}''')
        s(1.5)
        sy('cls')
        cep1()
    else:
        print(f'''{ye}
│ ERRO!
╰──>    QUANTIDADE DE NUMEROS INVALIDA: {r}{len(cep)}{w}''')
        s(1.5)
        sy('cls')
        cep1()