# -*- coding: utf-8 -*-
"""
Created on Sat Nov 14 2020

@author: Paweł Świder
"""

import Graph

prod_1_right = Graph.Graph_Transformation('prod_1_right')
prod_1_right.node('1', label='Y')
prod_1_right.node('2', label='c')
prod_1_right.node('3', label='a')
prod_1_right.edge('2', '1')
prod_1_right.edge('1', '3')
prod_1_right.edge('3', '2')

print(prod_1_right.body)
#prod_1_right.view()

prod_1_left = Graph.Graph_Transformation('prod_1_left')

prod_1_left.node('1', label='Y')
transformation_1 = {'a':'Y','b':'c','c':'Y','d':'a','X':'c','Y':'Y',}
production_1 = Graph.Production(prod_1_left,prod_1_right, transformation_1)

G1 = production_1.produce(prod_1_right, "wynik")
G2 = production_1.produce(G1, "wynik")
G2.view()
