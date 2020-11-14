# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 2020

@author: PaweŁ Świder
"""

print("Janusz")


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
        """
        for elem in self.body:
            if ' -- ' not in elem:
                if get_label(elem) == label:
                    return elem
        return None
    
    def find_edges_to_node(self, name):
        """Znajduje listę krawędzi powiędzy wierzchołkami
        name - nazwa krawędzi
        raturn - lista krawędzi z wierzchołkiem name
        """
        list_of_edges = []
        for elem in self.body:
            if node_or_edge(elem) == False and name in elem:
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
            print(new_name, label)
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
        print("Nody: ", nodes)
        print("Names: ", nodes_names)
        for node in nodes:
            try:
                node_position = nodes_names.index(get_name(node))
                labels[node_position] = get_label(node)
                print("Wierzchołek: ", get_label(node))
            except:
                print("Nie znaleziono")
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
        
        L_node = self.L.body[0]
        label = get_label(L_node)
        
        L_node_in_G = G.find_node_with_label(label)
        
        name_of_L_node = get_name(L_node_in_G)
        #znajdź graf lewej strony produkcji
        #znajdź wierzchołki pomiędzy podgrafem L a G-L
        edges_to_L = G.find_edges_to_node(name_of_L_node)
        
        #utwórz nowy graf G2
        G2 = Graph_Transformation(name_G2)
        
        #wstaw wierzchołki i krawędzie niebędące w poprzednich punktach
        names = []
        for element in G.body:
            if element not in edges_to_L and element != L_node_in_G:
                G2.body.append(element)
                if node_or_edge(element) == True:
                    try:
                        names.append(int(get_name(element)))
                    except:
                        print("Błednie odczytanie nazwy")
                        
        names.sort()
        print(names)
        R_nodes, R_edges = self.R.find_nodes_and_edges()
        
        R_new_names = find_unique_names(names,len(R_nodes))
        R_old_names = [get_name(element) for element in R_nodes]
        
        translator = {old: new for old, new in zip(R_old_names,R_new_names)}
        
        print(translator)
        R2 = self.R.translate_graph(translator, "R2")
        
        
        for element in R2.body:
            G2.body.append(element)
        
        nodes_in_edges_to_L = []
        for edge in edges_to_L:
            nodes_in_edges_to_L.append(get_names_from_edge(edge))
        
        embed_nodes_names = []
        for first, second in nodes_in_edges_to_L:
            if first == name_of_L_node:
                embed_nodes_names.append(second)
            else:
                embed_nodes_names.append(first)
        
        labels_of_embed_nodes = G.find_labels(embed_nodes_names)
        print("Wierzchołki do zaopiekowania się: ",labels_of_embed_nodes)
        labels_of_ends_of_embeded_nodes = [self.T[label] for label in labels_of_embed_nodes]
        print("Końcowe labele: ", labels_of_ends_of_embeded_nodes)
        
        R2_nodes_to_embed_edges = []
        for label in labels_of_ends_of_embeded_nodes:
            R2_nodes_to_embed_edges.append(get_name(R2.find_node_with_label(label)))
        
        for i in range(len(R2_nodes_to_embed_edges)):
            G2.edge(R2_nodes_to_embed_edges[i], embed_nodes_names[i])
        return G2

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
    first_end = edge.find(' -- ')
    first_start = 1
    first = edge[first_start:first_end]
    second_start = first_end + 4
    second_end = len(edge)
    second = edge[second_start:second_end]
    return first,second