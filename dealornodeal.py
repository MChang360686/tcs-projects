import random

def make_briefcases(list):
    list.append(0.01)
    list.append(1)
    list.append(5)
    list.append(10)
    for i in range(25, 125, 25):
        list.append(i)
    for i in range(200, 500, 100):
        list.append(i)
    for i in range(500, 1250, 250):
        list.append(i)
    list.append(5000)
    list.append(10000)
    for i in range(25000, 125000, 25000):
        list.append(i)
    for i in range(200000, 600000, 100000):
        list.append(i)
    list.append(750000)
    list.append(1000000)
    random.shuffle(list)
    return list

def game():
    briefcases = make_briefcases([])
    eliminated_briefcases = []
    b = int(input("Enter a briefcase number to choose(0-25): "))
    briefcase = briefcases[b]
    
    for i in range(0, 4):
        for j in range(0, 6):
            temp = int(input("Enter a briefcase number(0-25): "))
            if temp == b:
                print("That is your briefcase")
            else:
                print(briefcases[temp])
                eliminated_briefcases.append(briefcases[temp])
                
        offer = (i * 1000) + random.randint(0, 2000)
        if input("The Banker offers you " + str(offer) + "(y/n): ") == 'y':
            print("Final Score: " + str(offer))
            print(briefcase)
            return
        else:
            continue
        
    if input("There is one briefcase left.  Would you like to switch? (y/n): ") == 'y':
        for case in eliminated_briefcases:
            briefcases.remove(case)
        print("You had: briefcase# " + str(b) + " with " + str(briefcase) + " dollars")
        briefcases.remove(briefcase)
        print("You switched to: " + str(briefcases[0]))
    else:
       print('You kept your briefcase with ' + str(briefcase) + ' dollars')
    
game()