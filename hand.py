from deck import Deck
from card import Card

class Hand():
    def __init__(self):
        self.hand = []
        self.player_value = 0

    def add_card(self, card):
        self.hand.append(card)

    def show_first_card(self):
        if self.hand[0].rank > 9:
            return 10
        elif self.hand[0].rank == 1:
            return 11
        else:
            return self.hand[0].rank

    def calc_value(self):
        for card in self.hand:
            if card.rank > 9:
                self.player_value += 10
            elif card.rank == 1:
                if self.player_value + 11 > 21:
                    self.player_value += 1
                else:
                    self.player_value += 11
            else:
                self.player_value += card.rank
        current_value = self.player_value
        self.player_value = 0
        return current_value
    
    def reset(self):
        self.hand = []
        self.player_value = 0
