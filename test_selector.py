import unittest
import tkinterTestcase
import calculator

from tkinter import *
from tkinter import ttk

class TestSelector(tkinterTestcase.tkTestCase):
    def setUp(self):
        self.s = calculator.Selector(self.root)
        self.s.pack()
        self.s.wait_visibility()

    def tearDown(self):
        self.s.update()
        self.s.destroy()

    def test_render_OK(self):
        children = self.s.children
        self.assertEqual(self.s.status, "N")
        self.assertEqual(self.s.winfo_height(),50)
        self.assertEqual(self.s.winfo_width(), 68)
        self.assertEqual(children["rbtn_romano"].config()["text"][4], "R")
        self.assertEqual(children["rbtn_normal"].config()["text"][4], "N")
        self.assertTrue(isinstance(children["rbtn_romano"],ttk.Radiobutton))
        self.assertTrue(isinstance(children["rbtn_normal"],ttk.Radiobutton))
        
        
    def test_init_value_R(self):
        r_selector = calculator.Selector(self.root, "R")
        self.assertEqual(r_selector.status, "R")

    def test_click_change_status(self):
        rbtn_romano = self.s.children["rbtn_romano"]
        self.assertEqual(self.s.status, "N")
        rbtn_romano.invoke()
        self.assertEqual(self.s.status, "R")

    


        
        

if __name__ == "__main__":
    unittest.main()