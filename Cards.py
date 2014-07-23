import random

class Deck:
    def __init__(self):
        # init variables
        self.cards = []
        self.numCards = 0

        # init methods
        self.populate_cards()

        def deal(self):
            return self.cards.pop(random.randint(0, (self.numCards - 1)))

        def populate_cards(self):
            for suit in range (0, 5):
                for face in range (0, 13):
                    card = Card(face, suit)
                    self.cards.append(card)
                    self.numCards = self.numCards + 1	

        def cards_left(self):
            print (self.numCards)

class Card:
    def __init__(self, face = 0, suit = 0):
        self.face = face
        self.suit = suit

    def assign_value_using_face(self):
        pass

class BlackjackCard(Card):
    def __init__(self, face = 0, suit = 0):
        super().__init__(self, face, suit)
        self.value = None  

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
