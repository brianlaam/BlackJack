# Blackjack Game

This is a simple terminal-based Blackjack game written in Python.

## How to Play

- The game will start by asking how much you want to bet. Enter a number. 
- You and the dealer will each be dealt 2 cards. Your cards will be shown, while only one of the dealer's cards will be visible.
- If your initial hand value is less than 15, you will automatically be dealt another card.
- You can choose to 'Hit' to get another card or 'Stand' to stop drawing cards.
- Getting 21 points with your first 2 cards is a Blackjack. This pays out 1.5x your bet. 
- Going over 21 points is a bust and you lose your bet.
- After you stand, the dealer will draw cards until they have at least 17 points. 
- If you have more points than the dealer without busting, you win.
- Equal points result in a push (tie) and you get your bet back.

There are also some special hands:

- Dragon: Having 5 cards totaling 20 or less points pays 3x your bet. 
- Straight: Having 3 cards in a row (like 4,5,6) pays 10x your bet.
- Straight Flush: Having 3 suited cards in a row pays 40x your bet.

The game will track stats like your total wins, losses, current balance, etc.

## Requirements

- Python 3
- random 
- time

## License

This project is licensed under the MIT License - see the LICENSE file for details.
