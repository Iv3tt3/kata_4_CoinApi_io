import tkinter as tk
from tkcriptoquery.view import Desplegable
from tkcriptoquery.models import get_rate



class Converter(tk.Tk):
    def __init__(self):
        super().__init__()
        
        self.title("Tipo de cambio de Cripto a Moneda")
        self.geometry(f"600x300+200+200")

        self.criptos = Desplegable(self,"Seleccionar opcion", 'BTC', 'ETH', 'USDT', 'BNB', 'USDC')
        self.criptos.grid(row=0, column=0)

        self.fiats = Desplegable(self,"Seleccionar opcion", 'EUR', 'USD', 'JPY')
        self.fiats.grid(row=0, column=1)

        self.result = tk.Label(self)
        self.result.grid(row=3, column=0, columnspan=1)

        self.buton = tk.Button(self, text='Consultar', command=self.get_rates).grid(row=1, column=1)
    
    def get_rates(self):
            cripto = self.criptos.selected_option.get()
            fiat = self.fiats.selected_option.get()

            if cripto != "Seleccionar opcion" and fiat != "Seleccionar opcion":
                status, data, code = get_rate(cripto, fiat)
                if status:
                    self.result.config(text=f" 1 {cripto} son {data:.2f} {fiat}")
                else:
                    self.result.config(f" ERROR {code}\n{data}")

            else:
                self.result.config(text='Debes seleccionar una opcion de cripto y de moneda')