#https://ipwhois.app/json/
import requests
from colorama import *
import random
from banner import banner_ip
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
colors = [lg, r, cy, ye,b,p]

def consult_IP():
    banner_ip()
    inp_IP = input(f'''{ye}[-] PARA VOLTAR AO MENU.
  ╰──>  DIGITE O IP QUE DESEJA BUSCAR: {r}''')
    if len(inp_IP) == 14:
        request = requests.get(f'http://ip-api.com/json/{inp_IP}')
        IPaddres = request.json()
        if 'fail' in IPaddres:
            sy('cls')
            print(f'''{r}
│ ERRO!
╰──>    NÃO FOI POSSIVEL ENCONTRAR O IP: {ye}{inp_IP}{n}''')
            s(1.5)
            sy('cls')
            consult_IP()
        else:
            sy('cls')
            print(f'''{g}
│{w} IP: {g}{inp_IP}
│{w} PAÍS: {g}{(IPaddres['country'])}/{g}{(IPaddres['countryCode'])}
│{w} REGIÃO: {g}{(IPaddres['region'])}/{(IPaddres['regionName'])}
│{w} HORARIO GMT: {g}{(IPaddres['timezone'])}
│{w} CIDADE: {g}{(IPaddres['city'])}
│{w} LATITUDE: {g}{(IPaddres['lat'])}
│{w} LONGITUDE: {g}{(IPaddres['lon'])}
│{w} EMPRESA: {g}{(IPaddres['org'])}
│{w} LINK MAPS: {g}https://www.google.com.br/maps/place/{(IPaddres['lat'])}%20{(IPaddres['lon'])}''')
        input(f'''{g}│
╰──>   APERTE ENTER PARA CONTINUAR.{w}''')
    elif inp_IP == '-':
        pass
    else:
        print(f'''{ye}
│ ERRO!
╰──>    QUANTIDADE DE CARACTERES INVALIDA: {r}{len(inp_IP)}{w}''')
        s(1.5)
        sy('cls')
        consult_IP()
        #{(cnaddress_data['nome'])}
