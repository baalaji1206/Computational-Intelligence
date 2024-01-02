import random


class WumpusWorld:
    def __init__(self, size=4, num_pits=3):
        self.size = size
        self.num_pits = num_pits
        self.grid = [[None for _ in range(size)] for _ in range(size)]
        self.agent_pos = (0, 0)
        self.gold_pos = None
        self.wumpus_pos = None
        self.stench_pos = set()
        self.pit_pos = set()
        self.breeze_cells = set()

        self.generate_world()

    def generate_world(self):
        # Place gold randomly
        self.gold_pos = (
            random.randint(0, self.size - 1),
            random.randint(0, self.size - 1),
        )

        # Place wumpus randomly
        while self.wumpus_pos is None or self.wumpus_pos == (0, 0):
            self.wumpus_pos = (
                random.randint(0, self.size - 1),
                random.randint(0, self.size - 1),
            )
        x, y = self.wumpus_pos
        l = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        i = random.randint(0, 3)
        dx, dy = l[i]
        nx, ny = x + dx, y + dy
        if 0 <= nx < self.size and 0 <= ny <= self.size:
            self.stench_pos.add((nx, ny))

        # Place pits randomly
        for _ in range(self.num_pits):
            while True:
                pit_pos = (
                    random.randint(0, self.size - 1),
                    random.randint(0, self.size - 1),
                )
                if (
                    pit_pos != (0, 0)
                    and pit_pos != self.wumpus_pos
                    and pit_pos != self.gold_pos
                    and pit_pos not in self.pit_pos
                    and pit_pos != self.stench_pos
                ):
                    self.pit_pos.add(pit_pos)
                    self.add_breeze(pit_pos)
                    break

    def add_breeze(self, pos):
        x, y = pos
        for dx, dy in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nx, ny = x + dx, y + dy
            if 0 <= nx < self.size and 0 <= ny < self.size:
                self.breeze_cells.add((nx, ny))

    def is_adjacent(self, pos1, pos2):
        x1, y1 = pos1
        x2, y2 = pos2
        return abs(x1 - x2) + abs(y1 - y2) == 1

    def get_percepts(self):
        percepts = []
        msg = []

        if self.agent_pos == self.gold_pos:
            percepts.append("glitter")
            msg.append("Cell contains gold")
        if self.agent_pos == self.wumpus_pos:
            percepts.append("stench")
            msg.append("Adjacent cells may contain wumpus")
        if self.agent_pos in self.breeze_cells:
            percepts.append("breeze")
            msg.append("Adjacent cells may contain pit")

        return percepts, msg

    def move_forward(self):
        x, y = self.agent_pos
        new_x = min(x + 1, self.size - 1)
        self.agent_pos = (new_x, y)

    def move_backward(self):
        x, y = self.agent_pos
        new_x = max(x - 1, 0)
        self.agent_pos = (new_x, y)

    def turn_left(self):
        x, y = self.agent_pos
        new_y = max(y - 1, 0)
        self.agent_pos = (x, new_y)

    def turn_right(self):
        x, y = self.agent_pos
        new_y = min(y + 1, self.size - 1)
        self.agent_pos = (x, new_y)

    def grab(self):
        if self.agent_pos == self.gold_pos:
            self.gold_pos = None

    def shoot(self):
        if self.agent_pos == self.wumpus_pos:
            self.wumpus_pos = None

    def print_world(self):
        for row in range(self.size):
            for col in range(self.size):
                cell = ""
                if (row, col) == self.agent_pos:
                    cell += "A"
                if (row, col) == self.gold_pos:
                    cell += "G"
                if (row, col) == self.wumpus_pos:
                    cell += "W"
                if (row, col) in self.pit_pos:
                    cell += "P"
                if (row, col) in self.breeze_cells:
                    cell += "B"
                if (row, col) in self.stench_pos:
                    cell += "S"
                if not cell:
                    cell = " "
                print(f"{cell:<5}", end="")
            print()

    def play(self, count):
        c = 0
        print("Welcome to Wumpus World!")
        while True:
            self.print_world()
            percepts, msg = self.get_percepts()
            print("Percepts:", percepts)
            print("Message: ", msg)
            if c == count:
                print("Maximum moves reached!!")
                break
            else:
                if "glitter" in percepts:
                    action = input("Grab the gold? (yes/no): ")
                    if action.lower() == "yes":
                        self.grab()

                if "stench" in percepts:
                    action = input("Shoot the wumpus? (yes/no): ")
                    if action.lower() == "yes":
                        self.shoot()

                action = input(
                    "Enter your action (move_forward/move_backward/turn_left/turn_right): "
                )
                c = c + 1
                if action.lower() == "move_forward":
                    self.move_forward()

                elif action.lower() == "turn_left":
                    self.turn_left()
                elif action.lower() == "turn_right":
                    self.turn_right()
                elif action.lower() == "move_backward":
                    self.momove_forwardve_backward()

                if self.agent_pos == self.wumpus_pos:
                    print("Game Over! You were eaten by the wumpus!")
                    break
                if self.agent_pos in self.pit_pos:
                    print("Game Over! You fell into a pit!")
                    break
                if self.agent_pos == self.gold_pos:
                    print("Congratulations! You found the gold and won!")
                    break


if __name__ == "__main__":
    wumpus_world = WumpusWorld()
    c = int(input("Enter total moves:"))
    wumpus_world.play(c)