import random
from card_class import Card, suits, ranks

# DECK
class Deck:
    
    def __init__(self):
        # This only happens once upon creation of a new Deck
        self.all_cards = [] 
        for suit in suits:
            for rank in ranks:
                # This assumes the Card class has already been defined!
                self.all_cards.append(Card(suit, rank))
                
    def shuffle(self):
        # This doesn't return anything
        random.shuffle(self.all_cards)
        
    def deal_one(self):
        # We remove one card from the list of all_cards
        return self.all_cards.pop()
