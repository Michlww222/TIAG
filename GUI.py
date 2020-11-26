# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:26:21 2020

@author: Paweł Świder
"""

import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk

class Window(tk.Frame):
    def __init__(self,graph_photos, master=None, ):
        """
        graph_photos - tablica z plikami png zawierającymi grafy
        """
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1280x720")
        self.graph_photos = graph_photos
        
        graph_frame = tk.Frame(self.master, height=400, width=400, bg="red")
        graph_frame.place(x=0, y=0)
        
        text = tk.Label(self.master, text="Just do it")
        text.place()
        print(self.graph_photos)
        self.show_image_at_position(self.graph_photos[0], 100, 100, 300, 300)
        #self.show_image_at_position(self.graph_photos[1], 100, 100, 200, 200)
        #self.show_image_at_position(self.graph_photos[2], 500, 100, 200, 200)
        
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
        photo = ImageTk.PhotoImage(img)
        panel = tk.Label(self.master, image = photo)
        panel.image = photo
        panel.place(x=x,y=y)
        


graph_photos = ["test1.png", "test2.png", "test3.png"]
graph_photos = ["results/" + photo for photo in graph_photos]
root = tk.Tk()
app = Window(graph_photos, root )
root.wm_title(" Transformacje i algorytmy grafowe")
root.mainloop()