# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 2020

@author: Piotr Biały

from Graph import Graph_Transformation
from Production import Production

prod_1_right = Graph_Transformation('prod_1_right')
prod_1_right.node('1', label='Y')
prod_1_right.node('2', label='c')
prod_1_right.node('3', label='a')
prod_1_right.edge('2', '1')
prod_1_right.edge('1', '3')
prod_1_right.edge('3', '2')

prod_1_left = Graph_Transformation('prod_1_left')

prod_1_left.node('1', label='Y')
transformation_1 = {'a': None,'b':'c','c':'Y','d':'a','X':'c','Y':'Y',}
production_1 = Production(prod_1_left,prod_1_right, transformation_1)

G1 = production_1.produce(prod_1_right, "wynik")
G2 = production_1.produce(G1, "wynik1")
G3 = production_1.produce(G2, "wynik2")
G4 = production_1.produce(G3, "wynik3")
G5 = production_1.produce(G4, "wynik5")
G5.view()
"""

from Production import Production
from read_Graph import *


def parse_args():
    command = input()
    args = command.split()
    # name of output graph is args[0]
    name = args[0]
    # path to input graph is args[1]
    path = args[1]
    # others args are names of productions
    production_names = args[2:,]

    production_paths = [["productions\Left_" + name + ".dot",
                         "productions\Right_" + name + ".dot"
                         "productions\EmbedT_" + name + ".txt"]
                        for name in range(len(production_names))]
    return name, path, production_paths
# end def


def get_graph(name, path):
    return graph_to_graph_transformation(name,read_Graph(name,path))
# end def


def embed_transformation(path):
    file = open(path, "r")
    embed_transformation = {}
    with file:
        embed_transformation.fromkeys(file.read(), file.read())
    file.close()
    return embed_transformation
# end def


def get_productions(production_paths):
    productions = [[None]*3 for _ in production_paths]
    for i, production in enumerate(production_paths):
        productions[i][0] = read_Graph(str(i)+"R", production[0])
        productions[i][1] = read_Graph(str(i)+"L", production[1])
        productions[i][2] = embed_transformation(production[2])
    return productions
# end def


name, g_path, p_paths = parse_args()
graph = get_graph(name, g_path)
prod_args = get_productions(p_paths)
for prod_arg in prod_args:
    production = Production(prod_arg[0], prod_arg[1], prod_arg[2])
    graph = production.produce(graph, "name")
graph.render(filename="results\\" +  name + ".dot")
