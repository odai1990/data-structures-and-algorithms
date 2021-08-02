from graph_breadth_first.graph_breadth_first import *
from graph_breadth_first.vertix import *
from graph_breadth_first.edge import *
from graph_breadth_first.queue import Queue
# from graph.graph import *
# from graph.vertix import *
# from graph.edge import *
# from graph.queue import Queue


class Graph:    
    def __init__(self):
        self.adjacency_list = {}
    
    def add_node(self, value):
        v = Vertix(value)
        self.adjacency_list[v] = []
        return v
    
    def add_edge(self, start_node, end_node, weight=0):
   
        if start_node and  end_node in self.adjacency_list.keys():           
            edge = Edge(end_node, weight)
            self.adjacency_list[start_node].append(edge)
        else:            
            return 'you could not add to not exist vertix'
    
    def get_nodes(self):
        if not self.adjacency_list:
            return None
        output=[]
        for vertix in self.adjacency_list.keys():
            output.append(vertix.value)
        return output
    
    def get_neighbors(self, node):
        output={}
        for edge in self.adjacency_list[node]:
            # output.append(edge.vertix.value )
            output[edge.vertix.value]=edge.weight
        return output
    
    def size(self):
        return len(self.adjacency_list.keys())

    def __str__(self):
        output = ''
        for vertix in self.adjacency_list.keys():          
            output += vertix.value           
            for edge in self.adjacency_list[vertix]:
                output += ' -> ' + edge.vertix.value             
            output += '\n'
        return output

    def breadth_first(self, start_node):
            visited = [] 
            queue = Queue() 
            queue.enqueue(start_node) 
            visited.append(start_node.value)
            while queue.front: 
                node = queue.dequeue() 
                for n in self.adjacency_list[node]: 
                    if n.vertix.value not in visited:                         
                        queue.enqueue(n.vertix)                        
                        visited.append(n.vertix.value)
            return visited

    


if __name__ == '__main__':
    
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

  
    print(graph.breadth_first(Pandora))
   