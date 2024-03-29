class Graph:
    def __init__(self):
        self.length = 0
        self.adj = {}
        self.cost_matrix={}
        
    def add_node(self, value):  
        if value in self.adj:
            print(value, "Already exists")
        else:
            self.adj[value] = []
            self.length += 1
           
    def add_edge(self, node1, node2):  
        if node1 not in self.adj:
            print(node1, "Not in graph")
        elif node2 not in self.adj:
            print(node2, "Not in graph")
        else:            
            self.adj[node1].append(node2)
            self.adj[node2].append(node1)
            
    def del_node(self, value):
        if value in self.adj:
            del self.adj[value]
            for key in self.adj.keys():
                if value in self.adj[key]:
                    self.adj[key].remove(value)
        else:
            print(value, "Not in graph")
                    
    def del_edge(self, node1, node2):
    
        if node1 not in self.adj:
            print(node1, "Not in graph")
        elif node2 not in self.adj:
            print(node2, "Not in graph")
        else:
            self.adj[node1].remove(node2)
            self.adj[node2].remove(node1)
            
    def print_adj_list(self):
        for key in self.adj.keys():
            print("Node", key, ":", self.adj[key])
            
    def costMatrix(self):
        
        for key in self.adj.keys():
            for i in self.adj[key]:
                print("Enter cost for "+key+" - "+i)
                self.cost_matrix.setdefault(key,{})[i] = int(input()) 
                
        print("Cost Matrix is")
        for key in self.adj.keys():
            print("Node", key, ":", self.cost_matrix[key])

    def bfs(self, start, search):
        print("\nRESULT : ")
        visited = []
        queue = []
        res = []
        visited.append(start)
        queue.append(start)
        while queue:
            m = queue.pop(0)
            res.append(m)
            if m == search:
                for i in res:
                    print(i, end=" ")
                return True
            for neighbour in self.adj[m]:
                if neighbour[0] not in visited:
                    visited.append(neighbour[0])
                    queue.append(neighbour[0])
        return False

    def dfs(self, start, search):
        print("\nRESULT : ")
        visited = []
        stack = []
        res = []
        visited.append(start)
        stack.append(start)
        while stack:
            last = len(stack)-1
            m = stack.pop(last)
            res.append(m)
            if m == search:
                for i in res:
                    print(i, end=" ")
                return True
            for j in range(len(self.adj[m])-1,-1,-1):
                if(self.adj[m][j] not in visited):
                    visited.append(self.adj[m][j])
                    stack.append(self.adj[m][j])
        return False
        
    def ucs(self,source,goal):
        self.costMatrix()
        
        visited = set()
        queue = [(0, source, [])]
        
        while queue:
            cost, current_node, path = queue.pop(0)
            if current_node == goal:
                print("Path:", path + [current_node])
                print("Cost:", cost)
                return
            if current_node in visited:
                continue
            visited.add(current_node)
            for neighbour in self.adj[current_node]:
                new_cost = cost + self.cost_matrix[current_node][neighbour]
                new_path = path + [current_node]
                queue.append((new_cost, neighbour, new_path))
            queue.sort(key=lambda x: x[0])
      
def main():    
  g = Graph()
  choice = 0
  while choice <= 8:
    print("\n1. Add Node\n2. Add Edge\n3. Delete Node\n4. Delete Edge\n5. Print Adj List\n6. BFS\n7. UCS\n8. DFS\n")
    choice = int(input("\nEnter Choice:"))
    if choice == 1:
        node = input("Enter Node:")
        g.add_node(node)
    elif choice == 2:
        edge1 = input("Enter Node1:")
        edge2 = input("Enter Node2:")
        g.add_edge(edge1, edge2)
    elif choice == 3:
        node = input("Enter Node:")
        g.del_node(node)
    elif choice == 4:
        edge1 = input("Enter Node1:")
        edge2 = input("Enter Node2:")
        g.del_edge(edge1, edge2)
    elif choice == 5:
        g.print_adj_list()
    elif choice == 6:
        print("BFS")
        start = input("Enter Start:")
        goal = input("Enter Goal:")
        g.bfs(start, goal)
    elif choice == 7:
        start = input("Enter Start:")
        goal = input("Enter Goal:")
        g.ucs(start, goal)
    elif choice == 8:
        start = input("Enter Start:")
        goal = input("Enter Goal:")
        g.dfs(start, goal)
    else:
        break
        
              
if __name__ == '__main__':
    main()
        
