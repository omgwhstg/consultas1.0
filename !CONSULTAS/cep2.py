import requests
from os import system as s
from time import sleep as t
import json
from colorama import *
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





def cep2():
            def fetch(url, uf, city, road) -> requests.models.Response:
              return requests.get(
                url.format(uf, city, road)
              )
            
            
            def format_response(response: list) -> str:
              msg = "Não encontrado."
              for obj in response:
                resp = "Endereço: "
                resp += f"\n  │{n} CEP: " f'{g}'+ obj.get("cep", msg)
                resp += f"\n  │{n} RUA: " f'{g}'+ obj.get("logradouro", msg)
                resp += f"\n  │{n} Bairro: " f'{g}'+ obj.get("bairro", msg)
                resp += f"\n  │{n} Complemento: " f'{g}'+ obj.get("complemento", msg)
            
                resp += f"\n  │{n} Estado: " f'{g}'+ obj.get("uf", msg)
                resp += f"\n  │{n} Cidade: " f'{g}'+ obj.get("localidade", msg)
            
                resp += f"\n  │   Extra: "
                resp += f"\n  │{n} Siafi: " f'{g}'+ obj.get("siafi", msg)
                resp += f"\n  │{n} IBGE: " f'{g}'+ obj.get("ibge", msg)
                resp += f"\n  │{n} DDD: " f'{g}'+ obj.get("ddd", msg)
                resp += f'''\n  │{n} GIA: 
  {g}╰─────''' f'{g}'+ obj.get("gia", msg)
                yield resp
            estado = input(f'''{n}
╰──>  DIGITE A UF (SP): {g}''')
            cidade = input(f'''{n}   ╰──>  DIGITE A CIDADE: {g}''')
            rua = input(f'''{n}      ╰──>  DIGITE A RUA: {g}''')

            address = {
              "estado": estado,
              "cidade": cidade,
              "rua": rua
            }
            address = json.loads(
              fetch(
                "https://viacep.com.br/ws/{}/{}/{}/json/",
                *address.values()
              ).text
            )
            
            print("Resultados: " + str(len(address)))
            for i in format_response(address):
                print("\n\n" + i) 
            input(f'''{g}│
╰──>    APERTE ENTER PARA CONTINUAR.{w}''')