from criptoquery.view import test_input, output
from criptoquery.models import get_rate, criptos, fiats

while True:
    #Usamos view para la entrada de datos
    cripto = test_input(criptos, "Que cripto quieres saber?")
    fiat = test_input(fiats, "En que la quieres?")

    #Usamos models para obtener un dato de internet
    status, data, code = get_rate(cripto, fiat)

    #Usamos view para obtener el output de datos
    output(status, data, code, cripto, fiat)

    more_conversions = test_input(('S', 'N'), "Quieres saber mas criptos?")
    
    if more_conversions != 'S':
        break