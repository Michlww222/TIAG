# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:55:15 2020

@author: Piotr Biały
"""
from graphviz import Graph


class Graph_Creator():

    @staticmethod
    def hello_graph_creator():
        hello = open("grafy_startowe\graph_creator_instruction.txt", "r")
        print(hello.read())

    def init_parse(self):
        while True:
            command = input()
            if command == "exit":
                self.program_finished = True
                return None
            else:
                return command

    def __init__(self):
        self.program_finished = False
        self.name = self.init_parse()
        self.graph = Graph(self.name)

    def create_parse(self):
        caution = "Illegal phrase here, try \n node/edge <arg1> <arg2>\nor\nend"
        result = []
        while True:
            command = input()
            l = command.split()
            if l[0] == "end":
                return result
            if len(l) == 3:
                if l[0] == "node":
                    result = [True, l[1], l[2]]
                elif l[1] == "edge":
                    result = [False, l[1], l[2]]
                else:
                    print(caution)
            else:
                print(caution)

    def create(self):
        operation = self.create_parse()
        while len(operation) > 0:
            if operation[0]:
                self.graph.node(operation[1], operation[2])
            else:
                self.graph.edge(operation[1], operation[2])
            operation = self.create_parse()

        self.graph.render(filename="grafy_startowe\\" + self.name + ".dot")
# end def


Graph_Creator.hello_graph_creator()
creator = Graph_Creator()
while not creator.program_finished:
    creator.create()
    creator = Graph_Creator()
