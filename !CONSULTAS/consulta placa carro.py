import requests
#https://wdapi.com.br/placas/placa/token
def placa():
    placas = input('[*] Digite a placa do carro: ')
    request = requests.get(f'https://wdapi.com.br/{placas}/placa/402228e666d9fee5358d3a5459ed09c4')
    placa_carro = request.json()
    print(placa_carro)
if __name__ == '__main__':
    placa() 