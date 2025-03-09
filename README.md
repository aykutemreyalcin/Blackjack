# Blackjack Game

A simple command-line Blackjack game implemented in Python. The game follows standard Blackjack rules where the player competes against the dealer.

## Features
- Multiple deck support
- Hit or Stand gameplay
- Dealer follows Blackjack rules (hits until 17 or higher)
- Ace value adjustments (11 or 1) to prevent busting
- Automatic game progression with balance tracking

## How to Play
1. Run the script in a Python environment.
2. Choose the number of decks to play with.
3. Place your bet.
4. Receive two initial cards while the dealer also gets two cards (one hidden).
5. Choose whether to "Hit" (draw another card) or "Stand" (end your turn).
6. The dealer will then reveal their hand and draw cards if needed.
7. The result will be displayed based on standard Blackjack rules.

## Installation
### Requirements:
- Python 3.x

### Steps:
1. Clone this repository:
   ```sh
   git clone https://github.com/your-repo/blackjack-game.git
   ```
2. Navigate to the project directory:
   ```sh
   cd blackjack-game
   ```
3. Run the script:
   ```sh
   python blackjack.py
   ```

## Game Rules
- The goal is to get as close to 21 without exceeding it.
- Face cards (J, Q, K) are worth 10 points.
- Aces can be worth 11 or 1, depending on what benefits the player.
- The dealer must draw until they reach at least 17.
- If both the dealer and the player have the same score, it's a draw.
- If the player busts (exceeds 21), they lose immediately.
- If the dealer busts, the player wins.

## Future Enhancements
- Implement betting strategies
- Add a GUI version
- Introduce multiplayer support

## Author
Aykut - Aykutemreyalcin

