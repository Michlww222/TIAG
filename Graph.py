# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 2020

@author: PaweŁ Świder
"""

from graphviz import Graph

class Graph_Transformation(Graph):
    """Class extending Graph class from Graphviz"""
    
    def __init__(self, name):
        """
        Initiate a graph
        name - name of our graph
        """
        super().__init__(name, filename=name)
    
    def find_nodes_with_label(self,label):
        """
        Finds nodes with set label
        Label - label we use to find nodes with this label
        return - nodes with label
        """
        nodes = []
        for elem in self.body:
            if node_or_edge(elem):
                if get_label(elem) == label:
                    nodes.append(elem)
        return nodes
    
    def find_edges_to_node(self, name):
        """
        Finds edges which has one common node
        name - name of node
        return - list of edges containing node with name
        """
        list_of_edges = []
        for elem in self.body:
            if node_or_edge(elem) == False:
                if name in get_names_from_edge(elem):
                    list_of_edges.append(elem)
        return list_of_edges
    
    def translate_graph(self, translator, graph_name):
        """
        Create a new isomorphic graph
        translator - dictionary used as translator
        translator[old_name] = new_name
        graph_name - name of new isomorphic graph
        return - new isomorphic graph
        """
        G2 = Graph_Transformation(graph_name)
        nodes, edges = self.find_nodes_and_edges()
        
        for node in nodes:
            label = get_label(node)
            name = get_name(node)
            new_name = translator[name]
            G2.node(new_name, label=label)
            
        for edge in edges:
            first_name, second_name = get_names_from_edge(edge)
            new_first_name = translator[first_name]
            new_second_name = translator[second_name]
            G2.edge(new_first_name, new_second_name)
        
        return G2
    
    def find_labels(self,nodes_names):
        """
        Finds labes to list of nodes names in graph
        nodes_names - lista of nodes names
        return - list of labels 
        nodes_names[i] - labels[i] -- name and label of the same node
        """
        nodes, _ = self.find_nodes_and_edges()
        labels = [None]*len(nodes_names)
        for node in nodes:
            try:
                node_position = nodes_names.index(get_name(node))
                labels[node_position] = get_label(node)
            except:
                None
        if None in labels:
            raise ValueError("W tabeli label jest None")
        return labels
    
    def find_nodes_and_edges(self):
        """
        Finds graph nodes and edges
        return - (nodes, edges) - nodes and edges are lists
        """
        nodes = []
        edges = []
        for element in self.body:
            if node_or_edge(element) == True:
                nodes.append(element)
            else:
                edges.append(element)
        return nodes,edges
    
def node_or_edge(element):
    """
    Check if the graph element is node or edge
    element - graph element we want to check
    return - True -> node, False -> edge
    """
    return ' -- ' not in element
    
def get_label(node):
    """
    Get label of the node
    node - graphviz node -- "1 [label=Y]
    return - node label
    """
    start = node.find('label=') + 6
    end = node.find(']')
    return node[start:end]           

def get_name(node):
    """
    Get name of the node
    node - graphviz node -- "1 [label=Y]
    return - node name
    """
    last = node.find('[')
    return node[1:last-1]

def find_unique_names(names, n):
    """
    Finds proper names for the nodes
    names - sorted list of forbidden names
    n - amount of the names we want to find
    return - list of string with proper nodes names for new nodes
    """
    i = 0
    j = 0
    new_names = []
    while (len(new_names)<n):
        if j < len(names):
            if i == names[j]:
                i = i+1
                j = j+1
            elif i < names[j]:
                new_names.append(str(i))
                i = i+1
        else:
            new_names.append(str(i))
            i = i+1
    return new_names
    
def get_names_from_edge(edge):
    """
    Get nodes names from the edge
    edge - edge
    return - tuple (a,b), a and b are nodes names
    """
    first_end = edge.find(' -- ')
    first_start = 1
    first = edge[first_start:first_end]
    second_start = first_end + 4
    second_end = len(edge)
    second = edge[second_start:second_end]
    return first,second