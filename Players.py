# Player info

class Player:
    def __init__(self):
        self.hand = {}
        self.score = 0
        self.stay = 0

    def hit(self, deck):
        self.hand.append(deck.deal)

    def stay(self, deck):
        self.stay = 1

class Dealer(Player):
    def __init__(self):
        self.hand = {}
        self.score = 0

    def hit(self):  # hit is automatic for Dealer 
