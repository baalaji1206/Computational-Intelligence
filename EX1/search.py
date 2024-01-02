from queue import PriorityQueue
from collections import deque

class Node:
    def __init__(self, data, cost):
        self.data = data
        self.cost = cost
        self.next = None
        self.depth = 0

class Graph:
    def __init__(self):
        self.vertices = {}

    def add_vertex(self, data):
        if data not in self.vertices:
            self.vertices[data] = None

    def add_edge(self, src, dest, cost):
        if src not in self.vertices:
            self.add_vertex(src)

        if dest not in self.vertices:
            self.add_vertex(dest)

        new_node = Node(dest, cost)
        new_node.next = self.vertices[src]
        self.vertices[src] = new_node

        new_node = Node(src, cost)
        new_node.next = self.vertices[dest]
        self.vertices[dest] = new_node

    def delete_vertex(self, data):
        if data in self.vertices:
            del self.vertices[data]
            for vertex in self.vertices:
                self.delete_edge(vertex, data)

    def delete_edge(self, src, dest):
        if src in self.vertices and dest in self.vertices:
            current_node = self.vertices[src]
            prev_node = None

            while current_node:
                if current_node.data == dest:
                    if prev_node is None:
                        self.vertices[src] = current_node.next
                    else:
                        prev_node.next = current_node.next
                    break

                prev_node = current_node
                current_node = current_node.next

    def get_adjacent_vertices(self, vertex):
        if vertex in self.vertices:
            adjacent_vertices = []
            current_node = self.vertices[vertex]

            while current_node:
                adjacent_vertices.append(current_node.data)
                current_node = current_node.next

            return adjacent_vertices
        else:
            return []

    def display_graph(self):
        for vertex in self.vertices:
            print(f"Vertex {vertex}: ", end="")
            current_node = self.vertices[vertex]
            while current_node:
                print(f"{current_node.data} ({current_node.cost}) -> ", end="")
                current_node = current_node.next
            print("None")

    def dfs(self, start, destination):
        visited = set()
        stack = [start]

        while stack:
            current_vertex = stack.pop()
            print(current_vertex, end=" ")

            if current_vertex == destination:
                print("\nReached destination!")
                return

            visited.add(current_vertex)
            current_node = self.vertices[current_vertex]

            while current_node:
                if current_node.data not in visited:
                    stack.append(current_node.data)
                current_node = current_node.next

        print("\nDestination not found!")


    def bfs(self, start, destination):
        visited = set()
        queue = deque([start])

        while queue:
            current_vertex = queue.popleft()
            print(current_vertex, end=" ")

            if current_vertex == destination:
                print("\nReached destination!")
                return

            visited.add(current_vertex)
            current_node = self.vertices[current_vertex]

            while current_node:
                if current_node.data not in visited:
                    queue.append(current_node.data)
                    visited.add(current_node.data)
                current_node = current_node.next

        print("\nDestination not found!")

    def uniform_cost_search(self, start, destination):
        visited = set()
        pq = PriorityQueue()
        pq.put((0, [start]))
        explored_paths = []

        while not pq.empty():
            current_cost, current_path = pq.get()
            current_vertex = current_path[-1]

            if current_vertex == destination:
                explored_paths.append(current_path)
                print(f"\nReached destination with cost {current_cost} Path: {' -> '.join(current_path)}")
                return

            visited.add(current_vertex)
            current_node = self.vertices[current_vertex]
            print(f"Current Cost: {current_cost} Path: {' -> '.join(current_path)}")

            while current_node:
                if current_node.data not in visited:
                    new_cost = current_cost + current_node.cost
                    new_path = current_path + [current_node.data]
                    pq.put((new_cost, new_path))
                    explored_paths.append(new_path)
                    print(f"Current Cost: {new_cost} Path: {' -> '.join(new_path)}")
                current_node = current_node.next
            

        print("\nDestination not found, No path, UCS cannot be performed")
        return explored_paths

def main():
    graph = Graph()
    while True:
        print("1. Add new Vertex")
        print("2. Add new Edge")
        print("3. Display Graph")
        print("4. DFS")
        print("5. BFS")
        print("6. Get adjacent vertices")
        print("7. Delete Node")
        print("8. Delete Edge")
        print("9. Uniform Cost Search")
        print("10. Exit")
        print("Enter your choice:")
        ch = int(input())
        if ch == 1:
            print("Enter the vertex:")
            data = input()
            graph.add_vertex(data)
        elif ch == 2:
            print("Enter the source vertex:")
            src = input()
            print("Enter the destination vertex:")
            dest = input()
            print("Enter the edge cost:")
            cost = float(input())
            graph.add_edge(src, dest, cost)
        elif ch == 3:
            print("The Graph is:")
            graph.display_graph()
        elif ch == 4:
            print("Enter the source vertex:")
            src = input()
            print("Enter the destination vertex:")
            dest = input()
            print("DFS Traversal:")
            graph.dfs(src, dest)
        elif ch == 5:
            print("Enter the source vertex:")
            src = input()
            print("Enter the destination vertex:")
            dest = input()
            print("BFS Traversal:")
            graph.bfs(src, dest)
        elif ch == 6:
            print("Enter the vertex:")
            data = input()
            res = graph.get_adjacent_vertices(data)
            print(res)
        elif ch == 7:
            print("Enter the vertex to be deleted:")
            data = input()
            graph.delete_vertex(data)
            graph.display_graph()
        elif ch == 8:
            print("Enter the source vertex:")
            src = input()
            print("Enter the destination vertex:")
            dest = input()
            graph.delete_edge(src, dest)
            graph.display_graph()
        elif ch == 9:
            print("Enter the source vertex:")
            src = input()
            print("Enter the destination vertex:")
            dest = input()
            graph.uniform_cost_search(src, dest)
        elif ch == 10:
            break
        else:
            print("Wrong input!!!")

if __name__ == "__main__":
    main()
