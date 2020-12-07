# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:51:14 2020

@author: PaweŁ Świder (95%), Piotr Biały (5%)
"""

from Graph import Graph_Transformation, find_unique_names
from Graph import get_name, get_label, get_names_from_edge

class Production():
    """Class describing productions"""
    
    def __init__(self,L,R,T):
        """
        L - left side of the production graph
        R - right side of the production graph
        T - dictionary with embedding transformation
        T[label_in_old_graph] = label_in_new_graph
        """
        self.L = L
        self.R = R
        self.T = T
        
    def produce(self,G, name_G2):
        """
        Conduct a production over G graph
        G - graph
        name_G2 - name of the new graph created in the produce
        return - new graph which come to being after production
        """
        #L node data
        L_node = self.L.body[0]
        L_label = get_label(L_node)
        
        #L node data in G
        L_label_nodes_in_G = G.find_nodes_with_label(L_label)
        if len(L_label_nodes_in_G) > 0:
            L_node_in_G = L_label_nodes_in_G[0]
            L_node_in_G_name = get_name(L_node_in_G)

            #edges between G and L
            L_border_edges = G.find_edges_to_node(L_node_in_G_name)
            G_border_edges_names = [get_names_from_edge(edge) for 
                                            edge in L_border_edges]
            G_border_nodes_names = []
            for first, second in G_border_edges_names:
                if first == L_node_in_G_name:
                    G_border_nodes_names.append(second)
                else:
                    G_border_nodes_names.append(first)

            #getting rid of bad nodes names
            G_nodes, G_edges = G.find_nodes_and_edges()
            G_nodes.remove(L_node_in_G)
            G_edges = [edge for edge in G_edges if edge not in L_border_edges]
            names = [int(get_name(node)) for node in G_nodes]
            names.sort()

            # new graph with unproblematic name
            G2 = Graph_Transformation(name_G2)
            G2.body.extend(G_nodes)
            G2.body.extend(G_edges)

            #finds new name for R nodes
            R_nodes, _ = self.R.find_nodes_and_edges()
            R_new_names = find_unique_names(names,len(R_nodes))
            R_old_names = [get_name(element) for element in R_nodes]
            
            #create a translator
            translator = {old: new for old, new in zip(R_old_names,R_new_names)}

            #inserting R2 nodes into G2
            R2 = self.R.translate_graph(translator, "R2")
            G2.body.extend(R2.body)

            #inserting border edges after embedding transformation
            border_nodes_labels = G.find_labels(G_border_nodes_names)
            G2.body.extend(self.find_border_edges(
                    G_border_nodes_names,border_nodes_labels,R2))
            return G2
        else:
            #when there is not L subgraph in G return copy of G
            G2 = Graph_Transformation(name_G2)
            G2.body = G.body
            return G2
    
    def find_border_edges(self, border_nodes_names,border_nodes_labels, R):
        """
        Conduct embedding transformation in the border nodes
        border_nodes_noames - "hanging" nodes names
        border_nodes_labels - "hanging" nodes labels
        R - isomorhic graph to self.R - created with graph_translate
        return - list of embedded edges
        """
        result = []
        T2 = {}
        for key in self.T.keys():
            T2[key] = R.find_nodes_with_label(self.T[key])
        
        for name, label in zip (border_nodes_names,border_nodes_labels):
            for node in T2[label]:
                result.append("\t" + name + " -- " + get_name(node))
        return result