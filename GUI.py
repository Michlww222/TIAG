# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 20:26:21 2020

@author: Paweł Świder
"""

import tkinter as tk
from PIL import ImageTk, Image
import tkinter.ttk
import read_Graph as readG
import GraphData
import os
import produce_Graph

class Window(tk.Frame):
    def __init__(self,master=None, production_dir = "productions",
                 final_graph_dir = "results", starts_graph_dir = "grafy_startowe"):
        """
        master - Parent of the window
        production_dir - Directory which contains productions files
        final_graph_dir - Directrory which contains results graphs
        starts_graph_dir - Directory which contains start_graphs
        """
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1080x620")

        self.production_dir = production_dir
        self.final_graph_dir = final_graph_dir
        self.starts_graph_dir = starts_graph_dir

        self.final_graph_dir = final_graph_dir

        start_graph_paths = self.find_paths(starts_graph_dir)
        results_graph_paths = self.find_paths(final_graph_dir)
        self.graph_paths = start_graph_paths + results_graph_paths
        
        menu_frame = tk.Frame(self.master, bg="white")
        menu_frame.pack(side="left", fill = "y")
        show_frame = tk.Frame(self.master, bg = "gray")
        show_frame.pack(fill = "both", expand = "yes")
        
        menu_graph_frame = tk.Frame(menu_frame, bg = "white")
        menu_graph_frame.pack(side="top")
        
        graphs = tk.Label(menu_graph_frame, text = "Graphs", bg = "green")
        graphs.pack()
        
        graph_listbox = self.pack_listbox(menu_graph_frame, self.graph_paths)
        
        graph_next = tk.Button(menu_graph_frame, bg="gray", text = "Next",
                               command = lambda:self.next_button(graph_listbox, True))
        graph_next.pack()
        graph_previous = tk.Button(menu_graph_frame, bg="gray", text = "Previous",
                                   command = lambda: self.previous_button(graph_listbox, True))
        graph_previous.pack()

        productions_menu_frame = tk.Frame(menu_frame, bg= "white")
        productions_menu_frame.pack(side="bottom")
        
        productions = tk.Label(productions_menu_frame, text = "Productions", bg="green")
        productions.pack(fill = "y")
        
        self.productions_paths = self.find_paths(production_dir)
        production_listbox = self.pack_listbox(productions_menu_frame,
                          self.productions_paths, graphlistbox=False)
        
        productions_next = tk.Button(productions_menu_frame, bg="gray", text = "Next",
                                     command = lambda: self.next_button(production_listbox, False))
        productions_next.pack()
        productions_next = tk.Button(productions_menu_frame, bg="gray", text = "Previous",
                                     command = lambda: self.previous_button(production_listbox, False))
        productions_next.pack()

        #Produce button
        produce = tk.Button(text="Produce", bg="green", 
                        command = lambda: self.produce_button(graph_listbox, production_listbox))
        produce.place(x=42, y=270)
        
        #Graph and stats visualization
        self.stats_frame = tk.Frame(show_frame, bg = "green", width = 150, )
        self.stats_frame.pack(side = "bottom")
        self.photos_frame = tk.Frame(show_frame, bg = "grey")
        self.photos_frame.pack(fill="both", expand = "yes")
        
        self.show_graph("Barry", self.photos_frame, self.stats_frame)
        
    def frame_destroy_content(self, frame):
        """
        Destroy each element which is his child
        Frame - Frame to destroy content
        """
        children = frame.winfo_children()
        for child in children:
            child.destroy()

    def show_graph(self, name, photo_frame, stats_frame):
        """
        Show graph and it's statistics
        name - Name of graph
        photo_frame - Frame where we put graph photo
        stats_frame - Frame where we put graph statictics
        """
        self.frame_destroy_content(photo_frame)
        self.frame_destroy_content(stats_frame)
        
        graph = readG.read_Graph(self.starts_graph_dir, name)
        if graph.body == []:
            graph = readG.read_Graph(self.final_graph_dir, name)

        readed_graph = GraphData.GraphData(graph)
        graph_stats = readed_graph.get_data()
        self.pack_graph_statistics(stats_frame,graph_stats)
        
        label = tk.Label(photo_frame, text=name, bg = "grey")
        label.pack()
        path_to_png = graph.render(filename=name, directory = "graph_photos",
                                   cleanup=True, format="png")
        
        graph_image = self.label_graph_image(photo_frame, path_to_png)
        graph_image.pack(pady= 20, padx = 20)

    def show_production(self, name, photo_frame, stats_frame):
        """
        Show production graphs and embedding transformation
        name - name of production 
        photo_frame - Frame where we put transformation graphs
        stats_frame - Frame where we put embedding transformation
        """
        self.frame_destroy_content(photo_frame)
        self.frame_destroy_content(stats_frame)
        
        production = readG.read_Production(name)
        self.pack_embedding_transformation(stats_frame, production.T)
        
        label = tk.Label(photo_frame, text=name,  pady = 50, bg = "grey")
        label.pack()
        
        path_to_png = production.R.render(filename=name+"_right", format="png",
                            directory = "graph_photos", cleanup=True)
        rigth_image = self.label_graph_image(photo_frame, path_to_png)
        rigth_image.pack(padx= 100, side="right")
        
        path_to_png = production.L.render(filename=name+"_left", format="png",
                            directory = "graph_photos", cleanup=True)
        
        left_image = self.label_graph_image(photo_frame, path_to_png)
        left_image.pack(padx= 100, side = "left")
        
    def label_graph_image(self, frame, path):
        """
        Creating a Tkinter Label with Image
        frame - Frame  where we want have image
        path - path to the image
        """
        loaded_image = Image.open(path)
        rendered_image = ImageTk.PhotoImage(loaded_image)
        label_with_image = tk.Label(frame, image = rendered_image, anchor="center")
        label_with_image.image = rendered_image
        return label_with_image
        
    def next_button(self, listbox, graph_or_production):
        """
        Przełącza graf na następny
        listbox - listbox w której mamy włączyć następny element
        graph_or_production - True jesli listbox grafów, false jesli produkcji
        """
        
        if len(listbox.curselection()) == 0:
            return
        idx = int(listbox.curselection()[0])
        try:
            if idx == listbox.size() -1:
                raise AttributeError
            listbox.selection_clear(0, listbox.size())
            listbox.activate(idx+1)
            listbox.selection_set(idx+1)
            path = listbox.get(idx+1)
            print("Scieżka:" + path)
            self.selected_element_on_listbox(path, graph_or_production)
        except:
            print("It is the last index")

    def previous_button(self, listbox, graph_or_production):
        """
        Przełącza graf na następny
        listbox - listbox w której mamy włączyć następny element
        graph_or_production - True jesli listbox grafów, false jesli produkcji
        """
        
        if len(listbox.curselection()) == 0:
            return
        idx = int(listbox.curselection()[0])
        try:
            if idx == 0:
                raise AttributeError
            listbox.selection_clear(0, listbox.size())
            listbox.activate(idx-1)
            listbox.selection_set(idx-1)
            path = listbox.get(idx-1)
            print("Scieżka:" + path)
            self.selected_element_on_listbox(path, graph_or_production)
        except:
            print("It is the first index")

        
    def selected_element_on_listbox(self, path, is_graph):
        """
        Reaguje na nacisniecie listboxa
        """
        if is_graph == True:
            self.show_graph(path,self.photos_frame, self.stats_frame)
        else:
            self.show_production(path, self.photos_frame, self.stats_frame)
            
    def pack_listbox(self, frame, elements, graphlistbox = True):
        """
        Umieszcza listbox wraz ze scrollbarem zawierający wskazane elementy
        frame - Frame gdzie ma zostać umieszczony listbox
        elements - tablica zawierająca jakie elementy mają zawierać się w listboxie
        
        """
        listbox_frame = tk.Frame(frame)
        listbox_frame.pack()
        
        listbox = tk.Listbox(listbox_frame, exportselection=False)
        listbox.bind('<<ListboxSelect>>', lambda e:
                     self.selected_element_on_listbox(
                         listbox.get(listbox.curselection()), graphlistbox))
        for i, element in enumerate(elements):
            listbox.insert(i, element)
        listbox.pack(side="left", fill="both")
        
        scrollbar = tk.Scrollbar(listbox_frame)
        scrollbar.pack(side="right", fill="y")
        
        listbox.config(yscrollcommand = scrollbar.set)
        scrollbar.config(command = listbox.yview)
        
        return listbox
        
    def pack_graph_statistics(self, stats_frame, stats):
        """
        Umieszcza statystyki dotyczące grafu w wskazanym Framie
        stats_frame - Frame gdzie mają zostać umieszczone statystyki
        stats - tablica z wartosciami poszczególnych statystyk
        """
        title_stats_label = tk.Label(stats_frame, text = "Stats:", bg= "green")
        title_stats_label.pack()
        descriptions = ["Nodes:", "Edges:", "Components:",
                        "Average degree:","Average degree in a,b,c,d nodes:",
                        "Average nodes in degree:"]
        
        for description, stat in zip(descriptions, stats):
            element_frame = tk.Frame(stats_frame)
            element_frame.pack(fill="x")
            description_label = tk.Label(element_frame, text = description)
            description_label.pack(side="left", fill="x")
            stat_label = tk.Label(element_frame, text = str(stat))
            stat_label.pack(side = "right", fill="x")
            
    def pack_embedding_transformation(self,stats_frame, T):
        """
        Umieszcza szczegóły transformacji osadzenia w skazanym Framie
        stats_frame - Frame gdzie mają zostać umieszczone statystyki
        T - słownik zawierający transformacje osadzenia
        """
        title_trans_label = tk.Label(stats_frame,
                                     text = "Embedding transformation:", bg = "green")
        title_trans_label.pack()
        
        for key in T.keys():
            element_frame = tk.Frame(stats_frame)
            element_frame.pack(fill="x")
            description_label = tk.Label(element_frame, text = key)
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
        result_list = []
        for file in files_list:
            if ".dot" == file[-4:]:
                result_list.append(file[:-4])
        return result_list

    def produce_button(self, graph_listbox, production_listbox):
        """
        
        """
        try:
            g_name = self.graph_paths[graph_listbox.curselection()[0]]
            p_name = self.productions_paths[production_listbox.curselection()[0]]
        except: 
            print("Not selected graph and production")
            return
        print("Nazwy:", g_name, p_name)
        produce_Graph.produce(g_name,p_name)
        graph_listbox.insert(graph_listbox.size(), g_name+p_name)
        
        self.graph_paths.append(g_name+p_name)
        

root = tk.Tk()
app = Window(root)
root.wm_title(" Transformacje i algorytmy grafowe")
root.mainloop()