from funcs.generate_cards import generate_cards
from objs.card import Card


class Deck:

    SUITS = ["Spades","Hearts","Clubs","Diamonds"]
    RANKS = generate_cards()

    def __init__(self):

        self.deck = [Card(s,r) for s in self.SUITS for r in self.RANKS]


deck1 = Deck()
print(len(deck1.deck))
