from graph import __version__
from graph.graph import *

def test_version():
    assert __version__ == '0.1.0'

def test_adding_node():
    graph = Graph()
    a = graph.add_node('a')
    assert a.value=='a' 


def test_adding_edge():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    assert graph.add_edge(a,b)!='you could not add to not exist vertix' 

def test_retriving_all_node():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')
    assert graph.get_nodes()==['a','b','c','d','e','f'] 


def test_size():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
  
    assert graph.size()== 3


def test_retriving_all_node_e():
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    graph.add_edge(a,b)
    graph.add_edge(a,c)
  
    assert graph.get_neighbors(a)== {'b': 0, 'c': 0}

def test_empty_graph():
    graph = Graph()
    graph.get_nodes()
  
    assert graph.get_nodes()== None


def test_depth_first():
    graph = Graph()
    A = graph.add_node('A')
    B = graph.add_node('B')
    C = graph.add_node('C')
    G = graph.add_node('G')
    D = graph.add_node('D')
    F = graph.add_node('F')   
    H = graph.add_node('H')   
    E = graph.add_node('E')   
  
    graph.add_edge(A, D,150)
    graph.add_edge(A, B,82)   
    graph.add_edge(B, C,42)
    graph.add_edge(C, G,105)
    graph.add_edge(D, F,26)
    graph.add_edge(D, H,105)
    graph.add_edge(D, E,99)
    graph.add_edge(F, H,73)
    assert graph.depth_first(A)==['A', 'B', 'C', 'G', 'D', 'E', 'H', 'F']




