#from consulta placa carro import 
from cep import cep1
from cnpj import consult_cnpj
from ip1 import consult_IP
from os import system as sy
from time import sleep as s
from ipSite import consultSite
from whois import main_whois
from colorama import *
from cep2 import cep2
from banner import banner1

lg = Fore.LIGHTGREEN_EX
cy = Fore.CYAN
ye = Fore.YELLOW
r = Fore.RED
n = Fore.RESET
g = Fore.GREEN
p = Fore.MAGENTA
b = Fore.BLUE
w = Fore.WHITE
colors = [lg, r, cy, ye,b,w,g,n]



def menu_main():
    banner1()
    q1 = (input(f'''╰──>    SELECIONE UMA FUNÇÃO:
{cy}[1] IP
[2] CEP
[3] CEP2
[4] CNPJ
[5] PLACA
[6] GERAR PIX
[7] IP SITE
[8] WHOIS
[A] AJUDA
[S] SAIR
{w}
╰──> '''))

    if q1 == '1':
        sy('cls')
        consult_IP()
        sy('cls')
        menu_main()
    if q1 == '2':
        sy('cls')
        cep1()
        sy('cls')
        menu_main()
    if q1 == '3':
        sy('cls')
        cep2()
        sy('cls')
        menu_main()
    if q1 == '4':
        sy('cls')
        consult_cnpj()
        sy('cls')
        menu_main()
    if q1 == '5':
        sy('cls')
        pass
        sy('cls')
        menu_main()
    if q1 == '6':
        sy('cls')
        pass
        sy('cls')
        menu_main()
            
    if q1 == '7':
        sy('cls')
        consultSite()
        sy('cls')
        menu_main()
            
    if q1 == '8':
        sy('cls')
        main_whois()
        sy('cls')
        menu_main()
            

    if q1 == 'S':
        sy('cls')
        quit()

    if q1 == 's':
        sy('cls')
        quit()

    if q1 == 'A':
        sy('cls')
        pass
        sy('cls')
        menu_main()
    if q1 == 'a':
        sy('cls')
        pass
        sy('cls')
        menu_main()
            
    else:
            print('''
│ ERRO!
╰──>     ESCOLHA UMA OPÇÃO VALIDA.''')
            s(1)
            sy('cls')
            menu_main()