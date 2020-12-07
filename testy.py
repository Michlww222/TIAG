# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:45:50 2020

@author: Michał Wąsik
READM ME PAWEŁ, PIOTREK -> NIE WIEM CZY TESTY NA PRODUCTION NIE DZIAŁAJĄ BO NIE DZIAŁA MI ZCZYTYWANIE CZEGOKOLWKIE Z PLIKU W PYTHONIE + NIE MA NAPISANEGO JESZCZE TESTU NA translate_graph 
"""

from Graph import *
import Graph
import unittest
import GraphData
import Production
import read_Graph

class GraphTest(unittest.TestCase):

    
        
    G1 = Graph_Transformation("G1")
    G1.node("1", label = "Y")
    G1.node("2", label = "X")
    G1.node("3", label = "a")
    G1.edge("1", "2")
    G1.edge("1", "3")
    
        
    G2 = Graph_Transformation("G2")
    G2.node("1", label = "Y")
    G2.node("2", label = "X")
    G2.node("3", label = "a")
    G2.edge("1", "2")
    
        
    G3 = Graph_Transformation("G3")
    G3.node("1", label = "Y")
    G3.node("2", label = "X")
    G3.node("3", label = "a")
    
        
    G4 = Graph_Transformation("G4")
    G4.node("1", label = "Y")
    G4.node("2", label = "X")
    G4.node("3", label = "a")
    G4.node("4", label = "a")
    G4.edge("1", "3")
    G4.edge("2", "4")
    
        
    G5 = Graph_Transformation("G5")
    
        
    G6 = Graph_Transformation("G6")
    G6.node("1", label = "Y")
    G6.node("2", label = "X")
    G6.node("3", label = "a")
    G6.node("4", label = "a")
    G6.edge("1", "2")
    G6.edge("1", "3")
    G6.edge("1", "4")
    G6.edge("2", "3")
    G6.edge("2", "4")
    G6.edge("3", "4")

    
    def test_node_or_edge(self):
        self.assertFalse(node_or_edge("\t10 -- 6"))
        self.assertTrue(node_or_edge("\t10 [label=Y]"))


    def test_find_nodes_with_label(self):
        
        nodes = self.G1.find_nodes_with_label('Y')
        self.assertEquals(len(nodes),1)
        self.assertEquals(nodes[0],'\t1 [label=Y]')
        nodes = self.G1.find_nodes_with_label('X')
        self.assertEquals(len(nodes),1)
        self.assertEquals(nodes[0],'\t2 [label=X]')
        nodes = self.G1.find_nodes_with_label('a')
        self.assertEquals(len(nodes),1)
        self.assertEquals(nodes[0],'\t3 [label=a]')
        
        nodes = self.G4.find_nodes_with_label('Y')
        self.assertEquals(len(nodes),1)
        self.assertEquals(nodes[0],'\t1 [label=Y]')
        nodes = self.G4.find_nodes_with_label('X')
        self.assertEquals(len(nodes),1)
        self.assertEquals(nodes[0],'\t2 [label=X]')
        nodes = self.G4.find_nodes_with_label('a')
        self.assertEquals(len(nodes),2)
        nodes.sort()
        self.assertEquals(nodes[0],'\t3 [label=a]')
        self.assertEquals(nodes[1],'\t4 [label=a]')
        
        nodes = self.G5.find_nodes_with_label('a')
        self.assertEquals(len(nodes),0) 


    def test_find_edges_to_node(self):
        
        edges = self.G1.find_edges_to_node("1")
        self.assertEquals(len(edges),2)
        edges = self.G1.find_edges_to_node("2")
        self.assertEquals(len(edges),1)
        edges = self.G1.find_edges_to_node("3")
        self.assertEquals(len(edges),1)

        edges = self.G2.find_edges_to_node("3")
        self.assertEquals(len(edges),0)

        edges = self.G3.find_edges_to_node("1")
        self.assertEquals(len(edges),0)

        edges = self.G4.find_edges_to_node("2")
        self.assertEquals(len(edges),1)

        edges = self.G6.find_edges_to_node("2")
        self.assertEquals(len(edges),3)


    def test_translate_graph(self):
        self.assertTrue(True) # nwm jak w to transform


    def test_find_labels(self):

        labels = self.G1.find_labels(["1","3"])
        self.assertEquals(len(labels),2)
        labels = self.G1.find_labels(["2","3"])
        self.assertEquals(len(labels),2)
        labels = self.G1.find_labels(["1"])
        self.assertEquals(len(labels),1)

        labels = self.G2.find_labels(["1","3"])
        self.assertEquals(len(labels),2)

        labels = self.G3.find_labels(["3","2"])
        self.assertEquals(len(labels),2)

        labels = self.G4.find_labels(["1","4"])
        self.assertEquals(len(labels),2)

        labels = self.G6.find_labels(["4","2"])
        self.assertEquals(len(labels),2)


    def test_find_nodes_and_edges(self):
        
        nodes,edges = self.G1.find_nodes_and_edges()
        self.assertEquals(len(nodes),3)
        self.assertEquals(len(edges),2)

        nodes,edges = self.G2.find_nodes_and_edges()
        self.assertEquals(len(nodes),3)
        self.assertEquals(len(edges),1)

        nodes,edges = self.G3.find_nodes_and_edges()
        self.assertEquals(len(nodes),3)
        self.assertEquals(len(edges),0)

        nodes,edges = self.G4.find_nodes_and_edges()
        self.assertEquals(len(nodes),4)
        self.assertEquals(len(edges),2)

        nodes,edges = self.G5.find_nodes_and_edges()
        self.assertEquals(len(nodes),0)
        self.assertEquals(len(edges),0)

        nodes,edges = self.G6.find_nodes_and_edges()
        self.assertEquals(len(nodes),4)
        self.assertEquals(len(edges),6)


    def test_get_label(self):
        
        self.assertEquals(get_label("\t10 [label=Y]"),"Y")
        self.assertEquals(get_label("\t999 [label=X]"),"X")
        self.assertEquals(get_label("\t0 [label=a]"),"a")
        self.assertEquals(get_label("\t54 [label=d]"),"d")


    def test_get_name(self):
        
        self.assertEquals(get_name("\t10 [label=Y]"),"10")
        self.assertEquals(get_name("\t999 [label=X]"),"999")
        self.assertEquals(get_name("\t0 [label=a]"),"0")
        self.assertEquals(get_name("\t54 [label=d]"),"54")


    def test_find_unique_names(self):
        
        new_names = find_unique_names([0,5,7,9],5)
        self.assertEquals(new_names[0],'1')
        self.assertEquals(new_names[1],'2')
        self.assertEquals(new_names[2],'3')
        self.assertEquals(new_names[3],'4')
        self.assertEqual(new_names[4],'6')
        
        new_names = find_unique_names([],2)
        self.assertEquals(new_names[0],'0')
        self.assertEquals(new_names[1],'1')
        
        new_names = find_unique_names([0,1,2,3,4,5],2)
        self.assertEquals(new_names[0],'6')
        self.assertEquals(new_names[1],'7')


    def test_get_names_from_edge(self):
        
        first,second = get_names_from_edge('\t10 -- 6')
        self.assertEquals(first,'10')
        self.assertEquals(second,'6')
        
        first,second = get_names_from_edge('\t100 -- 101')
        self.assertEquals(first,'100')
        self.assertEquals(second,'101')

        first,second = get_names_from_edge('\t0 -- 97')
        self.assertEquals(first,'0')
        self.assertEquals(second,'97')

        first,second = get_names_from_edge('\t0 -- 1')
        self.assertEquals(first,'0')
        self.assertEquals(second,'1')
    

class GraphDataTests(unittest.TestCase):
    
    G1 = Graph_Transformation("G1")
    G1.node("1", label = "Y")
    G1.node("2", label = "X")
    G1.node("3", label = "a")
    G1.edge("1", "2")
    G1.edge("1", "3")
        
    G2 = Graph_Transformation("G2")
    G2.node("1", label = "Y")
    G2.node("2", label = "X")
    G2.node("3", label = "a")
    G2.edge("1", "2")
       
    G3 = Graph_Transformation("G3")
    G3.node("1", label = "Y")
    G3.node("2", label = "X")
    G3.node("3", label = "a")
        
    G4 = Graph_Transformation("G4")
    G4.node("1", label = "Y")
    G4.node("2", label = "X")
    G4.node("3", label = "a")
    G4.node("4", label = "a")
    G4.edge("1", "3")
    G4.edge("2", "4")
       
    G5 = Graph_Transformation("G5")
       
    G6 = Graph_Transformation("G6")
    G6.node("1", label = "Y")
    G6.node("222", label = "X")
    G6.node("30", label = "a")
    G6.node("4", label = "a")
    G6.edge("1", "222")
    G6.edge("1", "30")
    G6.edge("1", "4")
    G6.edge("222", "30")
    G6.edge("222", "4")
    G6.edge("30", "4")

    data1 = GraphData.GraphData(G1)
    data2 = GraphData.GraphData(G2)
    data3 = GraphData.GraphData(G3)
    data4 = GraphData.GraphData(G4)
    data5 = GraphData.GraphData(G5)
    data6 = GraphData.GraphData(G6) #działa
    
    def test_number_of_nodes(self):
    
        nodes_number = self.data1.number_of_nodes()
        self.assertEqual(nodes_number,3)
        
        nodes_number = self.data2.number_of_nodes()
        self.assertEqual(nodes_number,3)

        nodes_number = self.data3.number_of_nodes()
        self.assertEqual(nodes_number,3)

        nodes_number = self.data4.number_of_nodes()
        self.assertEqual(nodes_number,4)

        nodes_number = self.data5.number_of_nodes()
        self.assertEqual(nodes_number,0)
        
        nodes_number = self.data6.number_of_nodes()
        self.assertEqual(nodes_number,4)


    def test_number_of_edges(self):
        
        edges_number = self.data1.number_of_edges()
        self.assertEqual(edges_number,2)
        
        edges_number = self.data2.number_of_edges()
        self.assertEqual(edges_number,1)

        edges_number = self.data3.number_of_edges()
        self.assertEqual(edges_number,0)

        edges_number = self.data4.number_of_edges()
        self.assertEqual(edges_number,2)

        edges_number = self.data5.number_of_edges()
        self.assertEqual(edges_number,0)
        
        edges_number = self.data6.number_of_edges()
        self.assertEqual(edges_number,6)


    def test_number_of_components(self):
        
        components_number = self.data1.number_of_components()
        self.assertEqual(components_number,1)
        
        components_number = self.data2.number_of_components()
        self.assertEqual(components_number,2)

        components_number = self.data3.number_of_components()
        self.assertEqual(components_number,3)

        components_number = self.data4.number_of_components()
        self.assertEqual(components_number,2)

        components_number = self.data5.number_of_components()
        self.assertEqual(components_number,0)
       
        components_number = self.data6.number_of_components()
        self.assertEqual(components_number,1)


    def test_average_of_nodes_degree(self):
        
        nodes_degree_average = self.data1.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,1.33)
        
        nodes_degree_average = self.data2.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,0.67)

        nodes_degree_average = self.data3.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,0)

        nodes_degree_average = self.data4.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,1)

        nodes_degree_average = self.data5.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,None)
        
        nodes_degree_average = self.data6.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,3)


    def test_average_ABCD_nodes_degree(self):
        
        ABCD_nodes_degree_average = self.data1.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.data2.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,0)

        ABCD_nodes_degree_average = self.data3.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,0)

        ABCD_nodes_degree_average = self.data4.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,1)

        ABCD_nodes_degree_average = self.data5.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,None)
        
        ABCD_nodes_degree_average = self.data6.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,3)


    def test_average_of_nodes_in_components(self):
               
        nodes_in_components_average = self.data1.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,3)

        nodes_in_components_average = self.data2.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,1.5)

        nodes_in_components_average = self.data3.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,1)

        nodes_in_components_average = self.data4.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,2)

        nodes_in_components_average = self.data5.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,None)
        
        nodes_in_components_average = self.data6.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,4)
        

class ProductionTest(unittest.TestCase):
    G1 = Graph_Transformation("G1")
    G1.node("1", label = "Y")
    G1.node("2", label = "X")
    G1.node("3", label = "a")
    G1.edge("1", "2")
    G1.edge("1", "3")
        
    G2 = Graph_Transformation("G2")
    G2.node("1", label = "Y")
    G2.node("2", label = "X")
    G2.node("3", label = "a")
    G2.edge("1", "2")
       
    G3 = Graph_Transformation("G3")
    G3.node("1", label = "Y")
    G3.node("2", label = "X")
    G3.node("3", label = "a")
        
    G4 = Graph_Transformation("G4")
    G4.node("1", label = "Y")
    G4.node("2", label = "X")
    G4.node("3", label = "a")
    G4.node("4", label = "a")
    G4.edge("1", "3")
    G4.edge("2", "4")
       
    G6 = Graph_Transformation("G6")
    G6.node("1", label = "Y")
    G6.node("2", label = "X")
    G6.node("3", label = "a")
    G6.node("4", label = "a")
    G6.edge("1", "2")
    G6.edge("1", "3")
    G6.edge("1", "4")
    G6.edge("2", "3")
    G6.edge("2", "4")
    G6.edge("3", "4")

    Production1 = read_Graph.read_Production('P1') # tutaj mi nie działa zczytywanie produkcji więc niech ktoś sprawdzi czy to wgl działa
    Production2 = read_Graph.read_Production('P2')
    Production3 = read_Graph.read_Production('P3')
    Production4 = read_Graph.read_Production('P4')

    newP1G1 = Production1.produce(G1,'newG1')
    newP1G2 = Production1.produce(G2,'newG2')
    newP1G3 = Production1.produce(G3,'newG3')
    newP1G4 = Production1.produce(G4,'newG4')
    newP1G6 = Production1.produce(G6,'newG6')
    dataP1G1 = GraphData.GraphData(newP1G1)
    dataP1G2 = GraphData.GraphData(newP1G2)
    dataP1G3 = GraphData.GraphData(newP1G3)
    dataP1G4 = GraphData.GraphData(newP1G4)
    dataP1G6 = GraphData.GraphData(newP1G6)

    newP2G1 = Production2.produce(G1,'newG1')
    newP2G2 = Production2.produce(G2,'newG2')
    newP2G3 = Production2.produce(G3,'newG3')
    newP2G4 = Production2.produce(G4,'newG4')
    newP2G6 = Production2.produce(G6,'newG6')
    dataP2G1 = GraphData.GraphData(newP2G1)
    dataP2G2 = GraphData.GraphData(newP2G2)
    dataP2G3 = GraphData.GraphData(newP2G3)
    dataP2G4 = GraphData.GraphData(newP2G4)
    dataP2G6 = GraphData.GraphData(newP2G6)

    newP3G1 = Production3.produce(G1,'newG1')
    newP3G2 = Production3.produce(G2,'newG2')
    newP3G3 = Production3.produce(G3,'newG3')
    newP3G4 = Production3.produce(G4,'newG4')
    newP3G6 = Production3.produce(G6,'newG6')
    dataP3G1 = GraphData.GraphData(newP3G1)
    dataP3G2 = GraphData.GraphData(newP3G2)
    dataP3G3 = GraphData.GraphData(newP3G3)
    dataP3G4 = GraphData.GraphData(newP3G4)
    dataP3G6 = GraphData.GraphData(newP3G6)

    newP4G1 = Production4.produce(G1,'newG1')
    newP4G2 = Production4.produce(G2,'newG2')
    newP4G3 = Production4.produce(G3,'newG3')
    newP4G4 = Production4.produce(G4,'newG4')
    newP4G6 = Production4.produce(G6,'newG6')
    dataP4G1 = GraphData.GraphData(newP4G1)
    dataP4G2 = GraphData.GraphData(newP4G2)
    dataP4G3 = GraphData.GraphData(newP4G3)
    dataP4G4 = GraphData.GraphData(newP4G4)
    dataP4G6 = GraphData.GraphData(newP4G6)



    def test_Production1(self):
        #nodes_number
        nodes_number = self.dataP1G1.number_of_nodes()
        self.assertEquals(nodes_number,5)
        
        nodes_number = self.dataP1G2.number_of_nodes()
        self.assertEquals(nodes_number,5)

        nodes_number = self.dataP1G3.number_of_nodes()
        self.assertEquals(nodes_number,5)

        nodes_number = self.dataP1G4.number_of_nodes()
        self.assertEquals(nodes_number,6)
        
        nodes_number = self.dataP1G6.number_of_nodes()
        self.assertEquals(nodes_number,6)
        #edges_number
        edges_number = self.dataP1G1.number_of_edges()
        self.assertEquals(edges_number,4)
        
        edges_number = self.dataP1G2.number_of_edges()
        self.assertEquals(edges_number,3)

        edges_number = self.dataP1G3.number_of_edges()
        self.assertEquals(edges_number,2)

        edges_number = self.dataP1G4.number_of_edges()
        self.assertEquals(edges_number,4)
        
        edges_number = self.dataP1G6.number_of_edges()
        self.assertEquals(edges_number,8)
        #components_number  
        components_number = self.dataP1G1.number_of_components()
        self.assertEquals(components_number,1)
        
        components_number = self.dataP1G2.number_of_components()
        self.assertEquals(components_number,2)

        components_number = self.dataP1G3.number_of_components()
        self.assertEquals(components_number,3)

        components_number = self.dataP1G4.number_of_components()
        self.assertEquals(components_number,2)
       
        components_number = self.dataP1G6.number_of_components()
        self.assertEquals(components_number,1)
        #nodes_degree_average
        nodes_degree_average = self.dataP1G1.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.6)
        
        nodes_degree_average = self.dataP1G2.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.2)

        nodes_degree_average = self.dataP1G3.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,0.8)

        nodes_degree_average = self.dataP1G4.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.33)

        nodes_degree_average = self.dataP1G6.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,2.67)
        #ABCD_nodes_degree_average
        ABCD_nodes_degree_average = self.dataP1G1.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.dataP1G2.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0.67)

        ABCD_nodes_degree_average = self.dataP1G3.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0.67)

        ABCD_nodes_degree_average = self.dataP1G4.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.dataP1G6.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,2)
        #nodes_in_components_average       
        nodes_in_components_average = self.dataP1G1.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,5)

        nodes_in_components_average = self.dataP1G2.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,2.5)

        nodes_in_components_average = self.dataP1G3.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,1.67)

        nodes_in_components_average = self.dataP1G4.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,3)
        
        nodes_in_components_average = self.dataP1G6.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,6)


    def test_Production2(self):

        nodes_number = self.dataP2G1.number_of_nodes()
        self.assertEquals(nodes_number,5)
        
        nodes_number = self.dataP2G2.number_of_nodes()
        self.assertEquals(nodes_number,5)

        nodes_number = self.dataP2G3.number_of_nodes()
        self.assertEquals(nodes_number,5)

        nodes_number = self.dataP2G4.number_of_nodes()
        self.assertEquals(nodes_number,6)
        
        nodes_number = self.dataP2G6.number_of_nodes()
        self.assertEquals(nodes_number,6)

        edges_number = self.dataP2G1.number_of_edges()
        self.assertEquals(edges_number,4)
        
        edges_number = self.dataP2G2.number_of_edges()
        self.assertEquals(edges_number,3)

        edges_number = self.dataP2G3.number_of_edges()
        self.assertEquals(edges_number,2)

        edges_number = self.dataP2G4.number_of_edges()
        self.assertEquals(edges_number,4)
        
        edges_number = self.dataP2G6.number_of_edges()
        self.assertEquals(edges_number,8)
           
        components_number = self.dataP2G1.number_of_components()
        self.assertEquals(components_number,1)
        
        components_number = self.dataP2G2.number_of_components()
        self.assertEquals(components_number,2)

        components_number = self.dataP2G3.number_of_components()
        self.assertEquals(components_number,3)

        components_number = self.dataP2G4.number_of_components()
        self.assertEquals(components_number,2)
       
        components_number = self.dataP2G6.number_of_components()
        self.assertEquals(components_number,1)
        
        nodes_degree_average = self.dataP2G1.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.6)
        
        nodes_degree_average = self.dataP2G2.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.2)

        nodes_degree_average = self.dataP2G3.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,0.6)

        nodes_degree_average = self.dataP2G4.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.33)
        
        nodes_degree_average = self.dataP2G6.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,2.67)
        
        ABCD_nodes_degree_average = self.dataP2G1.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.dataP2G2.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0.67)

        ABCD_nodes_degree_average = self.dataP2G3.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0.67)

        ABCD_nodes_degree_average = self.dataP2G4.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1.25)
        
        ABCD_nodes_degree_average = self.dataP2G6.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,3)
               
        nodes_in_components_average = self.dataP2G1.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,5)

        nodes_in_components_average = self.dataP2G2.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,2.5)

        nodes_in_components_average = self.dataP2G3.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,1.67)

        nodes_in_components_average = self.dataP2G4.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,3)
        
        nodes_in_components_average = self.dataP2G6.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,6)


    def test_Production3(self):

        nodes_number = self.dataP3G1.number_of_nodes()
        self.assertEquals(nodes_number,4)
        
        nodes_number = self.dataP3G2.number_of_nodes()
        self.assertEquals(nodes_number,4)

        nodes_number = self.dataP3G3.number_of_nodes()
        self.assertEquals(nodes_number,4)

        nodes_number = self.dataP3G4.number_of_nodes()
        self.assertEquals(nodes_number,5)
        
        nodes_number = self.dataP3G6.number_of_nodes()
        self.assertEquals(nodes_number,5)

        edges_number = self.dataP3G1.number_of_edges()
        self.assertEquals(edges_number,3)
        
        edges_number = self.dataP3G2.number_of_edges()
        self.assertEquals(edges_number,2)

        edges_number = self.dataP3G3.number_of_edges()
        self.assertEquals(edges_number,1)

        edges_number = self.dataP3G4.number_of_edges()
        self.assertEquals(edges_number,3)
        
        edges_number = self.dataP3G6.number_of_edges()
        self.assertEquals(edges_number,7)
           
        components_number = self.dataP3G1.number_of_components()
        self.assertEquals(components_number,1)
        
        components_number = self.dataP3G2.number_of_components()
        self.assertEquals(components_number,2)

        components_number = self.dataP3G3.number_of_components()
        self.assertEquals(components_number,3)

        components_number = self.dataP3G4.number_of_components()
        self.assertEquals(components_number,2)
       
        components_number = self.dataP3G6.number_of_components()
        self.assertEquals(components_number,1)
        
        nodes_degree_average = self.dataP3G1.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.5)
        
        nodes_degree_average = self.dataP3G2.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1)

        nodes_degree_average = self.dataP3G3.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,0.5)

        nodes_degree_average = self.dataP3G4.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.2)
        
        nodes_degree_average = self.dataP3G6.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,2.8)
        
        ABCD_nodes_degree_average = self.dataP3G1.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.dataP3G2.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0)

        ABCD_nodes_degree_average = self.dataP3G3.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0)

        ABCD_nodes_degree_average = self.dataP3G4.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.dataP3G6.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,3)
               
        nodes_in_components_average = self.dataP3G1.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,4)

        nodes_in_components_average = self.dataP3G2.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,2)

        nodes_in_components_average = self.dataP3G3.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,1.33)

        nodes_in_components_average = self.dataP3G4.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,2.5)
        
        nodes_in_components_average = self.dataP3G6.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,5)


    def test_Production4(self):

        nodes_number = self.dataP4G1.number_of_nodes()
        self.assertEquals(nodes_number,3)
        
        nodes_number = self.dataP4G2.number_of_nodes()
        self.assertEquals(nodes_number,3)

        nodes_number = self.dataP4G3.number_of_nodes()
        self.assertEquals(nodes_number,3)

        nodes_number = self.dataP4G4.number_of_nodes()
        self.assertEquals(nodes_number,4)
        
        nodes_number = self.dataP4G6.number_of_nodes()
        self.assertEquals(nodes_number,4)

        edges_number = self.dataP4G1.number_of_edges()
        self.assertEquals(edges_number,2)
        
        edges_number = self.dataP4G2.number_of_edges()
        self.assertEquals(edges_number,1)

        edges_number = self.dataP4G3.number_of_edges()
        self.assertEquals(edges_number,0)

        edges_number = self.dataP4G4.number_of_edges()
        self.assertEquals(edges_number,2)
        
        edges_number = self.dataP4G6.number_of_edges()
        self.assertEquals(edges_number,6)
           
        components_number = self.dataP4G1.number_of_components()
        self.assertEquals(components_number,1)
        
        components_number = self.dataP4G2.number_of_components()
        self.assertEquals(components_number,2)

        components_number = self.dataP4G3.number_of_components()
        self.assertEquals(components_number,3)

        components_number = self.dataP4G4.number_of_components()
        self.assertEquals(components_number,2)
       
        components_number = self.dataP4G6.number_of_components()
        self.assertEquals(components_number,1)
        
        nodes_degree_average = self.dataP4G1.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1.33)
        
        nodes_degree_average = self.dataP4G2.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,0.67)

        nodes_degree_average = self.dataP4G3.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,0)

        nodes_degree_average = self.dataP4G4.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,1)
        
        nodes_degree_average = self.dataP4G6.average_of_nodes_degree()
        self.assertEquals(nodes_degree_average,3)
        
        ABCD_nodes_degree_average = self.dataP4G1.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1.5)
        
        ABCD_nodes_degree_average = self.dataP4G2.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0.5)

        ABCD_nodes_degree_average = self.dataP4G3.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,0)

        ABCD_nodes_degree_average = self.dataP4G4.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,1)
        
        ABCD_nodes_degree_average = self.dataP4G6.average_ABCD_nodes_degree()
        self.assertEquals(ABCD_nodes_degree_average,3)
               
        nodes_in_components_average = self.dataP4G1.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,3)

        nodes_in_components_average = self.dataP4G2.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,1.5)

        nodes_in_components_average = self.dataP4G3.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,1)

        nodes_in_components_average = self.dataP4G4.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,2)
        
        nodes_in_components_average = self.dataP4G6.average_of_nodes_in_components()
        self.assertEquals(nodes_in_components_average,4)
    



if __name__ == '__main__':
    unittest.main()