#from graphviz import Source

from graphviz import Source
from Graph import Graph_Transformation

def read_Graph(name,path):
    readedGraph = Source.from_file(path)
    newGraph =  Graph_Transformation(name,readedGraph)
    return newGraph



