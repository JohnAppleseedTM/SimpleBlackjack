# Simple Blackjack 🃏

A straightforward console-based Blackjack game written in Python. No fluff — just you vs. the dealer.

## Gameplay

The game follows standard Blackjack rules:

- You and the dealer are each dealt two cards
- You can **Hit** (draw a card) or **Stand** (end your turn)
- The dealer must hit until reaching 17 or higher
- Closest to 21 without going over wins
- Going over 21 is a **bust** — instant loss

## Rules & Limitations

This is a simplified version of Blackjack. The following are **not** included:

- No betting or balance system
- No splitting pairs
- No doubling down
- No insurance

Aces count as 11 or 1 (whichever keeps you under 22).

## Requirements

- Python 3.x

## How to Run

```bash
git clone https://github.com/JohnAppleseedTM/SimpleBlackjack.git
cd SimpleBlackjack
python blackjack.py
```

## Project Structure

```
SimpleBlackjack/
└── game.py   # Main game file
```

## License

This project is open source and free to use.
