from deck import Deck
from player import Player
from time import sleep

dealer_wins = 0
player_wins = 0

class Game():
    def __init__(self):
        self.deck = Deck()
        self.p1 = Player("Player")
        self.dealer = Player("Dealer")

    
    def start_game(self):
        print("Shuffling deck...")
        self.deck.shuffle()
        self.p1.hand.add_card(self.deck.deal()) # p1 deal
        self.dealer.hand.add_card(self.deck.deal()) #dealer deal
        self.p1.hand.add_card(self.deck.deal())
        self.dealer.hand.add_card(self.deck.deal())


    def player_turn(self):
        global dealer_wins, player_wins
        print(f"Players hand: {self.p1.hand.calc_value()}")
        print(f"Dealers first card: {self.dealer.hand.show_first_card()}")
        while True:
            if self.p1.hand.calc_value() < 21:
                choice = input("Hit or stand? (h/s): ").lower()
                if choice == "h":
                    self.p1.hand.add_card(self.deck.deal())
                    print(f"Players hand: {self.p1.hand.calc_value()}")
                elif choice == "s":
                    self.dealer_turn()
                    break
            elif self.p1.hand.calc_value() == 21 and len(self.p1.hand.hand) == 2:
                sleep(1.5)
                print("Blackjack: 21!")
                self.dealer_turn()
                break
            elif self.p1.hand.calc_value() == 21:
                self.dealer_turn()
                break
            else:
                sleep(1)
                print("Player bust...")
                sleep(1)
                print("Dealer wins...")
                dealer_wins += 1
                break
        sleep(2)

    def dealer_turn(self):
        global dealer_wins, player_wins
        if self.p1.hand.calc_value() <= 21:
            print(f"Players hand: {self.p1.hand.calc_value()}, against dealers hand: {self.dealer.hand.calc_value()}")
            while self.dealer.hand.calc_value() < 17:
                sleep(2)
                self.dealer.hand.add_card(self.deck.deal())
                print(f"Dealers hand: {self.dealer.hand.calc_value()}")
            if self.dealer.hand.calc_value() > 21:
                sleep(1)
                print("Dealer bust!")
                sleep(1)
                print("Player wins!")
                player_wins += 1
            else:
                self.check_winner()
                
    def check_winner(self):
        global dealer_wins, player_wins
        if self.p1.hand.calc_value() > self.dealer.hand.calc_value():
            print("Player wins!")
            player_wins += 1
        elif self.p1.hand.calc_value() == 21 and len(self.p1.hand.hand) == 2 and self.p1.hand.calc_value() < self.dealer.hand.calc_value():
            print("Player wins!")   
            print("Payout 3:1!")
            player_wins += 1
        elif self.p1.hand.calc_value() < self.dealer.hand.calc_value():
            print("Dealer wins...")
            dealer_wins += 1
        else:
            print("Push.")

    def play(self):
        self.p1.hand.reset()
        self.start_game()
        self.player_turn()

    def check_wins(self):
        global dealer_wins, player_wins
        print(f"Player wins: {player_wins}")
        print(f"Dealer wins: {dealer_wins}")
        
while True:
    sleep(1.5)
    game = Game()
    game.play()
    choice = input("Keep playing? (y/n): ").lower()
    if choice == 'n':
        break
    elif choice == 'wins':
        game.check_wins()