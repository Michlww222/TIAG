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
        menu_frame.pack(side="left", fill = "y")
        
        menu_graph_frame = tk.Frame(menu_frame, bg = "yellow")
        menu_graph_frame.pack(side="top")
        
        graphs = tk.Label(menu_graph_frame, text = "Graphs", bg = "yellow")
        graphs.pack()
        
        graph_listbox_frame = tk.Frame(menu_graph_frame)
        graph_listbox_frame.pack(fill="y")
        
        graph_listbox = tk.Listbox(graph_listbox_frame, bg="blue")
        for i in range(100):
            graph_listbox.insert(i, str(i))
        graph_listbox.pack(side="left", fill="both")
        
        graph_scrollbar = tk.Scrollbar(graph_listbox_frame)
        graph_scrollbar.pack(side="right", fill="y")
        
        graph_listbox.config(yscrollcommand = graph_scrollbar.set)
        graph_scrollbar.config(command = graph_listbox.yview)
        
        graph_next = tk.Button(menu_graph_frame, bg="blue", text = "Next")
        graph_next.pack()
        graph_previous = tk.Button(menu_graph_frame, bg="blue", text = "Previous")
        graph_previous.pack()
        
        productions_menu_frame = tk.Frame(menu_frame, bg= "red")
        productions_menu_frame.pack(side="bottom")
        
        productions = tk.Label(productions_menu_frame, text = "Productions", bg="blue")
        productions.pack(fill = "y")
        
        productions_listbox_frame = tk.Frame(productions_menu_frame)
        productions_listbox_frame.pack()
        
        productions_listbox = tk.Listbox(productions_listbox_frame, bg="blue")
        productions_listbox.insert(1, "First")
        productions_listbox.insert(2, "Second")
        productions_listbox.insert(3, "Third")
        productions_listbox.insert(4, "Fourth")
        productions_listbox.pack(side = "left")
        
        productions_scrollbar = tk.Scrollbar(productions_listbox_frame)
        productions_scrollbar.pack(side = "right", fill = "y")
        
        productions_listbox.config(yscrollcommand = productions_scrollbar.set)
        productions_scrollbar.config(command = productions_listbox.yview)
        
        productions_next = tk.Button(productions_menu_frame, bg="blue", text = "Next")
        productions_next.pack()
        productions_next = tk.Button(productions_menu_frame, bg="blue", text = "Previous")
        productions_next.pack()
        
        
        #self.show_image_at_position(self.graph_photos[1], 100, 100, 200, 200)
        #self.show_image_at_position(self.graph_photos[2], 500, 100, 200, 200)
        
        #wizualizacja grafów i statystyki
        show_frame = tk.Frame(self.master, bg = "green");
        show_frame.pack(fill = "both", expand = "yes")
        
        stats_frame = tk.Frame(show_frame, bg = "blue", width = 150, )
        stats_frame.pack(side = "bottom")
        self.pack_graph_statistics(stats_frame, [1,1,1,1,1.25,1])
        #self.pack_embedding_transformation(stats_frame,{"a": "Y","b": "c",
        #                                                "c": "Y","d": "a",
        #                                                "X": "c","Y": "Y",})
        
        self.show_image_at_position(self.graph_photos[0], 400, 100, 300, 300)
        
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
        
    def pack_graph_statistics(self, stats_frame, stats):
        """
        Umieszcza statystyki dotyczące grafu w wskazanym Framie
        stats_frame - Frame gdzie mają zostać umieszczone statystyki
        stats - tablica z wartosciami poszczególnych statystyk
        """
        title_stats_label = tk.Label(stats_frame, text = "Stats:")
        title_stats_label.pack()
        descriptions = ["Nodes:", "Edges:", "Components:",
                        "Average degree:","Average degree in a,b,c,d nodes:",
                        "Average nodes in degree:"]
        
        for description, stat in zip(descriptions, stats):
            element_frame = tk.Frame(stats_frame)
            element_frame.pack(fill="x")
            description_label = tk.Label(element_frame, text = description, bg= "yellow")
            description_label.pack(side="left", fill="x")
            stat_label = tk.Label(element_frame, text = str(stat))
            stat_label.pack(side = "right", fill="x")
            
    def pack_embedding_transformation(self,stats_frame, T):
        """
        Umieszcza szczegóły transformacji osadzenia w skazanym Framie
        stats_frame - Frame gdzie mają zostać umieszczone statystyki
        T - słownik zawierający transformacje osadzenia
        """
        title_trans_label = tk.Label(stats_frame, text = "Embedding transformation:")
        title_trans_label.pack()
        
        for key in T.keys():
            element_frame = tk.Frame(stats_frame)
            element_frame.pack(fill="x")
            description_label = tk.Label(element_frame, text = key, bg= "yellow")
            description_label.pack(side="left", fill="x")
            stat_label = tk.Label(element_frame, text = T[key])
            stat_label.pack(side = "right", fill="x")


graph_photos = ["test1.png", "test2.png", "test3.png"]
graph_photos = ["results/" + photo for photo in graph_photos]
root = tk.Tk()
app = Window(graph_photos, root )
root.wm_title(" Transformacje i algorytmy grafowe")
root.mainloop()