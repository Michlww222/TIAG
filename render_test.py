# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 20:26:20 2020

@author: spawe
"""
from Graph import Graph_Transformation

G1 = Graph_Transformation("test1")
G1.node("1", label = "Y")
G1.node("2", label = "X")
G1.node("3", label = "a")
G1.edge("1", "2")

G1.render(filename="results/test1", format="png")

G2 = Graph_Transformation("test2")
G2.node("1", label = "Y")
G2.node("2", label = "X")
G2.node("3", label = "a")
G2.node("4", label = "a")
G2.node("5", label = "a")
G2.edge("1", "2")
G2.edge("1", "3")
G2.edge("5", "4")

G2.render(filename="results/test2", format="png")

G3 = Graph_Transformation("test3")
G3.node("1", label = "Y")
G3.node("2", label = "X")
G3.node("3", label = "a")
G3.node("4", label = "a")
G3.edge("1", "2")
G2.edge("3", "4")

G3.render(filename="results/test3", format="png")
