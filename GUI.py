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
from produce_Graph import produce

class Window(tk.Frame):
    def __init__(self,master=None, production_dir = "productions",
                 final_graph_dir = "results", starts_graph_dir = "grafy_startowe"):
        """
        production_dir - folder z produkcjami
        final_graph_dir - folder z grafami wynikowymi
        starts_graph_dir - floder z grafami startowymi
        """
        tk.Frame.__init__(self, master)
        self.master = master
        self.master.geometry("1080x620")
        
        self.current_production_ID = 0
        self.current_graph_ID = 0

        self.final_graph_dir = final_graph_dir

        self.start_graph_paths = self.find_paths(starts_graph_dir)
        self.results_graph_paths = self.find_paths(final_graph_dir)
        self.graph_paths = self.start_graph_paths + self.results_graph_paths
        
        self.menu_frame = tk.Frame(self.master, bg="white")
        
        self.menu_frame.pack(side="left", fill = "y")
        show_frame = tk.Frame(self.master, bg = "gray")
        show_frame.pack(fill = "both", expand = "yes")
        
        menu_graph_frame = tk.Frame(self.menu_frame, bg = "white")
        menu_graph_frame.pack(side="top")

        self.menu_graph_frame = menu_graph_frame
        
        graphs = tk.Label(menu_graph_frame, text = "Graphs", bg = "green")
        graphs.pack()
        
        self.graph_listbox, self.graph_scrollbar, self.graph_listbox_frame = self.pack_listbox(menu_graph_frame, self.graph_paths)
        
        self.graph_next = tk.Button(menu_graph_frame, bg="gray", text = "Next",
                               command = lambda:self.next_button(self.graph_listbox, True))
        self.graph_next.pack()
        self.graph_previous = tk.Button(menu_graph_frame, bg="gray", text = "Previous",
                                   command = lambda: self.previous_button(self.graph_listbox, True))
        self.graph_previous.pack()

        productions_menu_frame = tk.Frame(self.menu_frame, bg= "white")
        productions_menu_frame.pack(side="bottom")
        
        productions = tk.Label(productions_menu_frame, text = "Productions", bg="green")
        productions.pack(fill = "y")
        
        self.productions_paths = self.find_paths(production_dir)
        production_listbox, _, _ = self.pack_listbox(productions_menu_frame,
                          self.productions_paths, graphlistbox=False)
        
        productions_next = tk.Button(productions_menu_frame, bg="gray", text = "Next",
                                     command = lambda: self.next_button(production_listbox, False))
        productions_next.pack()
        productions_next = tk.Button(productions_menu_frame, bg="gray", text = "Previous",
                                     command = lambda: self.previous_button(production_listbox, False))
        productions_next.pack()

        #przycisk produce
        produce = tk.Button(text="Produce", bg="green", command = lambda: self.produce(self.graph_listbox, production_listbox))
        produce.place(x=42, y=270)
        
        #wizualizacja grafów i statystyki
        self.stats_frame = tk.Frame(show_frame, bg = "green", width = 150, )
        self.stats_frame.pack(side = "bottom")
        self.photos_frame = tk.Frame(show_frame, bg = "grey")
        self.photos_frame.pack(fill="both", expand = "yes")
        
        self.show_graph("Barry", self.photos_frame, self.stats_frame)
        
    def frame_destroy_content(self, frame):
        """
        Usuwa każdy element będący dzieckiem okreslonego Frama
        frame - nazwa Frame dla której usuwamy dzieci
        """
        children = frame.winfo_children()
        print(children)
        for child in children:
            child.destroy()

    def show_graph(self, path, photo_frame, stats_frame):
        """
        Wyswietla graf wraz z jego statystykami
        path - scieżka gdzie zapisany jest graf
        photo_frame - Frame gdzie ma  zostać wyswietlony graf
        stats_frame - Frame gdzie mają zostać wyswietlone statystyki
        """
        self.frame_destroy_content(photo_frame)
        self.frame_destroy_content(stats_frame)
        
        graph = readG.read_Graph("grafy_startowe", path)
        if graph.body == []:
            graph = readG.read_Graph("results", path)
        print("Ciało grafu")
        print(graph.body)
        readed_graph = GraphData.GraphData(graph)
        graph_stats = readed_graph.get_data()
        self.pack_graph_statistics(stats_frame,graph_stats)
        
        path_to_png = graph.render(filename=path, directory = "graph_photos",
                                   cleanup=True, format="png")
        
        label = tk.Label(photo_frame, text=path, bg = "grey")
        label.pack()
        
        print(path_to_png)
        graph_image = self.label_graph_image(photo_frame, path_to_png)
        
        graph_image.pack(pady= 20, padx = 20)

    def show_production(self, path, photo_frame, stats_frame):
        """
        Wyswiatla dana produkcje wraz z transformacja osadzenia
                path - scieżka gdzie zapisany jest graf
        photo_frame - Frame gdzie ma  zostać wyswietlone grafy produkcji
        stats_frame - Frame gdzie mają zostać wyswietlone statystyki
        """
        self.frame_destroy_content(photo_frame)
        self.frame_destroy_content(stats_frame)
        
        production = readG.read_Production(path)
        self.pack_embedding_transformation(stats_frame, production.T)
        
        label = tk.Label(photo_frame, text=path,  pady = 50, bg = "grey")
        label.pack()
        
        path_to_png = production.R.render(filename=path+"_right", directory = "graph_photos",
                            cleanup=True, format="png")
        rigth_image = self.label_graph_image(photo_frame, path_to_png)
        rigth_image.pack(padx= 100, side="right")
        
        path_to_png = production.L.render(filename=path+"_left", directory = "graph_photos",
                            cleanup=True, format="png")
        left_image = self.label_graph_image(photo_frame, path_to_png)
        left_image.pack(padx= 100, side = "left")
        
    def label_graph_image(self, frame, path):
        """
        Wstawia obraz znajdujący się z danym pliku w podane miejsce
        frame - Frame gdzie ma zostać umieszczony obraz
        path - scieżka do obrazu
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
        
        return listbox, scrollbar, listbox_frame
        
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
        print(directory)
        files_list = os.listdir(directory)
        print(files_list)
        result_list = []
        for file in files_list:
            if ".dot" == file[-4:]:
                result_list.append(file[:-4])
        return result_list

    def produce(self, graph_listbox, production_listbox):
        g_name = self.graph_paths[graph_listbox.curselection()[0]]
        p_name = self.productions_paths[production_listbox.curselection()[0]]
        produce(g_name, p_name)
        self.results_graph_paths = self.find_paths(self.final_graph_dir)
        self.graph_paths = self.start_graph_paths + self.results_graph_paths
        self.graph_scrollbar.destroy()
        self.graph_listbox.destroy()
        self.graph_listbox_frame.destroy()
        self.graph_next.forget()
        self.graph_previous.forget()
        self.graph_listbox, self.graph_scrollbar, self.graph_listbox_frame = self.pack_listbox(self.menu_graph_frame, self.graph_paths)
        self.graph_next.pack()
        self.graph_previous.pack()

root = tk.Tk()
app = Window(root)
root.wm_title(" Transformacje i algorytmy grafowe")
root.mainloop()