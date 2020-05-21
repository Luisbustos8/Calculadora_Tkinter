import unittest
import tkinterTestcase
import calculator

from tkinter import *
from tkinter import ttk

class TestKeyboard(tkinterTestcase.tkTestCase):
    def setUp(self):
        self.k = calculator.Keyboard(self.root) #primero lo colgamos en la pantalla
        self.k.pack() #lo empaquetamos
        self.k.wait_visibility() #metodo para que lo pinte antes de probar test
    
    def tearDown(self):
        self.k.update() 
        self.k.destroy()

    def test_render_OK(self):
        self.assertEqual(self.k.winfo_height(), 250)
        self.assertEqual(self.k.winfo_width(), 272)
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.listaBNormales),18)

    def test_render_roman_OK(self):
        teclado_romano = calculator.Keyboard(self.root, "R")
        teclado_romano.pack()
        teclado_romano.wait_visibility()

        self.assertEqual(teclado_romano.winfo_height(), 250)
        self.assertEqual(teclado_romano.winfo_width(), 272)
        for btn in teclado_romano.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(teclado_romano.listaBRomanos),13)

    def test_change_staus_keyboard(self):
        self.assertEqual(self.k.status, "N")
        self.k.status = "R"
        for btn in self.k.children.values():
            self.assertIsInstance(btn, calculator.CalcButton)
        self.assertEqual(len(self.k.listaBRomanos),13)
        self.assertEqual(self.k.status, "R")

    

if __name__ == "__main__":
    unittest.main()