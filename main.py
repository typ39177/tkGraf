#!/usr/bin/env python3

from os.path import basename, splitext
import tkinter as tk
from tkinter import filedialog
import pylab as pl
# from tkinter import ttk


class MyEntry(tk.Entry):
    def __init__(self, master=None, cnf={}, **kw):
        super().__init__(master, cnf, **kw)

        if not "textvariable" in kw:
            self.variable = tk.StringVar()
            self.config(textvariable=self.variable)
        else:
            self.variable = kw["textvariable"]

    @property
    def value(self):
        return self.variable.get()

    @value.setter
    def value(self, new: str):
        self.variable.set(new)



class Application(tk.Tk):
    name = basename(splitext(basename(__file__.capitalize()))[0])
    name = "Vykreslení grafu"

    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Hello tkGraf")
        self.lbl.pack()

        self.fileframe = tk.LabelFrame(self, text="Soubor")
        self.fileframe.pack(padx=5, pady=5, fill="x")
        self.fileEntry=MyEntry(self.fileframe)
        self.fileEntry.pack(fill="x")
        self.filebtn = tk.Button(self.fileframe, text="...", command=self.choosefile)
        self.filebtn.pack(anchor="e")
        
        self.dataDirection = tk.StringVar(value="row")
        self.rowRadio = tk.Radiobutton(self.fileframe, variable=self.dataDirection, value="row", text="Data jsou v řádcích.")
        self.rowRadio.pack(anchor="w")
        self.collumnRadio = tk.Radiobutton(self.fileframe, text="Data jsou ve sloupcíh.", variable=self.dataDirection, value="collumn")
        self.collumnRadio.pack(anchor="w")
        

        self.btndraw =tk.Button(self.fileframe, text="Kresli", command=self.plot)
        self.btndraw.pack()
        self.btn = tk.Button(self, text="Quit", command=self.quit)
        self.btn.pack(fill="x")

    def choosefile(self):
        path = filedialog.askopenfilename()
        self.fileEntry.value = path
    
    def plot(self):
        with open(self.fileEntry.value) as f:
            if self.dataDirection.get() == "row":
                line = f.readline()
                x = line.split(";")
                line = f.readline()
                y = line.split(";")
                x = [ float(i.replace(',','.')) for i in x]
                y = [ float(i.replace(',','.')) for i in y]
        pl.plot(x, y)
        pl.show()
            

    def quit(self, event=None):
        super().quit()


app = Application()
app.mainloop()