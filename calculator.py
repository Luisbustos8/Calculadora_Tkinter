from tkinter import *
from tkinter import ttk

dbuttons = [
    {
        "text": "1",
        "col": 0,
        "row": 4
    },
    {
        "text": "2",
        "col": 1,
        "row": 4
    },
    {
        "text": "3",
        "col": 2,
        "row": 4
    },
    {
        "text": "+",
        "col": 3,
        "row": 4,
        "bg":"#f5923e"
    },
    {
        "text": "4",
        "col": 0,
        "row": 3
    },
    {
        "text": "5",
        "col": 1,
        "row": 3
    },
    {
        "text": "6",
        "col": 2,
        "row": 3
    },
    {
        "text": "-",
        "col": 3,
        "row": 3,
        "bg":"#f5923e"
    },
    {
        "text": "7",
        "col": 0,
        "row": 2
    },
    {
        "text": "8",
        "col": 1,
        "row": 2
    },
    {
        "text": "9",
        "col": 2,
        "row": 2
    },
    {
        "text": "x",
        "col": 3,
        "row": 2,
        "bg": "#f5923e"
        
    },
    {
        "text": "C",
        "col": 1,
        "row": 1
    },
    {
        "text": "+/-",
        "col": 2,
        "row": 1
    },
    {
        "text": "÷",
        "col": 3,
        "row": 1,
        "bg":"#f5923e"
    },
    {
        "text": "0",
        "col": 0,
        "row": 5,
        "W": 2
    },
    {
        "text": ",",
        "col": 2,
        "row": 5
    },
    {
        "text": "=",
        "col": 3,
        "row": 5,
        "bg": "#f5923e"
    }
]

def pinta(valor):
    print(valor)
    return valor

class Controlator(ttk.Frame):
    def __init__(self, parent, **kwargs):
        ttk.Frame.__init__(self, parent, width=272, height=300)
        self.reset()


        self.display = Display(self)
        self.display.grid(column=0, row=0, columnspan=4)

        for properties in dbuttons:
            btn = CalcButton(self, properties["text"], self.set_operation, properties.get("W", 1), properties.get("H",1))
            btn.grid(column=properties["col"], row=properties["row"], columnspan=properties.get("W",1), rowspan=properties.get("H", 1))
            

        self.selector = Selector(self)
        self.selector.grid(column=0, row=1)
        
        
        

        

    def reset(self):
        self.op1 = None
        self.op2 = None
        self.operation = ""
        self.dispValue = "0"
        self.signo_recien_Pulsado = False

    def toFloat(self, valor):
        return float(valor.replace(",","."))

    def toStr(self, valor):
        return str(valor.replace(".",","))

    def calculate(self):
        if self.operation == "+":
            return self.op1 + self.op2
        
        if self.operation == "-":
            return self.op1 - self.op2
        
        if self.operation == "x":
            return self.op1 * self.op2
        
        if self.operation == "÷":
            return self.op1 / self.op2

        return self.op2

        
    def set_operation(self, algo):
        
        if algo.isdigit():
            if self.dispValue == "0" or self.signo_recien_Pulsado:
                self.op1 = self.toFloat(self.dispValue)
                self.op2 = None
                self.dispValue = algo
            else:
                self.dispValue += str(algo)

        if algo == "C":
            self.reset()
        
        if algo == "+/-" and self.dispValue != "0":
            if self.dispValue[0] == "-":
                self.dispValue = self.dispValue[1:]
            else:
                self.dispValue = "-" + self.dispValue

        if algo == "," and "," not in self.dispValue:
            self.dispValue += str(algo)
      
        
        if algo == "+" or algo == "-" or algo == "x" or algo == "÷":
            if self.op1 == None:
                self.op1 = self.toFloat(self.dispValue)
                self.operation = algo    
            elif self.op2 == None:
                self.op2 = self.toFloat(self.dispValue)
                res = self.calculate()
                self.dispValue = self.toStr(str(res)) 
                self.operation = algo
            else:
                self.op1 = self.toFloat(self.dispValue)
                self.op2 = None
                self.operation = algo
            self.signo_recien_Pulsado = True
        else:
            self.signo_recien_Pulsado = False

        
        if algo == "=":
            if self.op1 != None and self.op2 == None:
                self.op2 = self.toFloat(self.dispValue)
                res = self.calculate()
                self.dispValue = self.toStr(str(res)) 

            elif self.op1 != None and self.op2 != None:
                self.op1 = self.toFloat(self.dispValue)
                res = self.calculate()
                self.dispValue = self.toStr(str(res))

        self.display.paint(self.dispValue)

class Display(ttk.Frame):

    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, width=272, height=50)
        self.pack_propagate(0)

        s = ttk.Style()
        s.theme_use("alt")
        s.configure("my.TLabel", font= "Helvetica 30", background="black", foreground="white")

        self.value = "0"
        

        self.lbl = ttk.Label(self, text=self.value, anchor=E, style="my.TLabel")
        self.lbl.pack(side=TOP, fill=BOTH, expand=True)

    def paint(self, algo):
        self.value = algo
        self.lbl.config(text=algo)

class Selector(ttk.Frame):
    def __init__(self, parent, status="N"):
        ttk.Frame.__init__(self, parent, width=68, height=50)
        self.status = status
        


        radiob1 = ttk.Radiobutton(self, text="N", value="N", name="rbtn_normal", variable=self.status)
        radiob1.place(x=0, y=5)
        radiob2= ttk.Radiobutton(self, text="R", value="R", name="rbtn_romano", variable=self.status)
        radiob1.place(x=0, y=30)

       
        self.Roman = StringVar(value="R")
        self.Normal = StringVar(value="")
        rb1 = ttk.Radiobutton(self, text="Roman", value="R")
        rb1.place(x=0, y=5)
        rb2 = ttk.Radiobutton(self, text="Normal", value="N")
        rb2.place(x=0, y=30)    
       

class CalcButton(ttk.Frame):
    def __init__(self, parent, value, command, width=1, height=1):
        ttk.Frame.__init__(self, parent, width=68*width, height=50*height)
        self.pack_propagate(0)


        btn = ttk.Button(self, text=value, command=lambda: command(value))
        btn.pack(side=TOP, fill=BOTH, expand=True)
        
        
    

