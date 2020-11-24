# -*- coding: utf-8 -*-
"""
Created on Sun Nov 15 20:45:50 2020

@author: Paweł Świder
"""

from Graph import *
import unittest

class GraphTest(unittest.TestCase):

    def test_node_or_edge(self):
        self.assertFalse(node_or_edge("\t10 -- 6"))
        self.assertTrue(node_or_edge("\t10 [label=Y]"))


if __name__ == '__main__':
    unittest.main()