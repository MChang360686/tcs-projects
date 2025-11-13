import random
import math

class Player:
    def __init__(self, stre, end, agi, dex, spd, luck):
        self.stre = stre
        self.end = end
        self.agi = agi
        self.dex = dex
        self.spd = spd
        self.luck = luck
        self.main_arm = None
        self.side_arm = None
        self.hp = end * 10  
        self.max_hp = self.hp
        self.position = 0  

    def get_stre(self): return self.stre
    def set_stre(self, amt): self.stre += amt
    def get_end(self): return self.end
    def set_end(self, amt): self.end += amt
    def get_agi(self): return self.agi
    def set_agi(self, amt): self.agi += amt
    def get_dex(self): return self.dex
    def set_dex(self, amt): self.dex += amt
    def get_spd(self): return self.spd
    def set_spd(self, amt): self.spd += amt
    def get_luck(self): return self.luck
    def set_luck(self, amt): self.luck += amt

    def equip_main(self, weapon):
        if isinstance(weapon, Weapon):
            self.main_arm = weapon
            print(f"Equipped {weapon.name} as main weapon.")

    def equip_side(self, weapon):
        if isinstance(weapon, Weapon):
            self.side_arm = weapon
            print(f"Equipped {weapon.name} as sidearm.")

    def is_alive(self):
        return self.hp > 0

class Weapon:
    def __init__(self, name, dmg, rng, ammo=None, reload_time=0):
        self.name = name
        self.dmg = dmg
        self.rng = rng  # Max effective range in meters
        self.ammo = ammo  # None for melee, int for guns
        self.max_ammo = ammo
        self.reload_time = reload_time  # Turns to reload

    def get_name(self): return self.name
    def get_dmg(self): return self.dmg
    def get_rng(self): return self.rng

    def fire(self):
        if self.ammo is None:
            return True  # Melee always works
        if self.ammo > 0:
            self.ammo -= 1
            return True
        return False

    def reload(self, turns):
        if self.ammo is not None and self.ammo < self.max_ammo:
            print(f"Reloading {self.name}... ({turns} turns)")
            self.ammo = self.max_ammo
            return turns
        return 0

class Zombie:
    def __init__(self, zombie_type, spd, hp, dmg, weapon=None):
        self.zombie_type = zombie_type
        self.spd = spd
        self.hp = hp
        self.dmg = dmg
        self.weapon = weapon
        self.position = 50  # Starts 50 meters away

    def get_type(self): return self.zombie_type
    def get_spd(self): return self.spd
    def get_hp(self): return self.hp
    def get_dmg(self): return self.dmg

    def is_alive(self):
        return self.hp > 0

    def move(self, distance):
        move_dist = min(self.spd, distance)
        self.position -= move_dist
        return move_dist

# ================== DICE ==================

def d100():
    return random.randint(1, 100)

def d6():
    return random.randint(1, 6)

# ================== ZOMBIE FACTORY ==================

def make_zombie(num_zombies=1):
    types = {
        1: ('normal', 3, 30, 8),
        2: ('fast', 7, 20, 6),
        3: ('fat', 2, 60, 12),
        4: ('armed', 3, 35, 15, Weapon("Rusty Pipe", 15, 2)),
        5: ('fat + armed', 1, 80, 18, Weapon("Crowbar", 20, 2)),
        6: ('fast + fat', 4, 50, 10),
        7: ('police', 4, 40, 12, Weapon("Pistol", 25, 15, ammo=6, reload_time=2)),
        8: ('military', 5, 50, 20, Weapon("Rifle", 40, 50, ammo=30, reload_time=3))
    }
    
    zombies = []
    for _ in range(num_zombies):
        roll = d6() + d6() if num_zombies > 3 else random.randint(1, 8)
        roll = min(roll, 8)
        z_type, spd, hp, dmg = types[roll][:4]
        weapon = types[roll][4] if len(types[roll]) > 4 else None
        zombies.append(Zombie(z_type, spd, hp, dmg, weapon))
    return zombies

# ================== WEAPONS ==================

WEAPONS = {
    "knife": Weapon("Combat Knife", 12, 1),
    "pistol": Weapon("9mm Pistol", 20, 20, ammo=15, reload_time=2),
    "shotgun": Weapon("Pump Shotgun", 45, 10, ammo=8, reload_time=3),
    "bat": Weapon("Baseball Bat", 15, 2),
    "axe": Weapon("Fire Axe", 25, 2),
    "rifle": Weapon("Hunting Rifle", 50, 100, ammo=5, reload_time=3)
}

# ================== COMBAT SYSTEM ==================

