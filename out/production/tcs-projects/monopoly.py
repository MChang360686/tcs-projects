import random

board = []
names = ['Pain Street', 'Horror Street', 'Spaghetti Street']

class Player:
    def __init__(self, name):
        self.name = name
        self.money = 1500
        self.properties = []
        self.position = 0
        self.jail = False
        self.doubles = 0

    def move(self, steps):
        self.position = (self.position + steps) % len(board)
        if self.position < steps:  # wrapped around, passed GO
            self.money += 200
            print(f"{self.name} passed GO! +$200")

    def pay(self, amount, other=None):
        self.money -= amount
        if other:
            other.money += amount
        print(f"{self.name} paid ${amount} {'to ' + other.name if other else ''}")

    def add_property(self, prop):
        self.properties.append(prop)

    def __str__(self):
        return f"{self.name}: ${self.money}, Props: {[p.name for p in self.properties]}"

class Property:
    def __init__(self, value, rent, name):
        self.value = value
        self.rent = rent
        self.name = name
        self.owner = None

    def __str__(self):
        return f"{self.name} (Cost: {self.value}, Rent: {self.rent}, Owner: {self.owner.name if self.owner else 'None'})"

def d6():
    return random.randint(1, 6)

def chance(player):
    card = random.choice(['Get $100', 'Go to GO', 'Go to Jail', 'Get out of jail free'])
    print(f"{player.name} drew Chance: {card}")
    if card == 'Get $100':
        player.money += 100
    elif card == 'Go to GO':
        player.position = 0
        player.money += 200
    elif card == 'Go to Jail':
        player.jail = True
        player.position = 9
    elif card == 'Get out of jail free':
        player.jail = False

def comm_chest(player):
    card = random.choice(['Go to Jail', 'Gain $100', 'Lose $50'])
    print(f"{player.name} drew Community Chest: {card}")
    if card == 'Go to Jail':
        player.jail = True
        player.position = 9
    elif card == 'Gain $100':
        player.money += 100
    elif card == 'Lose $50':
        player.money -= 50

def build_board():
    for i in range(20):
        if i == 6 or i == 18:
            board.append(Property(2000, 100, 'Railroad'))
        elif i == 8:
            board.append('chance')
        elif i == 9:
            board.append("go to jail")
        elif i == 16:
            board.append('community chest')
        else:
            board.append(Property(random.randint(100, 300), random.randint(10, 50), random.choice(names)))

def game():
    build_board()
    num_players = int(input('Number of players: '))
    players = [Player(f"Player {i+1}") for i in range(num_players)]

    while len(players) > 1:
        for player in players[:]:
            if player.money <= 0:
                print(f"{player.name} is bankrupt! Removed from game.")
                players.remove(player)
                continue

            print(f"\n--- {player.name}'s Turn ---")
            d1, d2 = d6(), d6()
            print(f"Rolled {d1} and {d2}")
            player.move(d1 + d2)

            tile = board[player.position]
            print(f"{player.name} landed on {tile}")

            if isinstance(tile, Property):
                if tile.owner is None:
                    decision = input(f"Do you want to buy {tile.name} for ${tile.value}? (y/n): ")
                    if decision == 'y' and player.money >= tile.value:
                        player.pay(tile.value)
                        tile.owner = player
                        player.add_property(tile)
                elif tile.owner != player:
                    player.pay(tile.rent, tile.owner)

            elif tile == "go to jail":
                player.jail = True
                player.position = 9
                print(f"{player.name} goes to Jail!")

            elif tile == "chance":
                chance(player)

            elif tile == "community chest":
                comm_chest(player)

            print(player)

            # check bankruptcy
            if player.money <= 0:
                print(f"{player.name} went bankrupt!")
                players.remove(player)

            if len(players) == 1:
                break

    print(f"\n🏆 {players[0].name} wins with ${players[0].money}!")

game()
