import requests
from banner import banner_IpSite
from colorama import *
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


def consultSite():
    banner_IpSite()
    site = input(f'''{ye}[*] PARA VOLTAR AO MENU.
  ╰──>  DIGITE O SITE QUE DESEJA BUSCAR: {r}''')
    site.replace('https://www.','')
    request = requests.get(f'http://ip-api.com/json/{site}')
    siteAdress = request.json()
    if 'fail' in siteAdress:
        sy('cls')
        print(f'''{r}
│ ERRO!
╰──>    NÃO FOI POSSIVEL ENCONTRAR O SITE: {ye}{site}{n}''')
        s(1.5)
        sy('cls')
        consultSite()
    else:
        sy('cls')
        print(f'''{g}
│{w} IP: {g}{site}
│{w} PAÍS: {g}{(siteAdress['country'])}/{g}{(siteAdress['countryCode'])}
│{w} REGIÃO: {g}{(siteAdress['region'])}/{(siteAdress['regionName'])}
│{w} HORARIO GMT: {g}{(siteAdress['timezone'])}
│{w} CIDADE: {g}{(siteAdress['city'])}
│{w} LATITUDE: {g}{(siteAdress['lat'])}
│{w} LONGITUDE: {g}{(siteAdress['lon'])}
│{w} EMPRESA: {g}{(siteAdress['org'])}
│{w} LINK MAPS: {g}https://www.google.com.br/maps/place/{(siteAdress['lat'])}%20{(siteAdress['lon'])}''')
        input(f'''{g}│
╰──>   APERTE ENTER PARA CONTINUAR.{w}''')
    if site == '*':
        pass
        #{(cnaddress_data['nome'])}