def combat_round(player, zombie, distance, reloading=0):
    print(f"\n{'='*50}")
    print(f"Distance: {distance}m | Zombie HP: {zombie.hp} | Your HP: {player.hp}/{player.max_hp}")
    
    if reloading > 0:
        print(f"Reloading... {reloading} turn(s) left.")
        return distance, reloading - 1

    action = input("\n(a)ttack, (r)eload, (m)ove back, (s)witch weapon, ( s t a t u s ): ").lower().strip()

    # Status
    if action == "status":
        print(player.__dict__)
        if player.main_arm: print(f"Main: {player.main_arm.name} ({player.main_arm.ammo})")
        if player.side_arm: print(f"Side: {player.side_arm.name} ({player.side_arm.ammo})")
        return combat_round(player, zombie, distance, reloading)

    # Switch weapon
    if action == "s" and player.side_arm:
        player.main_arm, player.side_arm = player.side_arm, player.main_arm
        print(f"Switched to {player.main_arm.name}")
        return distance, 0

    # Move back
    if action == "m":
        move = player.spd
        distance += move
        print(f"You back away {move}m.")
    else:
        move = 0

    # Attack
    weapon = player.main_arm
    if not weapon:
        print("You have no weapon!")
        return distance, 0

    if action == "a":
        if weapon.ammo is not None and weapon.ammo == 0:
            print("Out of ammo! Reload or switch.")
            return distance, 0

        # Range check
        if distance > weapon.rng:
            print(f"Too far! ({distance}m > {weapon.rng}m range)")
            move = player.spd // 2
            distance += move
            print(f"You retreat {move}m.")
        else:
            hit_roll = d100()
            crit = hit_roll > 95 or hit_roll + player.luck > 100
            dodge_roll = d100() - zombie.spd * 2

            if hit_roll > 15 and hit_roll > dodge_roll:
                dmg = weapon.dmg + player.stre // 3
                if crit:
                    dmg = int(dmg * 1.5)
                    print("CRITICAL HIT!")
                zombie.hp -= dmg
                print(f"You hit for {dmg} damage!")
                if weapon.ammo is not None:
                    weapon.fire()
            else:
                print("You missed!")

    # Reload
    if action == "r" and weapon.ammo is not None and weapon.ammo < weapon.max_ammo:
        return distance, weapon.reload(weapon.reload_time)

    # Zombie turn
    if zombie.is_alive():
        move_dist = zombie.move(distance)
        distance -= move_dist
        print(f"Zombie closes in {move_dist}m! Now at {distance}m.")

        if distance <= 2 and zombie.is_alive():
            print("Zombie attacks!")
            hit = d100() > 30
            if hit:
                dmg = zombie.dmg
                if zombie.weapon:
                    dmg = zombie.weapon.dmg
                    if zombie.weapon.ammo is not None and random.random() < 0.7:
                        zombie.weapon.fire()
                    else:
                        dmg = zombie.dmg  # Fists if out of ammo
                player.hp -= dmg
                print(f"Zombie hits for {dmg}! Your HP: {player.hp}")
            else:
                print("Zombie swings and misses!")

    return distance, 0

# ================== MAIN GAME ==================

def main():
    print("=== ZOMBIE SURVIVAL GAME ===")
    name = input("Enter your name: ")
    
    # Random stats or manual
    choice = input("Random stats? (y/n): ").lower()
    if choice == "y":
        stats = [random.randint(8, 18) for _ in range(6)]
    else:
        print("Assign 75 points across 6 stats (min 5, max 18):")
        stats = []
        points = 75
        for stat in ["Strength", "Endurance", "Agility", "Dexterity", "Speed", "Luck"]:
            while True:
                try:
                    val = int(input(f"{stat} ({points} left): "))
                    if 5 <= val <= 18 and val <= points:
                        stats.append(val)
                        points -= val
                        break
                    print("Invalid. Must be 5-18 and within points.")
                except:
                    print("Enter a number.")
    
    player = Player(*stats)
    player.hp = player.end * 10
    player.max_hp = player.hp

    # Starting weapons
    player.equip_main(WEAPONS["knife"])
    player.equip_side(WEAPONS["pistol"])

    print(f"\n{name}, prepare yourself...")
    input("Press Enter to begin...")

    wave = 1
    while player.is_alive():
        print(f"\n{'*' * 20} WAVE {wave} {'*' * 20}")
        zombies = make_zombie(wave)
        for i, zombie in enumerate(zombies):
            print(f"\nZombie #{i+1}: {zombie.zombie_type.upper()} approaches!")
            distance = 50
            reloading = 0
            while zombie.is_alive() and player.is_alive() and distance > 0:
                distance, reloading = combat_round(player, zombie, distance, reloading)
                if player.hp <= 0:
                    print("\nYou have been overwhelmed... Game Over.")
                    return
                if zombie.hp <= 0:
                    print(f"\n{zombie.zombie_type.upper()} defeated!")
                    break
            if distance <= 0 and zombie.is_alive():
                print("The zombie is upon you!")
                player.hp = 0

        if not player.is_alive():
            print("\nYou fought bravely, but the horde won.")
            break

        print(f"\nWave {wave} cleared! +1 to all stats.")
        for attr in ['stre', 'end', 'agi', 'dex', 'spd', 'luck']:
            setattr(player, attr, getattr(player, attr) + 1)
        player.max_hp += 10
        player.hp = player.max_hp
        wave += 1

        if wave > 5:
            print("\nYou've survived 5 waves! You're a legend!")
            break

        cont = input("\nContinue to next wave? (y/n): ")
        if cont.lower() != 'y':
            print("You escape into the night...")
            break

    print(f"\nFinal Stats:")
    print(f"HP: {player.hp}/{player.max_hp}")
    print(f"STR: {player.stre} | END: {player.end} | AGI: {player.agi}")
    print(f"DEX: {player.dex} | SPD: {player.spd} | LUK: {player.luck}")

if __name__ == "__main__":
    main()