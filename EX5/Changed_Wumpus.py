from collections import deque
class WumpusWorld:
    def __init__(self, size,w_x,w_y,num_pits,pits,g_x,g_y):
        self.size = size
        self.grid = [[Cell() for _ in range(size)] for _ in range(size)]
        self.agent_pos = (size - 1, 0)  # Starting from bottom left
        self.agent_direction = "right"  # Starting direction
        """self.gold_x = g_x
        self.gold_y = g_y"""
        self.generate_world(w_x,w_y,num_pits,pits,g_x,g_y)
    def generate_world(self,w_x,w_y,num_pits,pits,g_x,g_y):
        wumpus_x = w_x
        wumpus_y = w_y
        self.grid[wumpus_x][wumpus_y].has_wumpus = True
        for pit in range(num_pits):
            pit_x, pit_y = pits[pit][0],pits[pit][1]
            self.grid[pit_x][pit_y].has_pit = True
            # Mark adjacent cells as having breeze
            for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                new_x, new_y = pit_x + dx, pit_y + dy
                if (new_x, new_y) == self.agent_pos:
                    continue  # Skip marking the starting cell
                if 0 <= new_x < self.size and 0 <= new_y < self.size:
                    self.grid[new_x][new_y].has_breeze = True
        self.gold_x, self.gold_y = g_x,g_y
        self.grid[self.gold_x][self.gold_y].has_gold = True
        for i in range(self.size):
            for j in range(self.size):
                if self.grid[i][j].has_wumpus:
                    for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                        if 0 <= i + dx < self.size and 0 <= j + dy < self.size:
                            self.grid[i + dx][j + dy].has_stench = True
                if self.grid[i][j].has_gold:
                    self.grid[i][j].has_glitter = True

    def print_world(self):
        for i in range(self.size):
            print(i, end="| ")
            for j in range(self.size):
                cell = self.grid[i][j]
                if (i, j) == self.agent_pos:
                    print("A", end="\t")
                else:
                    symbols = ""
                    if cell.has_wumpus:
                        symbols += "w"
                    if cell.has_pit:
                        symbols += "P"
                    if cell.has_gold:
                        symbols += "G"
                    if cell.has_stench:
                        symbols += "S"
                    if cell.has_breeze:
                        symbols += "B"
                    if cell.has_glitter:
                        symbols += "gl"
                    if symbols:
                        print(symbols, end="\t")
                    else:
                        print("-", end="\t")
            print("\n")
    def bfs(self, start, goal):
        queue = deque([(start, [])])
        visited = set()
        while queue:
            current, path = queue.popleft()
            if current == goal:
                return path
            if current in visited:
                continue
            visited.add(current)
            x, y = current
            neighbors = self.get_valid_neighbors(x, y)
            for neighbor in neighbors:
                n_x, n_y = neighbor
                if self.grid[n_x][n_y].has_pit:
                    continue  # Skip paths leading to pits
                queue.append((neighbor, path + [neighbor]))
        return None
    def get_valid_neighbors(self, x, y):
        neighbors = []
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            new_x, new_y = x + dx, y + dy
            if 0 <= new_x < self.size and 0 <= new_y < self.size:
                neighbors.append((new_x, new_y))
        return neighbors

    def find_gold(self):
        start = (self.agent_pos[0], self.agent_pos[1])
        gold_pos = (self.gold_x,self.gold_y)
        """if not gold_pos:
            return []"""
        path = self.bfs(start, gold_pos)
        return path

    def play(self):
        optimal_path = self.find_gold()

        if not optimal_path:
            print("No path to the gold.")
            return
        print("Optimal path to the gold:", optimal_path)
        self.print_world()
        for step, (x, y) in enumerate(optimal_path):
            self.agent_pos = (x, y)
            print("Next Step.")
            self.print_world()
            
            if self.grid[x][y].has_gold:
                print("Congratulations! You found the gold and won!")
                break

class Cell:
    def __init__(self):
        self.visited = False
        self.has_wumpus = False
        self.has_pit = False
        self.has_gold = False
        self.has_stench = False
        self.has_breeze = False
        self.has_glitter = False

size = int(input("Enter the size:")) 
w_x,w_y = [int(x) for x in input("Enter the poisition of wumpus: ").split(",")]
num_pits = int(input("Enter the number of Pits: "))
pits=[]
for i in range(num_pits):
    p_x,p_y = [int(x) for x in input("Enter the position: ").split(",")]
    pits.append([p_x,p_y])
g_x,g_y = [int(x) for x in input("Enter the position of Gold: ").split(",")]
game = WumpusWorld(size,w_x,w_y,num_pits,pits,g_x,g_y)
game.play()

