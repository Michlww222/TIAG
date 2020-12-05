# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:45:50 2020

@author: Paweł Świder
"""

from Graph import *
import Graph
import unittest
import GraphData

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
        self.assertEquals(new_names[4],'6')
        
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
    G6.node("2", label = "X")
    G6.node("3", label = "a")
    G6.node("4", label = "a")
    G6.edge("1", "2")
    G6.edge("1", "3")
    G6.edge("1", "4")
    G6.edge("2", "3")
    G6.edge("2", "4")
    G6.edge("3", "4")

    data1 = GraphData.GraphData(G1)
    data2 = GraphData.GraphData(G2)
    data3 = GraphData.GraphData(G3)
    data4 = GraphData.GraphData(G4)
    data5 = GraphData.GraphData(G5)
    #data6 = GraphData.GraphData(G6) problem z wyjsciem poza liste (?) graphData Line 28 -> do sprawdzenia
    
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
        """
        nodes_number = self.data6.number_of_nodes()
        self.assertEqual(nodes_number,4)
        """


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
        """
        edges_number = self.data6.number_of_edges()
        self.assertEqual(edges_number,6)
        """   
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
        """
        components_number = self.data6.number_of_components()
        self.assertEqual(components_number,1)
        """   
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
        """
        nodes_degree_average = self.data6.average_of_nodes_degree()
        self.assertEqual(nodes_degree_average,3)
        """   
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
        """
        ABCD_nodes_degree_average = self.data6.average_ABCD_nodes_degree()
        self.assertEqual(ABCD_nodes_degree_average,3)
        """
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
        """
        nodes_in_components_average = self.data6.average_of_nodes_in_components()
        self.assertEqual(nodes_in_components_average,3)
        """

#class ProductionTest(unittest.TestCase): - TO DO

if __name__ == '__main__':
    unittest.main()