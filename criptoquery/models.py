import requests

apikey = '6FD88A14-4B8A-42A5-8884-EE08E9FDC460'

criptos = ['BTC', 'ETH', 'USDT', 'BNB', 'USDC']
fiats = ['EUR', 'USD', 'JPY']



def get_rate(cripto, fiat):

    url = f"https://rest.coinapi.io/v1/exchangerate/{cripto}/{fiat}?apikey={apikey}"

    try: 
        response = requests.get(url)
        data = response.json() 
        if response.status_code == 200:
            return True, data['rate'], response.status_code
        else:
            return False, data['error'], response.status_code

    except requests.exceptions.RequestExceptipon as error_str:
        return False, str(error_str), url