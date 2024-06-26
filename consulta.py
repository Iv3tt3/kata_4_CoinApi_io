import requests


apikey = '6FD88A14-4B8A-42A5-8884-EE08E9FDC460'

criptos = ['BTC', 'ETH', 'USDT', 'BNB', 'USDC']
fiats = ['EUR', 'USD', 'JPY']

def test_input(list_of_valid_inputs, input_question):
    str_input = input(input_question)
    while str_input not in list_of_valid_inputs:
        print('Debe ser una de las siguientes opciones', list_of_valid_inputs)
        str_input = input(input_question)
    return str_input

cripto = test_input(criptos, "Que cripto quieres saber?")

fiat = test_input(fiats, "En que la quieres?")

url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}"

try: 
    response = requests.get(url)

    data = response.json() 

    if response.status_code == 200:
        print(f'1 {cripto} vale {data["rate"]:.2f} {fiat}') 
    else:
        print(response.status_code, "-", data['error'])

except requests.exceptions.RequestExceptipon:
    print("Se ha producido un error en la peticion:\n", url)