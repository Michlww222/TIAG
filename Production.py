# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:51:14 2020

@author: spawe
"""

from Graph import Graph_Transformation, find_unique_names
from Graph import get_name, get_label, get_names_from_edge

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
        L_node_in_G = G.find_nodes_with_label(L_label)[0]
        L_node_in_G_name = get_name(L_node_in_G)
        
        #krawędzie pomiędzy G i podgrafem L
        L_border_edges = G.find_edges_to_node(L_node_in_G_name)
        G_border_edges_names = [get_names_from_edge(edge) for edge in L_border_edges]
        G_border_nodes_names = []
        for first, second in G_border_edges_names:
            if first == L_node_in_G_name:
                G_border_nodes_names.append(second)
            else:
                G_border_nodes_names.append(first)
        #stworzenie nowego grafu, wstawienie do niego częsci nienależacych do L
        #napisanie nazw w grafie G2
        G2 = Graph_Transformation(name_G2)
        
        G_nodes, G_edges = G.find_nodes_and_edges()
        G_nodes.remove(L_node_in_G)
        G_edges = [edge for edge in G_edges if edge not in L_border_edges]
        names = [int(get_name(node)) for node in G_nodes]
        names.sort()
        print(names)
        
        G2.body.extend(G_nodes)
        G2.body.extend(G_edges)
        
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
        #G2.body.extend(find_border_edges())
        border_nodes_labels = G.find_labels(G_border_nodes_names)
        print(self.find_border_edges(G_border_nodes_names,border_nodes_labels,R2))

        G2.body.extend(self.find_border_edges(G_border_nodes_names,border_nodes_labels,R2))
        return G2
    
    def find_border_edges(self, border_nodes_names,border_nodes_labels, R):
        """
        Zwraca listę zawierającą krawędzie powstałe w transformacji osadzenia
        border_nodes_noames - nazwy wierzchołków z "zwisającymi" krawędziami
        border_nodes_labels - label wierzchołków z "zwisającymi" krawędziami
        R - graf izomorficzny do prawej strony produckji za pomocą
        translate graph
        return - lista krawędzi powstałych w transformacji osadzenia
        """
        result = []
        T2 = {}
        for key in self.T.keys():
            T2[key] = R.find_nodes_with_label(self.T[key])
        
        for name, label in zip (border_nodes_names,border_nodes_labels):
            for node in T2[label]:
                result.append("\t" + name + " -- " + get_name(node))
        return result
        
        
        