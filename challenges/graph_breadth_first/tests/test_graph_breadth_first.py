from graph_breadth_first import __version__
from graph_breadth_first.graph_breadth_first import *

def test_version():
    assert __version__ == '0.1.0'
def test_breadth_first():
    graph = Graph()
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstroplolis = graph.add_node('Monstroplolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')   
    graph.add_edge(Pandora, Arendelle)
    graph.add_edge(Arendelle, Metroville)
    graph.add_edge(Arendelle, Monstroplolis)
    graph.add_edge(Metroville, Monstroplolis)
    graph.add_edge(Metroville, Narnia)
    graph.add_edge(Metroville, Naboo)
    graph.add_edge(Monstroplolis, Naboo)
  
    assert graph.breadth_first(Pandora)== ['Pandora', 'Arendelle', 'Metroville', 'Monstroplolis', 'Narnia', 'Naboo']