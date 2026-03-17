import random
import os
import time

# ─────────────────────────────────────────────
#  Utility
# ─────────────────────────────────────────────

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def slow_print(text, delay=0.03):
    for ch in text:
        print(ch, end="", flush=True)
        time.sleep(delay)
    print()

def bar(current, maximum, width=20, fill="█", empty="░"):
    filled = int(width * current / max(maximum, 1))
    return f"[{fill * filled}{empty * (width - filled)}] {current}/{maximum}"

# ─────────────────────────────────────────────
#  Trait / Perk definitions
# ─────────────────────────────────────────────

AVAILABLE_TRAITS = {
    "Fast Learner":  {"desc": "Gain +1 INT permanently after each combat.",   "type": "positive"},
    "Iron Skin":     {"desc": "Start each fight with 3 bonus Armor.",          "type": "positive"},
    "Adrenaline":    {"desc": "When below 25% HP, gain +3 SPD.",               "type": "positive"},
    "Weak Stomach":  {"desc": "Poison duration lasts 1 extra turn.",           "type": "negative"},
    "Glass Jaw":     {"desc": "Take +2 damage from every hit.",                "type": "negative"},
}

AVAILABLE_PERKS = {
    "Brawler":    {"desc": "Unarmed attacks deal +3 damage.",           "bonus": {"dmg": 3}},
    "Sprinter":   {"desc": "First attack each fight is a guaranteed hit.","bonus": {"first_hit": True}},
    "Tough":      {"desc": "+10 max HP.",                               "bonus": {"hp": 10}},
    "Evasive":    {"desc": "+15% dodge chance.",                        "bonus": {"dodge": 0.15}},
    "Medic":      {"desc": "Rest heals 50% more HP.",                  "bonus": {"heal_mult": 1.5}},
}

# ─────────────────────────────────────────────
#  Player
# ─────────────────────────────────────────────

class Player:
    def __init__(self):
        self.name   = "Survivor"
        self.str    = random.randint(5, 10)
        self.end    = random.randint(5, 10)
        self.agi    = random.randint(5, 10)
        self.spd    = random.randint(5, 10)
        self.intel  = random.randint(5, 10)  # 'int' is a builtin – use intel

        self.perks  = {}   # name -> perk dict
        self.traits = {}   # name -> trait dict

        self.max_hp = (2 * self.str) + (3 * self.end)
        self.hp     = self.max_hp
        self.xp     = 0
        self.level  = 1
        self.armor  = 0

        self.status_effects = {}   # e.g. {"poison": 3}
        self.inventory       = {"medkit": 1, "bandage": 2}
        self.kills           = 0
        self.day             = 1

    # ── derived stats ──────────────────────────
    @property
    def damage(self):
        base = self.str + random.randint(1, 6)
        if "Brawler" in self.perks:
            base += self.perks["Brawler"]["bonus"]["dmg"]
        return base

    @property
    def dodge_chance(self):
        chance = min(0.60, self.agi * 0.04)
        if "Evasive" in self.perks:
            chance += self.perks["Evasive"]["bonus"]["dodge"]
        return chance

    @property
    def hit_chance(self):
        return min(0.95, 0.50 + self.intel * 0.03 + self.spd * 0.01)

    @property
    def effective_armor(self):
        bonus = 3 if "Iron Skin" in self.traits else 0
        return self.armor + bonus

    @property
    def effective_spd(self):
        spd = self.spd
        if "Adrenaline" in self.traits and self.hp < self.max_hp * 0.25:
            spd += 3
        return spd

    # ── healing ────────────────────────────────
    def heal(self, amount):
        mult = self.perks.get("Medic", {}).get("bonus", {}).get("heal_mult", 1.0)
        healed = min(self.max_hp - self.hp, int(amount * mult))
        self.hp += healed
        return healed

    # ── levelling ──────────────────────────────
    def add_xp(self, amount):
        self.xp += amount
        threshold = self.level * 50
        if self.xp >= threshold:
            self.xp -= threshold
            self.level_up()

    def level_up(self):
        self.level += 1
        stat = random.choice(["str", "end", "agi", "spd", "intel"])
        setattr(self, stat, getattr(self, stat) + 1)
        old_max = self.max_hp
        self.max_hp = (2 * self.str) + (3 * self.end)
        self.hp    += self.max_hp - old_max
        if "Fast Learner" in self.traits:
            self.intel += 1
        slow_print(f"\n  ★  Level up! Now level {self.level}. {stat.upper()} increased!")

    # ── status effects ─────────────────────────
    def apply_status(self, effect, duration):
        self.status_effects[effect] = self.status_effects.get(effect, 0) + duration

    def tick_statuses(self):
        msgs = []
        if "poison" in self.status_effects:
            dmg = 3
            self.hp -= dmg
            msgs.append(f"  ☠  Poison deals {dmg} damage! ({self.hp}/{self.max_hp} HP)")
            dur = self.status_effects["poison"] - 1
            if "Weak Stomach" in self.traits:
                dur = self.status_effects["poison"]   # extra turn
            self.status_effects["poison"] = dur
            if self.status_effects["poison"] <= 0:
                del self.status_effects["poison"]
                msgs.append("  ✓  Poison has worn off.")
        return msgs

    # ── display ────────────────────────────────
    def show_stats(self):
        print(f"\n{'─'*40}")
        print(f"  {self.name}  |  Level {self.level}  |  Day {self.day}")
        print(f"  HP     {bar(self.hp, self.max_hp)}")
        print(f"  XP     {bar(self.xp, self.level*50)}")
        print(f"  STR {self.str:>2}  END {self.end:>2}  AGI {self.agi:>2}"
              f"  SPD {self.spd:>2}  INT {self.intel:>2}")
        print(f"  Armor: {self.effective_armor}  "
              f"Dodge: {self.dodge_chance:.0%}  "
              f"Hit: {self.hit_chance:.0%}")
        if self.traits:
            print(f"  Traits: {', '.join(self.traits)}")
        if self.perks:
            print(f"  Perks:  {', '.join(self.perks)}")
        if self.status_effects:
            fx = ", ".join(f"{k}({v})" for k, v in self.status_effects.items())
            print(f"  Status: {fx}")
        print(f"{'─'*40}")

