class Graph:
    def __init__(self, vertices):
        self.vertices = vertices
        self.adj_list = [[] for _ in range(vertices)]

    def add_edge(self, u, v):
        self.adj_list[u].append(v)

    def depth_limited_search(self, start, end, depth_limit):
        visited = [False] * self.vertices
        return self._depth_limited_search(start, end, depth_limit, visited)

    def _depth_limited_search(self, current, end, depth_limit, visited):
        if current == end:
            return [current]
        if depth_limit == 0:
            return []

        visited[current] = True
        for neighbor in self.adj_list[current]:
            if not visited[neighbor]:
                path = self._depth_limited_search(neighbor, end, depth_limit - 1, visited)
                if path:
                    return [current] + path

        return []


# Example usage
g = Graph(7)
g.add_edge(0, 1)
g.add_edge(0, 2)
g.add_edge(1, 3)
g.add_edge(1, 4)
g.add_edge(2, 5)
g.add_edge(2, 6)

start_node = 0
end_node = 6
depth_limit = 3

result = g.depth_limited_search(start_node, end_node, depth_limit)
if result:
    print("Path found:", result)
else:
    print("Path not found within depth limit.")
