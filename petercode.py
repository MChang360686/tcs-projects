import random

good_vaca = []
bad_vaca = []

def vacation():
    if input('Do you want a reccommendation(0) or to reccomend a vacation(1)? ') == '0':
        if len(good_vaca) == 0:
            print('I have no places to reccomend.  Come back later.')
        else:
            print(f'I reccomend you visit {good_vaca[random.randint(0, len(good_vaca) - 1)]}')
    else:
        location = input('Where would you like to reccomend? ')
        if input('Was it a good vacation(y/n)? ') == 'y':
            good_vaca.append(location)
        else:
            print('Sorry to hear that, location has been added to bad vacations')
            bad_vaca.append(location)
    
while True:            
    vacation()
