import tkinter as tk
from criptoquery2 import WIDTH, HEIGHT
from criptoquery2.models import criptos, fiats, get_rate
from criptoquery2.view import Buttons_of_List, A_Title, Display_resultado


class Controller2(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tipo de cambio de Cripto a Moneda")
        self.geometry(f"{WIDTH}x{HEIGHT}+400+200")

        title1 = A_Title(self,WIDTH/2,50,f"Elige una cripto:")
        title1.grid(row=0, column=0, padx=5)

        options1 = Buttons_of_List(self, self.click, criptos)
        options1.grid(row=1, column=0, padx = 5)

        options2 = Buttons_of_List(self, self.click, fiats)
        options2.grid(row=1, column=1, padx = 5)

        title2 = A_Title(self,WIDTH/2,50,"Elige una moneda:")
        title2.grid(row=0, column=1, padx = 5)

        title3 = A_Title(self,290,50,f"Resultado")
        title3.grid(row=2, column=0, columnspan=2, sticky='WE', pady = 10)

        self.display = Display_resultado(self)
        self.display.grid(row=3, column=0, columnspan=2, sticky='WE')
        self.display.typing(f" 1 [ELIGE UNA CRIPTO] son ______ [ELIGE UNA MONEDA]")

        self.cripto = '[ELIGE UNA CRIPTO]'
        self.fiat = '[ELIGE UNA MONEDA]'
            
    def click(self, tecla):
        if tecla in criptos:
            self.cripto = tecla
        else:
            self.fiat = tecla
        self.display.typing(f" 1 {self.cripto} son ______ {self.fiat}")
        if self.cripto != '[ELIGE UNA CRIPTO]' and self.fiat != '[ELIGE UNA MONEDA]':
            status, data, code = get_rate(self.cripto, self.fiat)
            if status:
                self.display.typing(f" 1 {self.cripto} son {data:.2f} {self.fiat}")
            else:
                self.display.typing(f" ERROR {code}\n{data}")
       
       

## CODIGO NO USADO ##


class Controller(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Tipo de cambio de Cripto a Moneda")
        self.geometry(f"800x800+100+100")

        #Aqui intento hacer una Entry, pero lo dejo porque prefiero una listbox
        userinput = tk.StringVar()
        entry1 = tk.Entry(self, textvariable=userinput)
        #FALTA COMPROBAR QUE EL INPUT ESTA EN LA LISTA CRIPTOS o FIAT
        entry1.pack(pady=20)

        #Aqui intento hacer una listbox, pero no se como sacar el elemento seleccionado. 
        self.list1 = tk.StringVar()
        self.list1.set(criptos)
        listbox1 =tk.Listbox(self, height=5, width=20, selectmode = tk.SINGLE, listvariable=self.list1, font="georgia 14 bold")
        listbox1.pack(pady=10)

        #Probando el mode BROWSE
        self.listbox2 =tk.Listbox(self, height=5, width=20, selectmode = tk.BROWSE, listvariable=self.list1, font="georgia 14 bold")
        self.listbox2.pack(pady=10)

        #Aqui intento hacer un scroll. Lo intento tambien creando una clase Frame
        frame = Frame_Scroll(self,100,100,self.list1)
        frame.pack()


class Frame_Scroll(tk.Frame):
    def __init__(self, location, w, h, list):
        super().__init__(location, width=w, height=h)
        self.list1 = list
        self.pack_propagate(False) 
        yscroll = tk.Scrollbar(self, orient='vertical')
        yscroll.pack(side=tk.RIGHT, fill=tk.BOTH)
        listbox =tk.Listbox(self, height=2, width=20, selectmode = tk.SINGLE, listvariable=self.list1, font="georgia 14 bold")
        listbox.pack(pady=10)

        '''
        yscroll = tk.Scrollbar(self, orient=VERTICAL)   
        self.listbox3=tk.Listbox(self, height=5, width=20, listvariable=self.list1, font="georgia 14 bold", yscrollcommand=self.yScroll.set)
        #self.yScroll[tk.SCROLL, 1, tk.UNITS] = self.listbox1.yview
        self.listbox1.pack()'''