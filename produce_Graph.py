# -*- coding: utf-8 -*-
"""
Created on Dec 04 2020

@author: Piotr Biały
"""

from Production import Production
from read_Graph import read_Graph, read_all_Productions


def get_name_of_start_graph():
    print("Enter start graph name")
    name = input()
    return name
# end def


def get_productions_sequence():
    print("Enter productions sequence, if you finish it, enter 'produce'")
    command = input()
    names = []
    while command != "produce":
        names.append(command)
        command = input()
    return names
# end def


def produce(graph_name, productions_names_sequence, save_all):
    g = read_Graph(graph_name)
    productions = read_all_Productions()
    for i, name in enumerate(productions_names_sequence):
        p = productions[name]
        g = p.produce(g, graph_name + str(i+1))
        if save_all:
            g.render(filename="results\dot\\" + graph_name + str(i+1) + ".dot")
            g.render(filename="results\png\\" + graph_name + str(i+1), format='png')
    if not save_all:
        g.render(filename="results\dot\\" + graph_name + "_end")
        g.render(filename="results\png\\" + graph_name + "_end", format='png')
# end def


g_name = get_name_of_start_graph()
p_names = get_productions_sequence()
produce(g_name, p_names, True)
