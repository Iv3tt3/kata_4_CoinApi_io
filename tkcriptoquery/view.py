import tkinter as tk


class Desplegable(tk.Frame):
    def __init__(self, location, title, *options):

        super().__init__(location, width=200, height=50)
        self.pack_propagate(False) 

        # Variable para almacenar la opción seleccionada
        self.selected_option = tk.StringVar(self)
        self.selected_option.set(title)  # Opción seleccionada por defecto

        # Crear el menú desplegable
        option_menu = tk.OptionMenu(self, self.selected_option, *options)
        option_menu.pack()