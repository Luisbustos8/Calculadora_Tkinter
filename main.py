from tkinter import *
from tkinter import ttk

import calculator


class Mainapp(Tk):
    def __init__(self):
        Tk.__init__(self)
        self.title("Calculadora")
        self.geometry("272x300")
        self.propagate(0)

        c = calculator.Controlator(self)
        c.pack(side=TOP, fill=BOTH)


    def start(self):
        self.mainloop()


if __name__ == "__main__":
    app = Mainapp()
    app.start()