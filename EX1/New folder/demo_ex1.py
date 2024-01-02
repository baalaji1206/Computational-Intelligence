class Graph:
    def __init__(self):
        self.length=0
        self.adj={}
        self.cost_matrix={}
    
    def add_node(self,value):
        if value in self.adj:
            print("Exist")
        else:
            self.adj[value]=[]
            self.length+=1
    
    def add_edge(self,node1,node2):
        if node1 not in self.adj:
            print("Node not present")
        elif node2 not in self.adj:
            print("Node not present")
        else:
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
    
    
    def print_adj_list(self):
        for key in self.adj.keys():
            print("Node", key, ":", self.adj[key]) 
        
    def cost_matrix(self):
        



        