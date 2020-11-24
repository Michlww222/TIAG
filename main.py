# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 2020

@author: Piotr Biały
"""

from Production import Production
from read_Graph import *
import pydot


def hello_main():
    hello = open("main_instruction.txt", "r")
    print(hello.read())


def get_name():
    name = input()
# end def


def graph_path():
    while True:
        path = input()
        try:
            _ = pydot.graph_from_dot_file(path)[0]
            return path
        except IOError:
            print("Nie znaleziono pliku")
            continue
# end def


def production_paths():
    command = input()
    production_names = command.split()
    production_paths = [["productions\Left_" + name + ".dot",
                         "productions\Right_" + name + ".dot",
                         "productions\EmbedT_" + name + ".txt"]
                        for name in range(len(production_names))]
    return production_paths
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


hello_main()
name = get_name()
g_path = graph_path()
p_paths = production_paths()
graph = get_graph(name, g_path)
prod_args = get_productions(p_paths)
for prod_arg in prod_args:
    production = Production(prod_arg[0], prod_arg[1], prod_arg[2])
    graph = production.produce(graph, "name")
graph.view()
graph.render(filename="results\\" +  name + ".dot")
