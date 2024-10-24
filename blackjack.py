import random

cards = {'a': 1, '2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, '10': 10, \
         'j': 10, 'q': 10, 'k': 10}

bank = {'player': 10000, 'dealer': 50000}

def deal_card():
    return random.choice(list(cards))

def sum_cards(list):
    card_total = 0
    for item in list:
        card_total += cards[item]
    return card_total

def game():

    while bank['player'] > -2000 and bank['dealer'] > 0:
        player_bust = False
        dealer_bust = False

        player_hand = []
        player_hand.append(deal_card())
        player_hand.append(deal_card())

        dealer_hand = []
        dealer_hand.append(deal_card())
        dealer_hand.append(deal_card())

        while player_bust is not True or dealer_bust is not True:
            print(f'Player hand: {sum_cards(player_hand)}')
            print(f'Dealer hand: {sum_cards(dealer_hand)}')

            player_action = input("hit or stay?")

            if player_action == 'hit':
                player_hand.append(deal_card())
                
                if sum_cards(player_hand) > 21:
                    print(f'Player bust {sum_cards(player_hand)}')
                    player_bust = True
                    print()
                    break
                else:
                    print(f'Player has: {sum_cards(player_hand)}')
            elif player_action == 'stay':
                pass
            else:
                print("I don't understand that command")

            if sum_cards(dealer_hand) < 17:
                dealer_hand.append(deal_card())
                if sum_cards(dealer_hand) > 21:
                    print(f'Dealer bust {dealer_hand}')
                    dealer_bust = True
                    print()
                    break
                else:
                    print(f'Dealer has: {sum_cards(dealer_hand)}')
           
game()
'''print(deal_card())
print(cards[deal_card()])'''