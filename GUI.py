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
        self.master.geometry("1080x620")
        self.graph_photos = graph_photos
        
        menu_frame = tk.Frame(self.master, bg="yellow")
        menu_frame.pack(side="left")
        
        menu_graph_frame = tk.Frame(menu_frame, width = 200, bg="blue")
        menu_graph_frame.pack(side="top")
        
        graphs = tk.Label(menu_graph_frame, text = "Graphs", bg = "blue")
        graphs.pack()
        
        
        graph_listbox_frame = tk.Frame(menu_graph_frame)
        graph_listbox = tk.Listbox(graph_listbox_frame, bg="blue")
        for i in range(100):
            graph_listbox.insert(i, str(i))
        graph_listbox.pack(side="left", fill="both")
        
        
        
        scrollbar = tk.Scrollbar(graph_listbox_frame)
        scrollbar.pack(side="right", fill="y")
        graph_listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = graph_listbox.yview)
        graph_listbox_frame.pack(fill="both")
        
        graph_next = tk.Button(menu_graph_frame, bg="blue", text = "Next")
        graph_next.pack()
        graph_next = tk.Button(menu_graph_frame, bg="blue", text = "Previous")
        graph_next.pack()
        
        productions_menu_frame = tk.Frame(menu_frame, bg= "red")
        
        productions = tk.Label(productions_menu_frame, text = "Productions", bg="blue")
        productions.pack(fill = "y")
        
        productions_listbox = tk.Listbox(productions_menu_frame, bg="blue")
        productions_listbox.insert(1, "First")
        productions_listbox.insert(2, "Second")
        productions_listbox.insert(3, "Third")
        productions_listbox.insert(4, "Fourth")
        productions_listbox.pack()
        
        productions_next = tk.Button(productions_menu_frame, bg="blue", text = "Next")
        productions_next.pack()
        productions_next = tk.Button(productions_menu_frame, bg="blue", text = "Previous")
        productions_next.pack()
        
        productions_menu_frame.pack(side="bottom")
        
        self.show_image_at_position(self.graph_photos[0], 400, 100, 300, 300)
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