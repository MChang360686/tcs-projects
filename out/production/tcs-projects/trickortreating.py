import random
import math

def d100():
    return random.randint(1, 100)

def d6():
    return random.randint(1, 6)

def candy(num_candies):
    return random.choices(['lollipop', 'chocolate', 'candy corn'], weights=(50, 30, 20), k=num_candies)

def weather():
    return random.choice(['clear', 'cloudy', 'rainy', 'foggy'])

def encounters():
    return random.choices(['find candy', 'cat', 'car'], weights=(60, 30, 10), k=1)

def set_time(diff):
    return 180 / diff

def build_map():
    return [ i for i in range(30) ]

def game():
    time = set_time(int(input('Enter a difficulty level(1-3): ')))
    w = weather()
    map = build_map()
    delay = 5
    bonus_modifier = 1
    candy_received = {'lollipop': 0, 'chocolate': 0, 'candy corn': 0}

    for i in range(3):
        if input('The weather is '+ w + '. Do you want to wait to see if things change? (y/n) ') == 'y':
            w = weather()
            print('you have ' + str(3 - i) + ' waits left')
            time -= 15
        else:
            break

    if w == 'cloudy':
        delay += 2
        bonus_modifier = 1.15
    elif w == 'rainy':
        delay += 3
        bonus_modifier = 1.25
    elif w == 'foggy':
        delay += 4
        bonus_modifier = 1.5

    while time > 0:
        if map[int(input("Enter a location(0-29): "))] != 'X':
            for piece in candy(math.ceil(d6() * bonus_modifier)):
                print('You got a ' + piece)
                candy_received[piece] += 1
            time -= delay
                
        else:
            print('Location already visited')
            time -= delay

        if d6() <= 3:
            random_event = encounters()
            if random_event[0] == 'find candy':
                for piece in candy(d6()):
                    candy_received[piece] += 1
            elif random_event[0] == 'cat':
                print('You see a cat ')
                continue
            else:
                print('You got hit by a car.  Trick or Treating is over, go home. ')
                time = 0
                break

    print('You got the following candy')
    print(candy_received)

game()
