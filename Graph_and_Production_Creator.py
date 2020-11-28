# -*- coding: utf-8 -*-
"""
Created on Tue Nov 27  2020

@author: Piotr Biały
"""


from graphviz import Graph


class Graph_Creaotr():

    def __init__(self, filename=None, name=None):
        if name is None:
            self.graph = Graph(name=self.create_name())
        else:
            self.graph = Graph(name=name)
        if filename is None:
            self.filename = "graphs\\" + self.graph.name + ".dot"
        else:
            self.filename = filename
        self.create_nodes()
        self.create_edges()
        self.finish_creating(self.filename)

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

    def finish_creating(self, filename):
        print("Your graph will be in file '" + filename + "'")
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
        Graph_Creaotr(filename=self.filename, name=self.name + "Left")
        self.add_to_file("# --- #")
        print("Now you creating right site production graph")
        Graph_Creaotr(filename=self.filename, name=self.name + "Right")
        self.add_to_file("# --- #")
        self.create_embed_transformation()

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
