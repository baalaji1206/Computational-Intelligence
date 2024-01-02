class WumpusGame:
    def __init__(self, size, pits, wumpus, gold):
        self.size = size
        self.pits = pits
        self.wumpus = wumpus
        self.gold = gold
        self.player_position = (0, 0)
        self.arrow = 1
        self.path = []
        self.score = 0  # Initialize the score to 0

    def move(self, new_position):
        self.player_position = new_position
        #self.score-=1
        self.path.append(new_position)
        self.check_status()

    def check_status(self):
        x, y = self.player_position

        if self.player_position == self.wumpus:
            print("You have been devoured by the Wumpus.")
            self.score -= 100  # Deduct 100 points for reaching the Wumpus
            return False

        if self.player_position in self.pits:
            print("You fell into a pit and met your demise.")
            self.score -= 100  # Deduct 100 points for falling into a pit
            return False

        if self.player_position == self.gold:
            print("Congratulations! You have found the gold.")
            self.score += 1000  # Add 1000 points for reaching the gold
            return False

        return True

    def shoot(self, direction):
        if self.arrow > 0:
            self.arrow -= 1
            if direction == 'up':
                if self.player_position[0] == self.wumpus[0] and self.player_position[1] < self.wumpus[1]:
                    print("You have slain the Wumpus with your expert archery skills!")
                    self.wumpus = None
                    self.score += 500  # Add 500 points for slaying the Wumpus
                else:
                    print("Your arrow missed its target.")
            elif direction == 'down':
                if self.player_position[0] == self.wumpus[0] and self.player_position[1] > self.wumpus[1]:
                    print("You have slain the Wumpus with your expert archery skills!")
                    self.wumpus = None
                    self.score += 500  # Add 500 points for slaying the Wumpus
                else:
                    print("Your arrow missed its target.")
            elif direction == 'left':
                if self.player_position[1] == self.wumpus[1] and self.player_position[0] > self.wumpus[0]:
                    print("You have slain the Wumpus with your expert archery skills!")
                    self.wumpus = None
                    self.score += 500  # Add 500 points for slaying the Wumpus
                else:
                    print("Your arrow missed its target.")
            elif direction == 'right':
                if self.player_position[1] == self.wumpus[1] and self.player_position[0] < self.wumpus[0]:
                    print("You have slain the Wumpus with your expert archery skills!")
                    self.wumpus = None
                    self.score += 500  # Add 500 points for slaying the Wumpus
                else:
                    print("Your arrow missed its target.")
        else:
            print("You have no arrows left.")

    def print_game_world(self):
        for j in reversed(range(self.size)):
            for i in range(self.size):
                position = (i, j)
                if position == self.player_position:
                    print("A", end="\t")  # Player's position
                elif position == self.wumpus:
                    print("W", end="\t")  # Wumpus
                elif position in self.pits:
                    print("P", end="\t")  # Pit
                elif position == self.gold:
                    print("G", end="\t")  # Gold
                else:
                    adjacent_rooms = [(i + 1, j), (i - 1, j), (i, j + 1), (i, j - 1)]
                    stench = any(room == self.wumpus for room in adjacent_rooms)
                    breeze = any(room in self.pits for room in adjacent_rooms)
                    glitter = position == self.gold
                    if stench:
                        print("S", end="\t")
                    elif breeze:
                        print("B", end="\t")
                    elif glitter:
                        print("Gl", end="\t")
                    else:
                        print("-", end="\t")
            print("\n")


    def play(self):
        self.path.append(self.player_position)
        while True:
            x, y = self.player_position
            print("Current game state:")
            self.print_game_world()

            print(f"You are in room ({x}, {y}).")
            print("You sense:")

            # Automate the movement towards the gold
            if self.player_position[0] < self.gold[0]:
                new_position = (x + 1, y)
            elif self.player_position[0] > self.gold[0]:
                new_position = (x - 1, y)
            elif self.player_position[1] < self.gold[1]:
                new_position = (x, y + 1)
            elif self.player_position[1] > self.gold[1]:
                new_position = (x, y - 1)
            else:
                print("You have reached the gold!")
                break

            if 0 <= new_position[0] < self.size and 0 <= new_position[1] < self.size:
                self.move(new_position)
        count=-1
        print("Here is the path you took:")
        for position in self.path:
            count=count+1
            print(position)
        print("Total moves : ",count)
        print(f"Your final score is: {self.score}")

if __name__ == "__main__":
    size = int(input("Enter the size of the grid: "))
    pits = eval(input("Enter the locations of pits as a list of tuples: "))
    wumpus = eval(input("Enter the location of the Wumpus as a tuple: "))
    gold = eval(input("Enter the location of the gold as a tuple: "))

    game = WumpusGame(size, pits, wumpus, gold)
    print("Welcome to the Wumpus World!")
    game.play()