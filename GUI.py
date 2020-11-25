# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:26:21 2020

@author: Paweł Świder
"""

import tkinter as tk
from PIL import ImageTk, Image

class Window(tk.Frame):
    def __init__(self, master=None):
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1280x720")
        menu = tk.Menu(self.master)
        fileMenu = tk.Menu(menu)
        fileMenu.add_command(label="Item")
        fileMenu.add_command(label="Exit", command=self.exitProgram)
        menu.add_cascade(label="File", menu=fileMenu)
        menu.add_command(label="Edit")
        self.master.config(menu=menu)
        
        text = tk.Label(self.master, text="Just do it")
        text.place(x=100,y=100)
        self.show_image_at_position("test.jpg", 400, 300, 200, 300)

    def exitProgram(self):
        self.master.destroy()
        
    def show_image_at_position(self,path, x, y, width, height):
        """
        Umieszcza obraz na danej pozycji
        path - scieżka do obrazu
        x - współrzędna x lewego górnego rogu
        y - współrzędna y lewego górnego roku
        width - szerekosć obrazu
        height - wysokosc obrazu
        """
        img = Image.open(path)
        img = img.resize((width, height))
        img = ImageTk.PhotoImage(img)
        panel = tk.Label(self.master, image = img)
        panel.image = img
        panel.place(x=x,y=y)
        


root = tk.Tk()
app = Window(root)
root.wm_title(" Transformacje i algorytmy grafowe")
root.mainloop()