# ─────────────────────────────────────────────
#  Enemy
# ─────────────────────────────────────────────

class Enemy:
    def __init__(self, name, stre, end, agi, spd, inte,
                 xp_reward=20, loot=None, special=None):
        self.name    = name
        self.str     = stre
        self.end     = end
        self.agi     = agi
        self.spd     = spd
        self.intel   = inte
        self.max_hp  = (2 * self.str) + (3 * self.end)
        self.hp      = self.max_hp
        self.xp_reward = xp_reward
        self.loot    = loot or {}
        self.special = special    # e.g. "poison"

    @property
    def damage(self):
        return self.str + random.randint(1, 4)

    @property
    def dodge_chance(self):
        return min(0.50, self.agi * 0.03)

    @property
    def hit_chance(self):
        return min(0.90, 0.45 + self.intel * 0.02 + self.spd * 0.01)

    def show(self):
        print(f"\n  Enemy: {self.name}")
        print(f"  HP  {bar(self.hp, self.max_hp)}")

# ─────────────────────────────────────────────
#  Enemy roster
# ─────────────────────────────────────────────

ENEMY_POOL = [
    lambda: Enemy("Zombie",         5,  6, 3, 2, 2, xp_reward=15, loot={"bandage": 0.3}),
    lambda: Enemy("Feral Dog",      7,  5, 7, 6, 3, xp_reward=20, loot={}),
    lambda: Enemy("Bandit",         8,  7, 6, 5, 6, xp_reward=30, loot={"medkit": 0.2, "bandage": 0.4}),
    lambda: Enemy("Toxic Crawler",  4,  4, 5, 4, 2, xp_reward=25, loot={}, special="poison"),
    lambda: Enemy("Raider",        10,  8, 7, 6, 7, xp_reward=40, loot={"medkit": 0.4}),
    lambda: Enemy("Zombie Brute",  12, 10, 2, 2, 1, xp_reward=50, loot={"bandage": 0.5}),
]

