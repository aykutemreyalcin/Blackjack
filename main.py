import time
import os
import random
#int(cards[0][:2])
#int(cards[0][:1])
print((10*'-')+"BlackJack"+(10*'-'))
time.sleep(.5)

balance = 100
print(f"your balace is {balance}$")
time.sleep(.5)
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

for i in table:
    print(i)

def print_table(balance, dealer_cards,dealer_cards_num, player_cards, player_cards_num, bet):
    print(f"""____________________   balance: {balance}$
|                  |
|   {dealer_cards}{dealer_cards_num}               
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|                  |
|   {player_cards}{player_cards_num}          {bet}$  
____________________""")
    
def print_table_A(balance, dealer_cards,dealer_cards_num, player_cards, player_cards_num, bet):
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
|   {player_cards}  {player_cards_num}/{player_cards_num_A}         {bet}$  
____________________""")

print(cards_in_game)
#2 11
print_table(100,1,1,1,1,1)
#while balance > 0:
dealer_cards = []
player_cards = []
dealer_cards_num = 0
player_cards_num = 0
player_cards_num_A = 0

while balance > 0:
    player_cards.append(cards_in_game.pop(random.randint(0, (len(cards_in_game)-1))))
    if player_cards[0][0] == 'A':
        player_cards_num += 11
        player_cards_num_A += 1
    elif len(player_cards[0]) == 3:
        player_cards_num += int(player_cards[0][:2])
    else:
        player_cards_num += int(player_cards[0][:2])
