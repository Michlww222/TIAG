# -*- coding: utf-8 -*-
"""
Created on Dec 07 2020

@author: Piotr Biały
"""
import os
import pydot
from read_Graph import graph_to_graph_transformation, pydot_graph_to_graph


def render_graph(graph):
    graph.render(filename="grafy_startowe\\" + graph.name + ".dot")
    graph.render(filename="graph_photos\\" + graph.name, format='png')
    os.remove("graph_photos/" + graph.name)
    os.remove("grafy_startowe/" + graph.name + ".dot.pdf")


def add_to_file(filename, line):
    file = open(filename, "a")
    with file:
        file.write(line + "\n")
    file.close()


def render_production(l, r, name):

    filename = "productions\\" + name + ".dot"
    f = open(filename, "w+")
    f.close()
    add_to_file(filename, "# name: " + name)
    add_to_file(filename, "# --- #")
    f = open(filename, "a")
    with f:
        f.write(l.source)
        f.write("\n")
    f.close()
    add_to_file(filename, "# --- #")
    f = open(filename, "a")
    with f:
        f.write(r.source)
        f.write("\n")
    f.close()
    add_to_file(filename, "# --- #")


def read_grammar_file(filename):
    """
    reads a .dot file with the entire grammar and saves the graph and productions to the corresponding files
    :param filename: filename of grammar file
    """
    graph_p = pydot.graph_from_dot_file(filename)[0]
    graph = graph_to_graph_transformation(pydot_graph_to_graph(graph_p, graph_p.get_name()))
    render_graph(graph)
    productions_graphs = pydot.graph_from_dot_file(filename)[1:]
    for i, productions_graph in enumerate(productions_graphs):
        if (i % 2 == 0):
            l_prod = productions_graph
        else:
            r_prod = productions_graph
            l = graph_to_graph_transformation(pydot_graph_to_graph(l_prod,"HS_" + str(i//2 + 1)))
            r = graph_to_graph_transformation(pydot_graph_to_graph(r_prod, "HS_" + str(i//2 + 1)))
            render_production(l, r, "HS_" + str(i//2  +1 ))


read_grammar_file("gramatyka.dot")