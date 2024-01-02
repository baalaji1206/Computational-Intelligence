def costMatrix(self):
        
        for key in self.adj.keys():
            for i in self.adj[key]:
                print("Enter cost for "+key+" - "+i)
                self.cost_matrix.setdefault(key,{})[i] = int(input()) 
                
        print("Cost Matrix is")
        for key in self.adj.keys():
            print("Node", key, ":", self.cost_matrix[key])