def random_enemy(day=1):
    """Later days unlock tougher enemies."""
    available = ENEMY_POOL[:max(2, min(len(ENEMY_POOL), 2 + day // 2))]
    factory   = random.choice(available)
    e         = factory()
    # Scale slightly with day
    scale = 1 + (day - 1) * 0.05
    for attr in ("str","end","agi","spd","intel"):
        setattr(e, attr, max(1, int(getattr(e, attr) * scale)))
    e.max_hp = (2 * e.str) + (3 * e.end)
    e.hp     = e.max_hp
    return e

# ─────────────────────────────────────────────
#  Combat
# ─────────────────────────────────────────────

def combat(player: Player, enemy: Enemy):
    slow_print(f"\n  ⚠  A {enemy.name} appears!")
    first_hit_perk = "Sprinter" in player.perks

    turn = 0
    while player.hp > 0 and enemy.hp > 0:
        turn += 1
        clear()
        player.show_stats()
        enemy.show()
        print()
        print("  Actions:")
        print("  [1] Attack")
        print("  [2] Use item")
        print("  [3] Try to flee")

        choice = input("\n  > ").strip()

        # ── Player turn ──────────────────────
        if choice == "1":
            guaranteed = first_hit_perk and turn == 1
            if guaranteed or random.random() < player.hit_chance:
                dmg = max(0, player.damage - random.randint(0, 2))  # minor enemy resistance
                enemy.hp -= dmg
                slow_print(f"\n  You hit the {enemy.name} for {dmg} damage!")
            else:
                slow_print(f"\n  You miss the {enemy.name}!")

        elif choice == "2":
            used = use_item(player)
            if not used:
                slow_print("  You rummage around but find nothing useful…")

        elif choice == "3":
            flee_chance = 0.30 + (player.effective_spd - enemy.spd) * 0.05
            if random.random() < max(0.05, flee_chance):
                slow_print("\n  You manage to escape!")
                return "fled"
            else:
                slow_print("\n  You couldn't get away!")
        else:
            slow_print("  Invalid action — you hesitate!")

        if enemy.hp <= 0:
            break

        # ── Enemy turn ───────────────────────
        if random.random() < (1 - player.dodge_chance):
            dmg = max(0, enemy.damage - player.effective_armor)
            # Glass Jaw trait
            if "Glass Jaw" in player.traits:
                dmg += 2
            player.hp -= dmg
            slow_print(f"  The {enemy.name} hits you for {dmg} damage!")
            if enemy.special == "poison" and random.random() < 0.40:
                dur = 3
                player.apply_status("poison", dur)
                slow_print(f"  You've been poisoned! ({dur} turns)")
        else:
            slow_print(f"  You dodge the {enemy.name}'s attack!")

        # ── Status ticks ─────────────────────
        for msg in player.tick_statuses():
            slow_print(msg)

        if player.hp <= 0:
            break

        input("\n  [Enter to continue]")

    # ── Outcome ──────────────────────────────
    if enemy.hp <= 0:
        slow_print(f"\n  ✔  You defeated the {enemy.name}!")
        player.kills += 1
        player.add_xp(enemy.xp_reward)
        roll_loot(player, enemy)
        return "victory"
    else:
        return "defeat"

# ─────────────────────────────────────────────
#  Items
# ─────────────────────────────────────────────

ITEMS = {
    "medkit":  {"desc": "Heals 30 HP.",  "heal": 30},
    "bandage": {"desc": "Heals 12 HP.",  "heal": 12},
}

def use_item(player: Player):
    usable = {k: v for k, v in player.inventory.items() if v > 0 and k in ITEMS}
    if not usable:
        return False
    print("\n  Inventory:")
    items = list(usable.items())
    for i, (name, count) in enumerate(items, 1):
        print(f"  [{i}] {name} x{count} — {ITEMS[name]['desc']}")
    print("  [0] Cancel")
    choice = input("  > ").strip()
    if choice == "0":
        return False
    try:
        idx   = int(choice) - 1
        name  = items[idx][0]
        healed = player.heal(ITEMS[name]["heal"])
        player.inventory[name] -= 1
        slow_print(f"  Used {name} — restored {healed} HP.")
        return True
    except (ValueError, IndexError):
        slow_print("  Nothing happened.")
        return False

def roll_loot(player: Player, enemy: Enemy):
    gained = []
    for item, chance in enemy.loot.items():
        if random.random() < chance:
            player.inventory[item] = player.inventory.get(item, 0) + 1
            gained.append(item)
    if gained:
        slow_print(f"  Loot: {', '.join(gained)}")

# ─────────────────────────────────────────────
#  Character creation
# ─────────────────────────────────────────────

def choose_traits(player: Player):
    slow_print("\n═══ Choose 2 Traits ═══")
    slow_print("Traits are permanent characteristics (mix of positive and negative).\n")
    trait_list = list(AVAILABLE_TRAITS.items())
    for i, (name, info) in enumerate(trait_list, 1):
        tag = "+" if info["type"] == "positive" else "-"
        print(f"  [{i}] ({tag}) {name}: {info['desc']}")

    chosen = []
    while len(chosen) < 2:
        raw = input(f"\n  Pick trait {len(chosen)+1}/2 (number): ").strip()
        try:
            idx = int(raw) - 1
            name = trait_list[idx][0]
            if name in chosen:
                slow_print("  Already chosen.")
            else:
                chosen.append(name)
                player.traits[name] = AVAILABLE_TRAITS[name]
                slow_print(f"  → {name} selected.")
        except (ValueError, IndexError):
            slow_print("  Invalid choice.")

def choose_perks(player: Player):
    slow_print("\n═══ Choose 1 Perk ═══")
    slow_print("Perks give special combat bonuses.\n")
    perk_list = list(AVAILABLE_PERKS.items())
    for i, (name, info) in enumerate(perk_list, 1):
        print(f"  [{i}] {name}: {info['desc']}")

    while True:
        raw = input("\n  Pick your perk (number): ").strip()
        try:
            idx  = int(raw) - 1
            name = perk_list[idx][0]
            player.perks[name] = AVAILABLE_PERKS[name]
            slow_print(f"  → {name} selected.")
            break
        except (ValueError, IndexError):
            slow_print("  Invalid choice.")

    # Apply immediate perk bonuses
    if "Tough" in player.perks:
        player.max_hp += player.perks["Tough"]["bonus"]["hp"]
        player.hp      = player.max_hp

# ─────────────────────────────────────────────
#  Camp (between combats)
# ─────────────────────────────────────────────

def camp_menu(player: Player):
    while True:
        clear()
        player.show_stats()
        print("\n  Camp actions:")
        print("  [1] Rest (recover HP, advance day)")
        print("  [2] Use item")
        print("  [3] Check inventory")
        print("  [4] Scavenge (risk encounter)")
        print("  [5] Continue travelling")
        choice = input("\n  > ").strip()

        if choice == "1":
            heal_amount = int(player.max_hp * 0.35)
            healed = player.heal(heal_amount)
            player.day += 1
            slow_print(f"\n  You rest. Recovered {healed} HP. Day {player.day} begins.")
            input("  [Enter]")

        elif choice == "2":
            use_item(player)
            input("  [Enter]")

        elif choice == "3":
            print("\n  Inventory:")
            if not player.inventory:
                print("  Empty.")
            for k, v in player.inventory.items():
                print(f"   {k} x{v}")
            input("  [Enter]")

        elif choice == "4":
            slow_print("\n  You head out to scavenge…")
            time.sleep(0.8)
            roll = random.random()
            if roll < 0.50:
                item = random.choice(["bandage", "medkit"])
                player.inventory[item] = player.inventory.get(item, 0) + 1
                slow_print(f"  Found a {item}!")
            elif roll < 0.80:
                slow_print("  Nothing useful around here.")
            else:
                slow_print("  Something stirs in the shadows…")
                enemy = random_enemy(player.day)
                result = combat(player, enemy)
                if result == "defeat":
                    return "defeat"
            input("  [Enter]")

        elif choice == "5":
            return "continue"

# ─────────────────────────────────────────────
#  Main game loop
# ─────────────────────────────────────────────

def main():
    clear()
    slow_print("╔══════════════════════════════════════╗")
    slow_print("║     DEAD WORLD — a CDDA-style game   ║")
    slow_print("╚══════════════════════════════════════╝\n")

    player = Player()
    name   = input("  Enter your survivor's name: ").strip()
    player.name = name or "Survivor"

    choose_traits(player)
    choose_perks(player)

    slow_print(f"\n  Good luck out there, {player.name}…")
    time.sleep(1.5)

    encounters_until_boss = 5

    for encounter in range(1, 21):   # 20-encounter run
        clear()
        player.show_stats()

        # Boss every 5 encounters
        if encounter % encounters_until_boss == 0:
            slow_print("\n  ⚡ A powerful enemy blocks your path!")
            boss = Enemy("Warlord", 14, 12, 8, 7, 9,
                         xp_reward=100,
                         loot={"medkit": 0.9, "bandage": 0.9})
            boss.max_hp = (2 * boss.str) + (3 * boss.end)
            boss.hp     = boss.max_hp
        else:
            boss = None

        enemy  = boss if boss else random_enemy(player.day)
        result = combat(player, enemy)

        if result == "defeat":
            clear()
            slow_print("\n  ✖  You have died.\n")
            slow_print(f"  Days survived : {player.day}")
            slow_print(f"  Kills         : {player.kills}")
            slow_print(f"  Level reached : {player.level}")
            break

        if result in ("victory", "fled"):
            camp_result = camp_menu(player)
            if camp_result == "defeat":
                clear()
                slow_print("\n  ✖  You have died.\n")
                slow_print(f"  Days survived : {player.day}")
                slow_print(f"  Kills         : {player.kills}")
                slow_print(f"  Level reached : {player.level}")
                break
    else:
        clear()
        slow_print("\n  ★  You survived the dead world.\n")
        slow_print(f"  Days survived : {player.day}")
        slow_print(f"  Kills         : {player.kills}")
        slow_print(f"  Level reached : {player.level}")

    input("\n  [Enter to quit]")


if __name__ == "__main__":
    main()