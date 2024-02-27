import random

d6 = [1, 2, 3, 4, 5, 6]

class Person():
    def __init__(self, acc, dmg, mv_speed, special):
        self.acc = acc
        self.dmg = dmg
        self.mv_speed = mv_speed
        self.special = special

    def get_acc(self):
        return self.acc
    
    def get_dmg(self):
        return self.dmg
    
    def get_mv_speed(self):
        return self.mv_speed
    
    def set_mv_speed(self, speed):
        self.mv_speed = speed
    
    def get_special(self):
        return self.special
    

def special(player_obj, player_special):
    match (player_special):
        case "blitz":
            player_obj.set_mv_speed(80)
        case "jump":
            player_obj.set_mv_speed(60)


def play():

    bob = Person(10, 35, 30, "blitz")
    alice = Person(40, 10, 35, "jump")

    bad_guy = Person(10, 10, 10, "blitz")
    bad_guy_2 = Person(10, 10, 10, "jump")

    while True:
        player_action = input("Please enter a move ")
        player_name = input("Choose a player (alice or bob) ")

        if player_name == "alice":
            match (player_action):
                case "score":
                    s = alice.get_acc
                    s_random = random.randint(1, 100)
                    if s_random < s:
                        print("SCORE")
                case "steal":
                    d = alice.get_dmg
                    d_random = random.randint(1, 100)
                    if d_random < d:
                        print("Stolen")
        elif player_name == "bob":
            match (player_action):
                case "score":
                    s = bob.get_acc
                    s_random = random.randint(1, 100)
                    if s_random < s:
                        print("SCORE")
                case "steal":
                    d = bob.get_dmg
                    d_random = random.randint(1, 100)
                    if d_random < d:
                        print("Stolen")
        else:
            print("I don't know that player")