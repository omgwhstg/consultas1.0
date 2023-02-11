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
    inp_IP = input(f'{ye}╰──>  DIGITE O IP QUE DESEJA BUSCAR: {r}')
    if len(inp_IP) == 14:
        request = requests.get(f'https://ipwhois.app/json/{inp_IP}')
        IPaddres = request.json()
        if 'message' in IPaddres:
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
│{w} IP: {g}{(IPaddres['ip'])}
│{w} TIPO: {g}{(IPaddres['type'])}
│{w} CONTINENTE:{g}{(IPaddres['continent'])}/{g}{(IPaddres['continent_code'])}
│{w} PAÍS: {g}{(IPaddres['country'])}/{g}{(IPaddres['country_code'])}
│{w} REGIÃO: {g}{(IPaddres['region'])}
│{w} CIDADE: {g}{(IPaddres['city'])}
│{w} LATITUDE: {g}{(IPaddres['latitude'])}
│{w} LONGITUDE: {g}{(IPaddres['longitude'])}
│{w} CODIGO DE ÁREA: {g}{(IPaddres['country_phone'])}
│{w} PAISES VIZINHOS: {g}{(IPaddres['country_neighbours'])}
│{w} ASN: {g}{(IPaddres['asn'])}
│{w} EMPRESA: {g}{(IPaddres['org'])}
│{w} HORARIO GMT: {g}{(IPaddres['timezone_gmt'])}
│{w} MOEDA: {g}{(IPaddres['currency'])}/{(IPaddres['currency_code'])}/{(IPaddres['currency_symbol'])}''')
        input(f'''{g}│
╰──>   APERTE ENTER PARA CONTINUAR.{w}''')
    else:
        print(f'''{ye}
│ ERRO!
╰──>    QUANTIDADE DE CARACTERES INVALIDA: {r}{len(inp_IP)}{w}''')
        s(1.5)
        sy('cls')
        consult_IP()
        #{(cnaddress_data['nome'])}