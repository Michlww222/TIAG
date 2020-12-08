# -*- coding: utf-8 -*-
"""
Created on Dec 04 2020

@author: Piotr Biały
"""

from Production import Production
from read_Graph import read_Graph, read_Production

import os


def find_filename(name):
    full_name = name + ".dot"
    names1 = os.listdir("grafy_startowe")
    if full_name in names1:
        return "grafy_startowe"
    else:
        names2 = os.listdir("results")
        if full_name in names2:
            return "results"
        else:
            return None
# end def


def produce(graph_name, production_name):
    graph_directory = find_filename(graph_name)
    graph = read_Graph(graph_directory, graph_name)
    production = read_Production(production_name)
    result_graph = production.produce(graph, graph_name+production_name)
    result_graph.render(filename=result_graph.name, directory="graph_photos",
                        format='png', cleanup = True)
    result_graph.render(filename=result_graph.name, directory="results", format='png')
    result_graph.render(filename=result_graph.name + ".dot", directory="results")
    os.replace("results/" + result_graph.name + ".png", "graph_photos/" + result_graph.name + ".png")
    os.remove("results/" + result_graph.name)
    os.remove("results/" + result_graph.name + ".dot.pdf")
    return result_graph
# end def
