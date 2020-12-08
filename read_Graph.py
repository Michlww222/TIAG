# -*- coding: utf-8 -*-
"""
Created on Nov 28 2020

@author: Piotr Biały
"""


from Graph import Graph_Transformation
import pydot
from graphviz import Graph
import os

from Production import Production


def graph_to_graph_transformation(graph_g):
    graph_t = Graph_Transformation(graph_g.name)
    graph_t.body = graph_g.body
    return graph_t
# end def


def pydot_graph_to_graph(graph_p, name):
    graph_g = Graph(name)

    for node in graph_p.get_nodes():
        graph_g.node(node.get_name(), node.get('label'))

    for edge in graph_p.get_edges():
        graph_g.edge(edge.get_source(), edge.get_destination())

    return graph_g


def read_Graph(directory, name):
    """
    Read a graph from 'graphs\name.dot'
    :param name: name of graph to read
    directory - directory
    :return: graph (class Graph_Transformation)
    """

    try:
        filename = directory + "\\" + name + ".dot"
        graph_p = pydot.graph_from_dot_file(filename)[0]
        graph_g =pydot_graph_to_graph(graph_p, name)

        return graph_to_graph_transformation(graph_g)
    except:
        return Graph_Transformation("empty")
# end def


def read_embed_transformation(filename):
    file = open(filename, "r")
    embed_t = {}
    with file:
        command = file.read().split()
    file.close()
    for i, str in enumerate(command):
        if str == "embed_transformation":
            if command[i+2] == "None":
                embed_t[command[i + 1]] = None
            else:
                embed_t[command[i+1]] = command[i+2]
    return embed_t
# end def


def get_production_name(filename):
    file = open(filename, "r")
    with file:
        name = file.readline().split()[2]
    file.close()
    return name
# end def


def read_Production(name):
    """
    Read a production from 'productions\name.dot'
    :param name: name of production to read
    :return: Production object
    """
    filename = "productions\\" + name + ".dot"
    left_p = pydot.graph_from_dot_file(filename)[0]
    right_p = pydot.graph_from_dot_file(filename)[1]
    l = graph_to_graph_transformation(pydot_graph_to_graph(left_p, name))
    r = graph_to_graph_transformation(pydot_graph_to_graph(right_p, name))
    e = read_embed_transformation(filename)
    return Production(l, r, e)
# end def


def read_all_Productions():
    """
    Read all productions from directory productions\
    :return: dictionary of all Productions, with key = name of production
    """
    P = {}
    productions = os.listdir("productions\\")
    for production_file in productions:
        name = get_production_name("productions\\" + production_file)
        P[name] = read_Production(name)

    return P
# end def
