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

class Card:
    def __init__(self, face, suit):
        self.face = face
        self.suit = suit
        self.face_name = None
        self.suit_name = None
        self.translate_face_to_name()
        self.translate_suit_to_name()

    def translate_face_to_name(self):
        if self.face == 1:
           self.face_name = "ace"
        elif self.face == 2:
           self.face_name = "two"
        elif self.face == 3:
           self.face_name = "three"
        elif self.face == 4:
           self.face_name = "four"
        elif self.face == 5:
           self.face_name = "five"
        elif self.face == 6:
           self.face_name = "six"
        elif self.face == 7:
           self.face_name = "seven"
        elif self.face == 8:
           self.face_name = "eight"
        elif self.face == 9:
           self.face_name = "nine"
        elif self.face == 10:
           self.face_name = "ten"
        elif self.face == 11:
           self.face_name = "jack"
        elif self.face == 12:
           self.face_name = "queen"
        elif self.face == 13:
           self.face_name = "king"

    def translate_suit_to_name(self):
       if self.suit == Suit.Diamond:
           self.suit_name = "diamond"
       elif self.suit == Suit.Club:
           self.suit_name = "club"
       elif self.suit == Suit.Heart:
           self.suit_name = "heart"
       elif self.suit == Suit.Spade:
           self.suit_name = "spade"

class Suit:
    Diamond = 1
    Club = 2
    Heart = 3
    Spade = 4
