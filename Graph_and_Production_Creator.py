# -*- coding: utf-8 -*-
"""
Created on Nov 27  2020

@author: Piotr Biały
"""
import pydot
from graphviz import Graph
from read_Graph import graph_to_graph_transformation, pydot_graph_to_graph
import os


class Graph_Creaotr():

    def __init__(self, filename=None, name=None, start_graph=True):
        if name is None:
            self.graph = Graph(name=self.create_name())
        else:
            self.graph = Graph(name=name)
        if filename is None:
            self.filename = "grafy_startowe\\" + self.graph.name + ".dot"
        else:
            self.filename = filename
        self.create_nodes()
        self.create_edges()
        self.finish_creating(self.filename, start_graph)

    def create_name(self):
        print("Enter the name of your new graph")
        name = input()
        return name

    def create_nodes(self):
        print("Now create all nodes in graph by entering 'name label'\nTo go to the next part of creating graph enter 'next")
        command = input().split()
        while command[0] != 'next':
            if len(command) == 2:
                self.graph.node(command[0], label=command[1])
            else:
                print("You enter too much arguments")
            command = input().split()

    def create_edges(self):
        print("Now create all edge in graph by entering 'head_node tail_node'\nTo finish creating graph enter 'next")
        command = input().split()
        while command[0] != 'next':
            if len(command) == 2:
                self.graph.edge(command[0], command[1])
            else:
                print("You enter too much arguments")
            command = input().split()

    def finish_creating(self, filename, graph_or_production):
        print("Your graph will be in file '" + filename + "'")
        if (graph_or_production):
            self.graph.render(filename="grafy_startowe\\" + self.graph.name + ".dot")
            self.graph.render(filename="graph_photos\\" + self.graph.name, format='png')
            os.remove("graph_photos/" + self.graph.name)
            os.remove("grafy_startowe/" + self.graph.name + ".dot.pdf")
        else:
            file = open(self.filename, "a")
            with file:
                file.write(self.graph.source)
                file.write("\n")
            file.close()
# end def


class Production_Creator():

    def __init__(self):
        self.name = self.create_name()
        self.filename = "productions\\" + self.name + ".dot"
        f = open(self.filename, "w+")
        f.close()
        self.add_to_file("# name: " + self.name)
        self.add_to_file("# --- #")
        print("Now you creating left site production graph")
        Graph_Creaotr(filename=self.filename, name=self.name + "Left", start_graph=False)
        self.add_to_file("# --- #")
        print("Now you creating right site production graph")
        Graph_Creaotr(filename=self.filename, name=self.name + "Right", start_graph=False)
        self.add_to_file("# --- #")
        self.create_embed_transformation()
        self.finish_creating()

    def create_name(self):
        print("Enter the name of your new production")
        name = input()
        return name

    def add_to_file(self, line):
        file = open(self.filename, "a")
        with file:
            file.write(line + "\n")
        file.close()

    def create_embed_transformation(self):
        print("Now create embed transformation by entering 'head_label tail_label'\nTo finish creating production enter 'next")
        file = open(self.filename, "a")
        command = input().split()
        with file:
            while command[0] != 'next':
                if len(command) == 2:
                    file.write("# embed_transformation " + command[0] + " " + command[1] + " \n")
                else:
                    print("You enter too much arguments")
                command = input().split()
        file.close()

    def finish_creating(self):
        left_p = pydot.graph_from_dot_file(self.filename)[0]
        right_p = pydot.graph_from_dot_file(self.filename)[1]
        l = graph_to_graph_transformation(pydot_graph_to_graph(left_p, self.name))
        r = graph_to_graph_transformation(pydot_graph_to_graph(right_p, self.name))
        l.render(filename="graph_photos\\" + l.name + "_left", format='png')
        r.render(filename="graph_photos\\" + r.name + "_right", format='png')
        os.remove("graph_photos/" + l.name + "_left")
        os.remove("graph_photos/" + r.name + "_right")
# end def


print("Hello in the Graph & Production Creator!")
while True:
    print("To create new graph, enter 'new graph'")
    print("To create new production, enter 'new production'")
    print("To escape the program, enter 'escape'")
    command = input()
    if command == "new graph":
        Graph_Creaotr()
    elif command == "new production":
        Production_Creator()
    elif command == "escape":
        break
    else:
        print("Illegal argument here, try again")
