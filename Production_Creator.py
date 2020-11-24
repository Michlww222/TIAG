# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 13:55:15 2020

@author: Piotr Biały
"""
from graphviz import Graph


class Production_Creator():

    @staticmethod
    def hello_production_creator():
        hello = open("productions\production_creator_instruction.txt", "r")
        print(hello.read())

    def init_parse(self):
        while True:
            command = input()
            l = command.split()
            if l[0] == "new_production":
                if len(l) > 1 :
                    return l[1]
                else:
                    print("You forget about name of your new production")
            elif l[0] == 'exit':
                self.program_finished = True
                return "_"
            else:
                print("Illegal phrase here, try \nnew production <name> \nor\nexit")

    def __init__(self):
        self.program_finished = False
        self.name = self.init_parse()
        self.left_production_graph = Graph(name="Left" + self.name)
        self.right_production_graph = Graph(name="Right" + self.name)
        self.transformation = []

    def create_parse(self):
        caution = "Illegal phrase here, try \nright/left node/edge <arg1> <arg2> \nor\nembed_transformation <arg1> <arg2>\nor\nend"
        result = []
        while True:
            command = input()
            l = command.split()
            if l[0] == "end":
                return result
            if len(l) == 4:
                if l[0] == "right":
                    result.append(True)
                elif l[0] == "left":
                    result.append(False)
                else:
                    print(caution)
                    continue
                if l[1] == "node":
                    result.append(True)
                elif l[1] == "edge":
                    result.append(False)
                else:
                    print(caution)
                    continue
                result.append(l[2])
                result.append(l[3])
                return result
            if len(l) == 3:
                if l[0] == "embed_transformation":
                    result.append(l[1])
                    result.append(l[2])
                    return result
                else:
                    print(caution)
                    continue
            else:
                print(caution)

    def create(self):
        operation = self.create_parse()
        while len(operation) > 0:
            if len(operation) == 4:
                if operation[0]:
                    if operation[1]:
                        self.right_production_graph.node(operation[2], operation[3])
                    else:
                        self.right_production_graph.edge(operation[2], operation[3])
                else:
                    if operation[1]:
                        self.left_production_graph.node(operation[2], operation[3])
                    else:
                        self.left_production_graph.edge(operation[2], operation[3])
                operation = self.create_parse()
            else:
                self.transformation.append(operation)
                operation = self.create_parse()
        self.right_production_graph.render(filename="productions\Right_" + self.name + ".dot")
        self.left_production_graph.render(filename="productions\Left_" + self.name + ".dot")
        embed_t = open("productions\EmbedT_" + self.name + ".txt", "w+")
        with embed_t:
            for item in self.transformation:
                embed_t.write(item[0] + " ")
                embed_t.write(item[1] + " ")
        embed_t.close()
# end def


Production_Creator.hello_production_creator()
creator = Production_Creator()
while not creator.program_finished:
    creator.create()
    creator = Production_Creator()
