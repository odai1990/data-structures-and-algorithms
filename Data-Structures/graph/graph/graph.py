from graph.graph import *
from graph.vertix import *
from graph.edge import *
from graph.stack import *


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


    def depth_first(self, start_node):
          stack = Stack()
          stack.push(start_node)
          visited =[]
          while not stack.is_empty():
            vertex = stack.pop()
            if vertex.value in visited:
                continue
          
            visited.append(vertex.value)
            for neighbor in self.adjacency_list[vertex]:
                stack.push(neighbor.vertix)
          return visited


if __name__ == '__main__':
    graph = Graph()
    a = graph.add_node('a')
    b = graph.add_node('b')
    c = graph.add_node('c')
    d = graph.add_node('d')
    e = graph.add_node('e')
    f = graph.add_node('f')   
    graph.add_edge(a, c)
    graph.add_edge(a, d)
    # graph.add_edge(b, c)
    # graph.add_edge(b, f)
    # graph.add_edge(c, a)
    # graph.add_edge(c, b)
    # graph.add_edge(c, e)
    # graph.add_edge(d, a)
    # graph.add_edge(d, e)
    # graph.add_edge(e, c)
    # graph.add_edge(e, d)
    # graph.add_edge(e, f)
    # graph.add_edge(f, b)
    # graph.add_edge(f, e)
    # print(graph)
    print(graph.size())
   