from graph_business_trip import __version__
from graph_business_trip.graph_business_trip import business_trip
from graph_business_trip.graph import Graph
import pytest
def test_version():
    assert __version__ == '0.1.0'


def test_happy_path(adding):
    assert business_trip(adding,['Metroville', 'Pandora'])==[True, '$82']
    
def test_expected_failure(adding):
    assert business_trip(adding,['Narnia', 'Arendelle', 'Naboo'])==[False, '$0']

def test_edge_case(adding):
    assert business_trip(adding,['Narnia', 'Naboo', 'Arendelle'])==[False, '$0']

@pytest.fixture
def adding():
    graph = Graph()
    Pandora = graph.add_node('Pandora')
    Arendelle = graph.add_node('Arendelle')
    Metroville = graph.add_node('Metroville')
    Monstroplolis = graph.add_node('Monstroplolis')
    Narnia = graph.add_node('Narnia')
    Naboo = graph.add_node('Naboo')   
    graph.add_edge(Pandora, Arendelle,150)
    graph.add_edge(Pandora, Metroville,82)

    graph.add_edge(Arendelle, Pandora,150)
    graph.add_edge(Arendelle, Metroville,99)
    graph.add_edge(Arendelle, Monstroplolis,42)

    graph.add_edge(Metroville, Pandora,82)
    graph.add_edge(Metroville, Arendelle,99)
    graph.add_edge(Metroville, Monstroplolis,105)
    graph.add_edge(Metroville, Naboo,26)
    graph.add_edge(Metroville, Narnia,37)

    graph.add_edge(Monstroplolis, Arendelle,42)
    graph.add_edge(Monstroplolis, Metroville,105)
    graph.add_edge(Monstroplolis, Naboo,73)

    graph.add_edge(Naboo, Monstroplolis,73)
    graph.add_edge(Naboo, Metroville,26)
    graph.add_edge(Naboo, Narnia,250)

    graph.add_edge(Narnia, Naboo,250)
    graph.add_edge(Narnia, Metroville,37)
    return graph