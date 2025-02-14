import random
import math
import time

upgrade_cost = {'click_power': 10, 'grandma': 100, 'factory': 5000}
upgrades_owned = {'click_power': 1, 'grandma': 0, 'factory': 0}

def click(cookies_owned, cookies_per_click, cookies_per_second, time_since_last_click):
    curr_time = int(time.perf_counter())
    cookies_owned += (cookies_per_click + (cookies_per_second * int(curr_time - time_since_last_click)))
    return cookies_owned

def buy(cookies_owned, upgrade_name):
    if cookies_owned >= upgrade_cost[upgrade_name]:
        cookies_owned -= upgrade_cost[upgrade_name]
        upgrades_owned[upgrade_name] += 1
        return upgrade_name + " purchased!"
    else:
        return "Not enough cookies"
    
def calc_click_power():
    return (upgrades_owned['click_power'] + (upgrades_owned['grandma'] * 5) + (upgrades_owned['factory'] * 50))

def shop(cookies):
    print(upgrade_cost)

    cmd = input("What would you like to buy?  Press enter to exit ")

    if cmd == 'click_power':
        print(buy(cookies, 'click_power'))
    elif cmd == 'grandma':
        print(buy(cookies, 'grandma'))
    elif cmd == 'factory':
        print(buy(cookies, 'factory'))
    else:
        return   
    
def main():
    c = 0
    cpc = calc_click_power()
    cps = 1
    time_since_last_click = int(time.perf_counter())

    while True:
        cmd = input("Press enter to click ")

        if cmd == 'shop':
            shop(c)
            cpc = calc_click_power()
        elif cmd == 'help':
            print("Type 'shop' to buy upgrades")
            print("Type 'help' to see this message again")
        else:
            c = click(c, cpc, cps, time_since_last_click)
            print('You have ' + str(c) + ' cookies')
            print('you gain ' + str(cpc) + ' cookies per click')
            print('you gain ' + str(cps) + ' cookies per second')

main()
        