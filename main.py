import time
import os
#int(cards[0][:2])
#int(cards[0][:1])
print((10*'-')+"BlackJack"+(10*'-'))
time.sleep(1)

balance = 100
print(f"your balace is {balance}$")
time.sleep(1)
os.system('cls||clear')

table = []
table.append(20*'_')
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
