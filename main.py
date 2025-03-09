import time
import os
import random

os.system('cls||clear')
time.sleep(0.5)
print((10*'-')+"BlackJack"+(10*'-'))
time.sleep(1.5)

balance = 100
print(f"your balance is {balance}$")
time.sleep(1.5)
os.system('cls||clear')

deck_num = int(input("How many decks of cards do you want to play with?\n"))
cards = []
suit_signs = ['♠', '♥', '♣', '♦']

for suit in suit_signs:
    cards.append("A"+suit)

for i in range(2, 11):
    for suit in suit_signs:
        cards.append(str(i)+suit)

for face in ['J', 'Q', 'K']:
    for suit in suit_signs:
        cards.append(face+suit)

cards_in_game = cards * deck_num

def print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet):
    print(f"""____________________   Balance: {balance}$
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

def draw_card(cards_in_game):
    card = cards_in_game.pop(random.randint(0, len(cards_in_game)-1))
    if card[0] == 'A':
        return card, 11 
    elif card[0] in ['J', 'Q', 'K']:
        return card, 10
    elif len(card) == 3:
        return card, 10
    else:
        return card, int(card[0])

os.system('cls||clear')

while balance > 0:
    dealer_cards = []
    player_cards = []
    dealer_cards_num = 0
    player_cards_num = 0
    player_cards_num_A = 0
    dealer_cards_num_A = 0

    print_table(balance, '', '', '', '', '')
    bet = int(input("Please Put Your Bet!!!\n"))
    balance -= bet
    os.system('cls||clear')

    card, value = draw_card(cards_in_game)
    player_cards.append(card)
    player_cards_num += value
    if card[0] == 'A':
        player_cards_num_A += 1
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
    time.sleep(2)
    os.system('cls||clear')

    card, value = draw_card(cards_in_game)
    dealer_cards.append(card)
    dealer_cards_num += value
    if card[0] == 'A':
        dealer_cards_num_A += 1
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
    time.sleep(2)
    os.system('cls||clear')

    card, value = draw_card(cards_in_game)
    player_cards.append(card)
    player_cards_num += value
    if card[0] == 'A':
        player_cards_num_A += 1
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
    time.sleep(2)
    os.system('cls||clear')

    card, value = draw_card(cards_in_game)
    dealer_cards.append(card)
    dealer_cards_num += value
    if card[0] == 'A':
        dealer_cards_num_A += 1
    print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
    time.sleep(2)

    if player_cards_num > 21 and player_cards_num_A > 0:
        player_cards_num -= 10
        player_cards_num_A -= 1
        os.system('cls||clear')
        print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
        time.sleep(2)

    if dealer_cards_num > 21 and dealer_cards_num_A > 0:
        dealer_cards_num -= 10
        dealer_cards_num_A -= 1
        os.system('cls||clear')
        print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
        time.sleep(2)

    if dealer_cards_num == 21 and player_cards_num == 21:
        print("--DRAW--")
        balance += bet
        time.sleep(2)
        os.system('cls||clear')
        continue
    elif dealer_cards_num == 21:
        print("--YOU LOST--")
        time.sleep(2)
        os.system('cls||clear')
        continue

    while True:
        choice = input("Hit or Stand? (h/s): ").lower()
        os.system('cls||clear')

        if choice == 'h':
            card, value = draw_card(cards_in_game)
            player_cards.append(card)
            player_cards_num += value
            if card[0] == 'A':
                player_cards_num_A += 1

            while player_cards_num > 21 and player_cards_num_A > 0:
                player_cards_num -= 10
                player_cards_num_A -= 1

            print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
            time.sleep(2)

            if player_cards_num > 21:
                print("--BUSTED--")
                print(f"--YOU LOST {bet}$")
                time.sleep(2)
                os.system('cls||clear')
                break
        else:
            break

    while dealer_cards_num < 17:
        card, value = draw_card(cards_in_game)
        dealer_cards.append(card)
        dealer_cards_num += value
        if card[0] == 'A':
            dealer_cards_num_A += 1

        while dealer_cards_num > 21 and dealer_cards_num_A > 0:
            dealer_cards_num -= 10
            dealer_cards_num_A -= 1

        print_table(balance, dealer_cards, dealer_cards_num, player_cards, player_cards_num, bet)
        time.sleep(2)
        os.system('cls||clear')

    if dealer_cards_num > 21:
        print("--DEALER BUSTED--")
        print(f"--YOU WON {bet}$--")
        balance += (bet*2)
        time.sleep(2)
        os.system('cls||clear')
    elif dealer_cards_num < player_cards_num:
        print(f"--YOU WON {bet}$--")
        balance += (bet*2)
        time.sleep(2)
        os.system('cls||clear')
    elif dealer_cards_num == player_cards_num:
        print("--DRAW--")
        balance += bet
        time.sleep(2)
        os.system('cls||clear')
    else:
        print("--YOU LOST--")

    time.sleep(2)
    os.system('cls||clear')