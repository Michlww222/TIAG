# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:26:21 2020

@author: Paweł Świder
"""

import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk
import os

class Window(tk.Frame):
    def __init__(self,master=None, production_dir = "productions",
                 final_graph_dir = "results", starts_graph_dir = "grafy_startowe"):
        """
        graph_photos - tablica z plikami png zawierającymi grafy
        production_dir - folder z produkcjami
        final_graph_dir - folder z grafami wynikowymi
        starts_graph_dir - floder z grafami startowymi
        """
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1080x620")
        self.graph_photos = graph_photos
        
        
        self.start_graph_paths = self.find_paths(starts_graph_dir)
        print(self.start_graph_paths)
        
        menu_frame = tk.Frame(self.master, bg="yellow")
        menu_frame.pack(side="left", fill = "y")
        show_frame = tk.Frame(self.master, bg = "green");
        show_frame.pack(fill = "both", expand = "yes")
        
        menu_graph_frame = tk.Frame(menu_frame, bg = "yellow")
        menu_graph_frame.pack(side="top")
        
        graphs = tk.Label(menu_graph_frame, text = "Graphs", bg = "yellow")
        graphs.pack()
        
        self.pack_listbox(menu_graph_frame, [str(i) for i in range(50)])
        
        graph_next = tk.Button(menu_graph_frame, bg="blue", text = "Next",
                               command = lambda:self.next_graph(show_frame))
        graph_next.pack()
        graph_previous = tk.Button(menu_graph_frame, bg="blue", text = "Previous")
        graph_previous.pack()
        
        productions_menu_frame = tk.Frame(menu_frame, bg= "red")
        productions_menu_frame.pack(side="bottom")
        
        productions = tk.Label(productions_menu_frame, text = "Productions", bg="blue")
        productions.pack(fill = "y")
        
        self.pack_listbox(productions_menu_frame, ["First", "Second", "Third", "Fourth", "Fifth"])
        
        productions_next = tk.Button(productions_menu_frame, bg="blue", text = "Next")
        productions_next.pack()
        productions_next = tk.Button(productions_menu_frame, bg="blue", text = "Previous")
        productions_next.pack()
        
        
        #self.show_image_at_position(self.graph_photos[1], 100, 100, 200, 200)
        #self.show_image_at_position(self.graph_photos[2], 500, 100, 200, 200)
        
        #wizualizacja grafów i statystyki
        stats_frame = tk.Frame(show_frame, bg = "blue", width = 150, )
        stats_frame.pack(side = "bottom")
        self.pack_graph_statistics(stats_frame, [1,1,1,1,1.25,1])
        #self.pack_embedding_transformation(stats_frame,{"a": "Y","b": "c",
        #                                                "c": "Y","d": "a",
        #                                                "X": "c","Y": "Y",})
        
        self.pack_graph_image(show_frame, self.graph_photos[0])
        #self.show_image_at_position(self.graph_photos[0], 400, 100, 300, 300)
        
    def pack_graph_image(self, frame, path):
        """
        Wstawia obraz znajdujący się z danym pliku w podane miejsce
        frame - Frame gdzie ma zostać umieszczony obraz
        path - scieżka do obrazu
        """
        loaded_image = Image.open(path)
        rendered_image = ImageTk.PhotoImage(loaded_image)
        label_with_image = tk.Label(frame, image = rendered_image)
        label_with_image.image = rendered_image
        label_with_image.place(relx = 0.5, rely = 0.5, 
                   anchor = 'center')
        
    def next_graph(self, frame):
        next_label = tk.Label(frame, text= "Next button pressed")
        next_label.pack(side= "right")
        next_label.after(3000, next_label.destroy) # samoznikający napis
        print("next pressed")
        
    def pack_listbox(self, frame, elements):
        """
        Umieszcza listbox wraz ze scrollbarem zawierający wskazane elementy
        frame - Frame gdzie ma zostać umieszczony listbox
        elements - tablica zawierająca jakie elementy mają zawierać się w listboxie
        """
        listbox_frame = tk.Frame(frame)
        listbox_frame.pack()
        
        listbox = tk.Listbox(listbox_frame)
        for i, element in enumerate(elements):
            listbox.insert(i, element)
        listbox.pack(side="left", fill="both")
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side="right", fill="y")
        
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        
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
            
    def find_paths(self, directory):
        """
        Znajduje nazwy plikow w formacie .dot dla wskazanego folderu
        directory - folder w którym szukami plików
        return - lista scieżek plików w formacie dot
        """
        files_list = os.listdir(directory)
        print(files_list)
        result_list = []
        for file in files_list:
            if ".dot" == file[-4:]:
                result_list.append(file)
        return result_list




graph_photos = ["test1.png", "test2.png", "test3.png"]
graph_photos = ["results/" + photo for photo in graph_photos]
root = tk.Tk()
app = Window(root)
root.wm_title(" Transformacje i algorytmy grafowe")
root.mainloop()