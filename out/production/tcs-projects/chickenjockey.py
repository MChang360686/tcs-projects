class Chicken:
    
    def make_sound(self):
        print('bok bok bok')
        
class Zombie:
    
    def make_sound(self):
        print('Braaaaaaiiinnns')
        

def chicken_jockey():
    points = 0
    endpoint = int(input('Please enter a number to go up to '))
    
    chicken = Chicken()
    child_zombie = Zombie()
    
    for i in range(0, endpoint):
        print(i)
        player_ans = input('Enter chicken, jockey, chickenjockey, or nothing ')
        
        if i % 5 == 0 and i % 3 == 0:
            if player_ans == 'chickenjockey':
                chicken.make_sound()
                child_zombie.make_sound()
                points += 1
            else:
                continue
        elif i % 3 == 0:
            if player_ans == 'chicken':
                chicken.make_sound()
                points += 1
            else:
                continue
        elif i % 5 == 0:
            if player_ans == 'jockey':
                child_zombie.make_sound()
                points += 1
            else:
                continue
        
    return 'You earned ' + str(points) + ' points total'

print(chicken_jockey())