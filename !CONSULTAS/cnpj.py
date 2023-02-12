import requests
from colorama import *
from banner import banner_cnpj
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



def consult_cnpj():
    banner_cnpj()
    cnpj = input(f'''{ye}[*] PARA VOLTAR AO MENU.
  ╰──>  DIGITE O IP QUE DESEJA BUSCAR: {r}''')
    cnpj = cnpj.replace("-", "")
    cnpj = cnpj.replace(".", "")
    cnpj = cnpj.replace("/", "")
    if len(cnpj) == 14:
        request = requests.get(f'https://api-publica.speedio.com.br/buscarcnpj?cnpj={cnpj}')
        Cnpj_adress = request.json()
        sy('cls')
        banner_cnpj()
        print(f'''{g}╭
{g}│{n}CNPJ: {g}{(Cnpj_adress['CNPJ'])}
{g}│{n}NOME: {g}{(Cnpj_adress['NOME FANTASIA'])}
{g}│{n}RAZAO SOCIAL: {g}{(Cnpj_adress['RAZAO SOCIAL'])}        
{g}│{n}DESCRIÇÃO: {g}{(Cnpj_adress['CNAE PRINCIPAL DESCRICAO'])}       
{g}│{n}CNEA: {g}{(Cnpj_adress['CNAE PRINCIPAL CODIGO'])}
{g}│{n}STATUS: {g}{(Cnpj_adress['STATUS'])}
{g}│{n}CEP: {g}{(Cnpj_adress['CEP'])}
{g}│{n}TIPO: {g}{(Cnpj_adress['TIPO LOGRADOURO'])}
{g}│{n}LOGRADOURO: {g}{(Cnpj_adress['LOGRADOURO'])}
{g}│{n}NUMERO: {g}{(Cnpj_adress['NUMERO'])}
{g}│{n}COMPLEMENTO{g}{(Cnpj_adress['COMPLEMENTO'])}
{g}│{n}BAIRRO: {g}{(Cnpj_adress['BAIRRO'])}
{g}│{n}MUNICIPIO: {g}{(Cnpj_adress['MUNICIPIO'])}
{g}│{n}UF: {g}{(Cnpj_adress['UF'])}
{g}│{n}DATA ABERTURA:{g}{(Cnpj_adress['DATA ABERTURA'])}
{g}│{n}TELEFONE: {g}{(Cnpj_adress['DDD'])} {g}{(Cnpj_adress['TELEFONE'])}
{g}│{n}E-MAIL: {g}{(Cnpj_adress['EMAIL'])}''')
        input(f'''{g}│
╰──>    APERTE ENTER PARA CONTINUAR.{w}''')
    if cnpj == '*':
        pass
    elif len(cnpj) == 0:
        print(f'''{r}
│ ERRO!
╰──>    FAVOR INSERIR ALGUM VALOR.{w}''')
        s(1.5)
        sy('cls')
        consult_cnpj()
    else:
        print(f'''{ye}
│ ERRO!
╰──>    QUANTIDADE DE NUMEROS INVALIDA: {r}{len(cnpj)}{w}''')
        s(1.5)
        sy('cls')
        banner_cnpj()

    #https://api-publica.speedio.com.br/buscarcnpj?cnpj=00000000000191