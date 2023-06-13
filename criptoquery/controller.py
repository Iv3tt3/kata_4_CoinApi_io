from criptoquery.view import test_input, output
from criptoquery.models import get_rate, criptos, fiats


class Controller:
    def mainloop(self):
        while True:
            cripto = test_input(criptos, "Que cripto quieres saber?")
            fiat = test_input(fiats, "En que la quieres?")

            status, data, code = get_rate(cripto, fiat)

            output(status, data, code, cripto, fiat)

            more_conversions = test_input(('S', 'N'), "Quieres saber mas criptos?")
            
            if more_conversions != 'S':
                break