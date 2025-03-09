import time
import os
import random
#int(cards[0][:2])
#int(cards[0][:1])
os.system('cls||clear')
time.sleep(0.5)
print((10*'-')+"BlackJack"+(10*'-'))
time.sleep(1.5)

balance = 100
print(f"your balace is {balance}$")
time.sleep(1.5)
os.system('cls||clear')

deck_num = int(input("how many deck of cards do you want to play with?\n"))
table = []
table.append(20*'_'+15*' '+str(balance)+'$')
for i in range(1,12):
    temp_string = ''
    temp_string += ('|')
    temp_string += (18*' ')
    temp_string += ('|')
    table.append(temp_string)
table.append(20*'_')

cards = []
suit_signs = ['♠', '♥', '♣', '♦']

for i in suit_signs:
    cards.append("A"+i)
    
for i in range(2, 11):
    for j in suit_signs:
        cards.append(str(i)+j)

for i in ['J', 'Q', 'K']:
    for j in suit_signs:
        cards.append(i+j)

cards_in_game = []
for i in range(0, deck_num):
    for j in cards:
        cards_in_game.append(j)

def print_table(balance, dealer_cards,dealer_cards_num, player_cards, player_cards_num, bet):
    print(f"""____________________   balance: {balance}$
|                  |
|   {dealer_cards}  {dealer_cards_num}              
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|   {player_cards}  {player_cards_num}         {bet}$  
____________________""")

os.system('cls||clear')

while balance > 0:

    dealer_cards = []
    player_cards = []
    dealer_cards_num = 0
    player_cards_num = 0
    player_cards_num_A = 0
    dealer_cards_num_A = 0

    print_table(balance,'','','','','')
    bet = int(input("Please Put Your Bet!!!\n"))
    balance -= bet
    os.system('cls||clear')
    print_table(balance,'','','','',bet)
    time.sleep(1.5)
    os.system('cls||clear')

    player_cards.append(cards_in_game.pop(random.randint(0, (len(cards_in_game)-1))))
    if player_cards[0][0] == 'A':
        player_cards_num += 11
        player_cards_num_A += 1
    elif player_cards[0][0] == 'J' or player_cards[0][0] == 'Q' or player_cards[0][0] == 'K':
        player_cards_num += 10
    elif len(player_cards[0]) == 3:
        player_cards_num += int(player_cards[0][:2])
    else:
        player_cards_num += int(player_cards[0][:1])
    
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
    time.sleep(1.5)
    os.system('cls||clear')

    dealer_cards.append(cards_in_game.pop(random.randint(0, (len(cards_in_game)-1))))
    if dealer_cards[0][0] == 'A':
        dealer_cards_num += 11
        dealer_cards_num_A += 1
    elif dealer_cards[0][0] == 'J' or dealer_cards[0][0] == 'Q' or dealer_cards[0][0] == 'K':
        dealer_cards_num += 10
    elif len(dealer_cards[0]) == 3:
        dealer_cards_num += int(dealer_cards[0][:2])
    else:
        dealer_cards_num += int(dealer_cards[0][:1])
    
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)

    time.sleep(1.5)
    os.system('cls||clear')

    player_cards.append(cards_in_game.pop(random.randint(0, (len(cards_in_game)-1))))
    if player_cards[1][0] == 'A':
        player_cards_num += 11
        player_cards_num_A += 1
    elif player_cards [1][0] == 'J' or player_cards [1][0] == 'Q' or player_cards [1][0] == 'K':
        player_cards_num += 10
    elif len(player_cards[1]) == 3:
        player_cards_num += int(player_cards[1][:2])
    else:
        player_cards_num += int(player_cards[1][:1])

    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
    time.sleep(1.5)
    os.system('cls||clear')
    
    dealer_cards.append(cards_in_game.pop(random.randint(0, (len(cards_in_game)-1))))
    if dealer_cards[1][0] == 'A':
        dealer_cards_num += 11
        dealer_cards_num_A += 1
    elif dealer_cards[1][0] == 'J' or dealer_cards[1][0] == 'Q' or dealer_cards[1][0] == 'K':
        dealer_cards_num += 10
    elif len(dealer_cards[1]) == 3:
        dealer_cards_num += int(dealer_cards[1][:2])
    else:
        dealer_cards_num += int(dealer_cards[1][:1])
    
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)

    time.sleep(2)

    if dealer_cards_num == 21 and player_cards_num == 21:
        print("--DRAW--")
        balance += bet
    elif dealer_cards_num == 21:
        print("--YOU LOST--")
    continue


