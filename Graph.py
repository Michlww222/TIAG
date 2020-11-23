# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 2020

@author: PaweŁ Świder
"""

from graphviz import Graph

class Graph_Transformation(Graph):
    """Klasa wykonująca produkcje na grafie"""
    
    def Graph_Transformation(self, name):
        """Inicjuje graf
        name - nazwa naszego grafu oraz pliku pdf w wygenerowanym grafem
        """
        super().__init__(name, filename=name)
            
    def HelloGraph(self):
        self.node("A");
        self.node("B");
        self.edge("A","B");
        self.view()
        
    def find_node_with_label(self,label):
        """Znajduje wierzchołek z o określonym parametrze label
        label - nazwa parametru label wierzchołka
        return - string zawierający informacje o wierzchołku
        DO USUNIĘCIA
        """
        for elem in self.body:
            if ' -- ' not in elem:
                if get_label(elem) == label:
                    return elem
        return None
    
    def find_nodes_with_label(self,label):
        """Znajduje wierzchołki z o określonym parametrze label
        label - nazwa parametru label wierzchołka
        return - lista wierzchołków o podanym paramentze label
        """
        nodes = []
        for elem in self.body:
            if ' -- ' not in elem:
                if get_label(elem) == label:
                    nodes.append(elem)
        print(nodes)
        return nodes
    
    def find_edges_to_node(self, name):
        """Znajduje listę krawędzi powiędzy wierzchołkami
        name - nazwa krawędzi
        raturn - lista krawędzi z wierzchołkiem name
        """
        list_of_edges = []
        for elem in self.body:
            if node_or_edge(elem) == False:
                if name in get_names_from_edge(elem):
                    list_of_edges.append(elem)
        return list_of_edges
    
    def translate_graph(self, translator, graph_name):
        """Generuje nowy graf izomorficzny
        translator - słownik zawierający gdzie klucz to stara wartosć a pole nowa
        translator[old_name] = new_name
        lista nowych nazw
        graph_name - nazwa nowego izomorficznego grafu
        return - graf izomorficzny G2
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
        """Znajduje wartosci label dla podanych nazw nodów
        nodes_names - lista nazw wierzchołków
        return - lista imion dla poszczególnych nodóW
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
            print(nodes_names)
            print(labels)
            raise ValueError("W tabeli label jest None")

        return labels
    
    def find_nodes_and_edges(self):
        """Zwraca listę wierzchołków i listę krawędzi
        return - (nodes, edges)
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
    """Sprawdza czy element jest wierzchołkiem czy grawędzią
    element - string reprezentujący linię tekstu w formacie dot
    return - true -> wierzchołek, false -> krawędź
    """
    return ' -- ' not in element
    
def get_label(node):
    """Zwraca wartość label dla danego wierzchołka
    node - wierzchołek zapisany w formacie dot
    Return: zawartość parametru label
    """
    start = node.find('label=') + 6
    end = node.find(']')
    return node[start:end]           

def get_name(node):
    """Zwraca unikalna nazwę wierzchołka
    node - wierzchołek zapisany w formacie dot
    Return: unikalna nazwa wierzchołka
    """
    last = node.find('[')
    return node[1:last-1]

def find_unique_names(names, n):
    """Znajduje odpowiednie nazwy dla wierzchołków
    names - posortowana tablica liczb zawierająca już używane nazwy
    n - ilosć nazw do znalezienia
    return - tablica string nazwierająca odpowiednia nazwy
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
    """Zwraca nazwy wierzchołków dla danej krawędzi
    edge - krawędź
    return - (a,b), gdzie a,b to nazwy wierzchołków połączonych krawędzią edge
    """
    first_end = edge.find(' -- ')
    first_start = 1
    first = edge[first_start:first_end]
    second_start = first_end + 4
    second_end = len(edge)
    second = edge[second_start:second_end]
    return first,second