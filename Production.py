# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:51:14 2020

@author: spawe
"""

from Graph import *

class Production():
    """Klasa opisująca produkcje"""
    
    def __init__(self,L,R,T):
        """
        L - graf lewej strony produkcji
        R - graf prawej strony produkcji
        T - transformacja osadzenia będąca słownikiem
        T[label_in_old_graph] = label_in_new_graph
        """
        self.L = L
        self.R = R
        self.T = T
        
    def produce(self,G, name_G2):
        """Przeprowadza produkcje na grafie G
        G - obiekt klasy Graph_Transformation
        name_G2 - nazwa nowego grafu
        return - obiekt G2 będący wynikiem przeprowadzenia produkcji na G
        """
        #dane wierzchołka L
        L_node = self.L.body[0]
        L_label = get_label(L_node)
        #dane wierzchołka w L grafie G 
        L_node_in_G = G.find_node_with_label(L_label)
        L_node_in_G_name = get_name(L_node_in_G)
        
        #krawędzie pomiędzy G i podgrafem L
        G_edges_to_L = G.find_edges_to_node(L_node_in_G_name)
        G_nodes_names_in_edges_to_L = [get_names_from_edge(edge) for edge in G_edges_to_L]
        G_nodes_to_L_names = []
        for first, second in G_nodes_names_in_edges_to_L:
            if first == L_node_in_G_name:
                G_nodes_to_L_names.append(second)
            else:
                G_nodes_to_L_names.append(first)
        
        #stworzenie nowego grafu, wstawienie do niego częsci nienależacych do L
        #napisanie nazw w grafie G2
        G2 = Graph_Transformation(name_G2)
        
        names = []
        for element in G.body:
            if element not in G_edges_to_L and element != L_node_in_G:
                G2.body.append(element)
                if node_or_edge(element) == True:
                    try:
                        names.append(int(get_name(element)))
                    except:
                        print("Błednie odczytanie nazwy")
        names.sort()
        
        R_nodes, _ = self.R.find_nodes_and_edges()
        #znajdujemy nowe nazwy dla grafu R 
        R_new_names = find_unique_names(names,len(R_nodes))
        R_old_names = [get_name(element) for element in R_nodes]
        #tworzymy translator
        translator = {old: new for old, new in zip(R_old_names,R_new_names)}
        
        #sprawiamy żeby graf R nie kolidował z grafem G2 i wstawiamy R2 w G2
        R2 = self.R.translate_graph(translator, "R2")
        G2.body.extend(R2.body)
        
        #znalezienie label dla krawędzi "zwisających"
        # author Piotr Biały

        G_nodes_to_L_labels = G.find_labels(G_nodes_to_L_names)
        G_nodes_to_L_names = [G_nodes_to_L_names[i] for i,label in enumerate(G_nodes_to_L_labels) if self.T[label] is not None]
        G_nodes_to_L_labels = [label for label in G_nodes_to_L_labels if self.T[label] is not None]
        R2_nodes_to_G_labels = [self.T[label] for label in G_nodes_to_L_labels]
        '''
        i = 0
        while i < len(G_nodes_to_L_labels):
            if self.T[G_nodes_to_L_labels[i]] == None:
                G_nodes_to_L_labels.pop(i)
                G_nodes_to_L_names.pop(i)
                i = i-1
            i = i+1

        R2_nodes_to_G_labels = [self.T[label] for label in G_nodes_to_L_labels]
        '''
        #znalezienie koncowych krawedzi transformacji osadzenia
        R2_nodes_names_to_G_nodes = [get_name(R2.find_node_with_label(label)) for label in R2_nodes_to_G_labels]
        
        for i in range(len(R2_nodes_names_to_G_nodes)):
            G2.edge(R2_nodes_names_to_G_nodes[i], G_nodes_to_L_names[i])
            
        return G2