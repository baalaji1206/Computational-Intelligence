from queue import PriorityQueue
import numpy as np
import pandas as pd
class Node:
    def __init__(self, data, heuristic):
        self.data = data
        self.neighbors = []
        self.heuristic = heuristic
        self.g_cost = float('inf')

class Graph:
    def __init__(self):
        self.nodes = {}
    
    def add_node(self, node, heuristic):
        self.nodes[node] = Node(node, heuristic)

    def add_edge(self, start, end, cost):
        node1 = self.nodes[start]
        node2 = self.nodes[end]
        node1.neighbors.append((end, cost))
        #node2.neighbors.append((start, cost))
    
    def astar_search(self, start, goal):
        visited = set()
        pq = PriorityQueue()
        pq.put((0 + self.nodes[start].heuristic, 0, [start]))

        while not pq.empty():
            current_cost, g_cost, current_path = pq.get()
            current_vertex = current_path[-1]

            if current_vertex == goal:
                return current_cost, current_path

            if current_vertex in visited:
                continue

            visited.add(current_vertex)
            current_node = self.nodes[current_vertex]

            intermediate_paths = []

            for neighbor, cost in current_node.neighbors:
                if neighbor in visited:
                    new_g_cost = g_cost + cost
                    if new_g_cost < self.nodes[neighbor].g_cost:
                        self.nodes[neighbor].g_cost = new_g_cost
                else:
                    new_g_cost = g_cost + cost
                    new_h_cost = self.nodes[neighbor].heuristic
                    new_cost = new_g_cost + new_h_cost
                    new_path = current_path + [neighbor]
                    pq.put((new_cost, new_g_cost, new_path))
                    intermediate_paths.append((new_cost, new_path))

            print(f"Possible paths from {current_vertex}:")
            for cost, path in intermediate_paths:
                print(f"{' -> '.join(path)} \t Cost: {cost}")
           

        return float('inf'), None
    
graph = Graph()

while(True):
    print("\n=======MENU=======")
    print("1 - Add Node")
    print("2 - Add Edge")
    print("3 - A-Star Search")
    print("4 - Exit")
    print("==================\n")
    choice = int(input("Enter choice: "))
    inp = pd.read_csv("input.csv")
    node_input = inp["Node"]
    heuristic_input = inp["Heuristic"]
    edgecost = pd.read_csv("edgecost.csv")
    n1_inp = edgecost["Node1"]
    n2_inp = edgecost["Node2"]
    cost_inp = edgecost["Cost"]
    if(choice==1):
        for i in range(len(node_input)):
            graph.add_node(node_input[i], heuristic_input[i])
    elif(choice==2):
        for i in range(len(n1_inp)):
            graph.add_edge(n1_inp[i], n2_inp[i], cost_inp[i])
    elif(choice==3):
        source = input("Enter source node: ")
        goal = input("Enter goal node: ")
        cost, path = graph.astar_search(source, goal)
        if path is not None:
            print(f"\nOptimal path: {' -> '.join(path)}")
            print(f"Optimal cost: {cost}")
        else:
            print("No path found.")

    elif(choice==4):
        break

    else:
        print("Enter a valid choice!")
