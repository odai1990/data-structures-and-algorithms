class Vertix:
    def __init__(self, value):
        self.value = value
 

class Edge:
    def __init__(self, vertix , weight):
        self.vertix = vertix
        self.weight = weight

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
        print(node)
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
