import tkinter as tk
from tkinter.font import Font


class A_Title(tk.Frame):
    def __init__(self, location, w, h, text):
        super().__init__(location, width=w, height=h)
        self.text = text
        self.pack_propagate(False) 
        f = Font(family='Helvetica',size=18, weight='bold')
        self.label = tk.Label(self, text=self.text, background="#2964A7", foreground="#FFFFFF",
                               padx=8, 
                              font=f)
        self.label.pack(side=tk.TOP, fill=tk.BOTH, expand=True)


class Create_button(tk.Button):
    def __init__(self, location, text, command):
        super().__init__(location, text=text, command=self.pressed)
        self.text = text
        self.command = command
    
    def pressed(self):
        self.command(self.text)

class Buttons_of_List(tk.Frame):
    def __init__(self, location, command, the_list):
        super().__init__(location, width=100, height=200)
        self.pack_propagate(False) 
        for item in the_list:
            Create_button(self, text=item, command=command).pack(side=tk.TOP, fill=tk.BOTH, expand=True)
            
class Display_resultado(tk.Frame):
    def __init__(self, location):
        super().__init__(location, width=272, height=50)
        self.pack_propagate(False)
        f = Font(family='Helvetica',size=19, weight='bold')
        self.label = tk.Label(self, foreground="#000000", padx=8, font=f)
        self.label.pack()

    def typing(self,text):
        self.label.config(text=text) 
            

