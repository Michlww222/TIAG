from Graph import Graph_Transformation
import pydot
from graphviz import Graph

def read_Graph(name,path):
    graph = pydot.graph_from_dot_file(path)[0]
    graph_g = Graph(name)

    for node in graph.get_nodes():
        graph_g.node(node.get_name(), node.get('label'))

    for edge in graph.get_edges():
        graph_g.edge(edge.get_source(), edge.get_destination())

    return graph_g
  
def graph_to_graph_transformation(name,graph_g):
    graph_t = Graph_Transformation(name)
    graph_t.body = graph_g.body
    return graph_t