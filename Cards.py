import random

class Deck:
    def __init__(self):
        self.cards = []
        self.populate_cards()
        self.shuffle()

    def deal(self):
        return self.cards.pop(0)

    def shuffle(self):
        random.shuffle(self.cards)

    def populate_cards(self):
        for suit in range (1, 5):
            for face in range (1, 14):
                card = Card(face, suit)
                self.cards.append(card)

    def cards_left(self):
        print (len(self.cards))

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit

class Suit:
    Diamond = 1
    Club = 2
    Heart = 3
    Spade = 4

class Face:
    Ace = 1
    Two = 2
    Three = 3
    Four = 4
    Five = 5
    Six = 6
    Seven = 7
    Eight = 8
    Nine = 9
    Ten = 10
    Jack = 11
    Queen = 12
    King = 13
