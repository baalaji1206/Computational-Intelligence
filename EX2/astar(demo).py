from queue import PriorityQueue
import pandas as pd
import numpy as np

class Node:
    def __init__(self,data,heuristic):
        self.data=data
        self.heuristic=heuristic
        self.neighbour=[]
        self.g_cost=float('inf')
        
class Graph:
    def __ini__(self):
        self.nodes={}
    
    def add_node(self,node,heuristic):
        self.nodes[node]=Node(self,node,heuristic)
    
    def add_edge(self,start,goal,cost):
        node1=self.nodes[start]
        node2=self.nodes[goal]
        node1.neighbour.append(goal,cost)
        
    def astar(self,start,goal):
        visited=set()
        pq=PriorityQueue()
        pq.put(0+self.nodes[start].heuristic,0,[start])
        
        while not pq.empty():
            current_cost,g_cost,current_path=pq.get()
            current_vertex=current_path[-1]
            
            if current_vertex==goal:
                return current_path,current_cost
            
            if current_vertex in visited:
                continue
            
            visited.add(current_vertex)
            current_node=self.nodes[current_vertex]
             
            intermediate_path=[]
        
             
            for neighbour,cost in current_node.neighbour:
                if neighbour not in visited:
                    new_g_cost=cost+g_cost
                    if new_g_cost <= self.nodes[neighbour].g_cost:
                        self.nodes[neighbour].g_cost=new_g_cost
                        
                else:
                    new_g_cost=cost+g_cost
                    new_h_cost=self.nodes[neighbour].heuristic
                    new_cost=new_g_cost+new_h_cost
                    new_path=current_path+[neighbour]
                    pq.put((new_cost,new_g_cost,new_path))
                    intermediate_path.append(new_cost,new_path)
                
                print("possible path from" +str(current_vertex))
                for cost,path in intermediate_path:
                    print(f"{' -> '.join(path)} \t Cost: {cost}")
                
        return float('inf'),None