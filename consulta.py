import requests


apikey = '6FD88A14-4B8A-42A5-8884-EE08E9FDC460'

url = f"https://rest.coinapi.io/v1/exchangerate/BTC/EUR?apikey={apikey}"

response = requests.get(url)

print(response.status_code) #response es un objeto y status_code es un objeto. El codigo que salga sera el error
print(response.text) #Esto es para que imprima la respuesta

#request me crea un objeto response que tiene un metodo llamado json