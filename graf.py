import matplotlib
import tkinter as tk
from tkinter import filedialog, simpledialog
import pylab as pl


class graf(tk.Tk):
    name = "graf"
    def __init__(self):
        super().__init__(className=self.name)
        self.title(self.name)
        self.bind("<Escape>", self.quit)
        self.lbl = tk.Label(self, text="Výběr souboru")
        self.lbl.pack()
        self.choosebtn = tk.Button(self, text="Vyber soubor", command=self.choose)
        self.choosebtn.pack()
        self.showbtn = tk.Button(self, text = "Show", command=self.show)
        self.showbtn.pack()
        self.quitbtn = tk.Button(self,text="Quit", command=self.quit)
        self.quitbtn.pack()

    def choose(self):
        self.filename = filedialog.askopenfilename()
        self.lbl.config(text=self.filename)

    def show(self):
        if not self.filename:
            return
        axisx = []
        axisy = []
        with open(self.filename, "r") as f:
            while line := f.readline():
                x, y = line.split()
                axisx.append(float(x))
                axisy.append(float(y))
            pl.plot(axisx, axisy)        
            pl.show()

app = graf()
app.mainloop()



