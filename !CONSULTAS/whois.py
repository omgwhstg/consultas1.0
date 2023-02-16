import requests
from colorama import *
from banner import banner_whois
# Seu código aqui

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
def main_whois():
  banner_whois()
  site = input(f'''{ye}[*] PARA VOLTAR AO MENU.
    ╰──>  DIGITE O SITE QUE DESEJA BUSCAR: {r}''')
  site.replace('https://','')
  site.replace('www.','')
  url = f'https://api.apilayer.com/whois/query?domain={site}'

  payload = {}
  headers= {
    "apikey": "iY7nkSQFeAiFSFjTTgLRtovlE7FSLCtd"
  }

  response = requests.get(url, headers=headers, data = payload)
  result = response.json()
  print(result)
  print(f'''
  │DOMANAIN NAME :{g}{result["result"]["domain_name"]}{n}
  │WHOIS SERVER :{g}{result["result"]["whois_server"]}{n}
  │REFERRAL URL :{g}{result["result"]["referral_url"]}{n}
  │UPDATED DATE :{g}{result["result"]["updated_date"]}{n}
  │CREATION DATE :{g}{result["result"]["creation_date"]}{n}
  │EXPIRATION DATE :{g}{result["result"]["expiration_date"]}{n}
  │E-MAILS :{g}{result["result"]["emails"]}{n}
  │DNSSEC :{g}{result["result"]["dnssec"]}{n}
  │NAME :{g}{result["result"]["name"]}{n}
  │ORG :{g}{result["result"]["org"]}{n}
  │ADDRESS :{g}{result["result"]["address"]}{n}
  │CITY :{g}{result["result"]["city"]}{n}
  │STATE :{g}{result["result"]["state"]}{n}
  │ZIPCODE :{g}{result["result"]["zipcode"]}{n}
  │COUNTRY :{g}{result["result"]["country"]}{n}
  ''')
  input(f'''{g}│
  ╰──>   APERTE ENTER PARA CONTINUAR.{w}''')
  if site == '*':
      pass