class Node:
    def __init__(self,value):
        self.value = value
class Graph:
    def __init__(self):
        self.total_v = 0
        self.nodes=[]
        self.edges=[]

    def addNode(self,value):
        self.total_v+=1
        v = Node(value)
        self.nodes.append(v)
        self.edges.append([])
        
    def addEdge(self,src,dest):
        node1_index = self.find_index(src)
        node2_index = self.find_index(dest)
        
        self.edges[node1_index].append(dest)
        self.edges[node2_index].append(src)
                
    def delNode(self,value):
        self.total_v-=1
        node_index = self.find_index(value)
        self.nodes.pop(node_index)
    def delEdge(self,src,dest):
        node1_index = self.find_index(src)
        node2_index = self.find_index(dest)
        for n in self.edges[node1_index]:
            if(n.value==dest.value):
                self.edges[node1_index].remove(n)
                break
        for n in self.edges[node2_index]:
            if(n.value==src.value):
                self.edges[node2_index].remove(n)
                break
    def adjList(self):
        print("Adjacency List\n")
        for i in range(self.total_v):
            print("Node: ", self.nodes[i].value, " -> ", end="")
            for n in self.edges[i]:
                print(n.value, end=" ")
            print()
             
    def find_index(self,node):
        for i in range(self.total_v):
            if(self.nodes[i].value==node.value):
                return i
        return self.total_v-1
                
    def BFS(self,start,end):
        queue=[]
        visited=[]
        bfs=[]
        queue.append(start)
        visited.append(start.value)
        while queue:
            n = queue.pop(0)
            bfs.append(n.value)
            if(n.value==end.value):
               return bfs
            i = self.find_index(n)
            for j in self.edges[i]:
                if(j.value not in visited):
                   queue.append(j)
                   visited.append(j.value)
        return bfs
    def DFS(self,start,end):
        stack=[]
        visited=[]
        dfs=[]
        stack.append(start)
        visited.append(start.value)
        while stack:
            n = stack.pop(-1)
            dfs.append(n.value)
            if(n.value==end.value):
               return dfs
            i = self.find_index(n)
            imt = []
            for j in self.edges[i]:
                if(j.value not in visited):
                    imt.append(j)
                    visited.append(j.value)
            imt2=imt[::-1]
            for i in imt2:
                stack.append(i)
        return dfs
g = Graph()
while(True):
    print("1.Add Node")
    print("2.Add Edge")
    print("3.Remove Node")
    print("4.Remove Edge")
    print("5.Adjacency List")
    print("6.BFS of Graph")
    print("7.DFS of Graph")
    print("7.Exit")
    print()
    n = int(input("Enter choice: "))
    if(n==1):
        node = input("Enter node: ")
        g.addNode(node)
    elif(n==2):
        node1 = input("Enter node 1: ")
        node2 = input("Enter node 2: ")
        g.addEdge(Node(node1),Node(node2))
    elif(n==3):
        node = input("Enter node: ")
        g.delNode(Node(node))
    elif(n==4):
        node1 = input("Enter node 1: ")
        node2 = input("Enter node 2: ")
        g.delEdge(Node(node1),Node(node2))
    elif(n==5):
        print("Adjacency List: ")
        g.adjList()
    elif(n==6):
        start = input("Enter starting node: ")
        end = input("Enter ending node: ")
        bfs = g.BFS(Node(start), Node(end))
        if(bfs[len(bfs)-1]!=end):
           print("Cannot construct BFS")
        print("\nBFS Traversal: ", bfs)
    elif(n==7):
        start = input("Enter starting node: ")
        end = input("Enter ending node: ")
        dfs = g.DFS(Node(start), Node(end))
        if(dfs[len(dfs)-1]!=end):
           print("Cannot construct DFS")
        print("\nDFS Traversal: ", dfs)
    else:
        break
