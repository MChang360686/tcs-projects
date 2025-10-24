import random
import math

map = [[1, 1, 0], [1, 1, 1], [0, 1, 1]]

chores = ['take out trash', 'make bed', 'wash dishes', 'put dishes away', 'clean room', 'defrost meat']
player_stats = {'str': 0, 'agi': 0, 'dex': 0, 'con': 0}

def d6():
    return random.randint(1, 6)
    
def move(current_position, destination):
    if map[current_position][destination] == 1:
        return True
    else:
        return False
        
def skill_check(stat):
    bonus = player_stats[stat]
    if d6() + bonus >= 3:
        return True
    else:
        return False
    
def help():
    print("Goal: do your chores before mom gets back.\n\nCOMMANDS\nmove - attempts to move to a different room\nchore - attempts to perform a chore and starts skill check\nlist - describes chores to be done in this room.  Doesn\'t cost time.\nhelp - displays game rules.  Doesn\'t cost time.\n")
        
def game():
    
    for _ in range(5):
        choice = input('Enter a stat to allot a point to (str, agi, dex, con): ')
        player_stats[choice] += 1

    print(player_stats)
        
    time = 60 * int(input('enter a difficulty level (1-3)'))
    current_position = 0
    
    while time > 0:
        print('Time remaining: ' + str(time))
        cmd = input('Choose an action(move, chore, list, help): ')
        if cmd == 'help':
            help()
        elif cmd == 'move':
            new_room = int(input('Enter the room you want to move to(0-2) '))
            if move(current_position, new_room):
                time -= 5
                current_position = new_room
            else:
                time -= 10
                print('Invalid move. Time lost. ')
        elif cmd == 'list':
            if current_position == 0:
                print('make bed', 'clean room')
            elif current_position == 1:
                print('n/a')
            else:
                print('take out trash', 'wash dishes', 'put dishes away', 'defrost meat')
        elif cmd == 'chore':
            chore_name = input('enter name of chore you wish to do ')
            match chore_name:
                case 'take out trash' if current_position == 2:
                    if skill_check('str'):
                        print('chore successful')
                        chores.remove('take out trash')
                        time -= math.floor(5/player_stats['str'])
                    else:
                        print('chore unsuccessful')
                        time -= math.floor(5/player_stats['str'])
                case 'wash dishes' | 'put dishes away' if current_position == 2:
                    if skill_check('dex'):
                        print('chore successful')
                        chores.remove(chore_name)
                        time -= math.floor(10/player_stats['dex'])
                    else:
                        print('chore unsuccessful')
                        time -= math.floor(10/player_stats['dex'])
                case 'make bed' if current_position == 0:
                    if skill_check('agi'):
                        print('chore successful')
                        chores.remove('make bed')
                        time -= math.floor(5/player_stats['agi'])
                    else:
                        print('chore unsuccessful')
                        time -= math.floor(5/player_stats['agi'])
                case 'clean room' if current_position == 0:
                    if skill_check('agi'):
                        print('chore successful')
                        chores.remove('clean room')
                        time -= math.floor(5/player_stats['agi'])
                    else:
                        print('chore unsuccessful')
                        time -= math.floor(5/player_stats['agi'])
                case 'defrost meat' if current_position == 2:
                    if skill_check('con'):
                        print('chore successful')
                        chores.remove('defrost meat')
                        time -= math.floor(5/player_stats['con'])
                    else:
                        print('chore unsuccessful')
                        time -= math.floor(5/player_stats['con'])
                case _:
                    print('Unknown chore name.  Time lost. ')
                    time -= 5

        else:
            time -= 10
            print('Invalid command.  Time lost. ')

        if len(chores) < 1:
            print('you win')
            break

    if len(chores) > 0:
        print('you lose')
    else:
        print('you win')
game()
    