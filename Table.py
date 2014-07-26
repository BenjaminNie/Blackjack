from Cards import *
from Players import *

class Game:
    def __init__(self, num_players):

        # varibles
        self.dealer = BlackjackDealer()
        self.players = {}
        self.deck = Deck()
        self.num_players = num_players 

        # methods
        self.start_game()

    def add_player(self, name):
        self.players[name] = BlackjackPlayer(name)

    def remove_player(self, name):
        del self.players[name]

    def start_game(self):
        print "Welcome to Ben's Blackjack game"
        print "How many players will be playing today?"
        self.num_players = int(raw_input())

        # create players
        self.create_players()

        # initial deal
        self.initial_deal()

    def create_players(self):
        i = 1
        while (i <= self.num_players):
           print "What is player " + i + "'s name?"
           name = raw_input()
           self.players.append(BlackjackPlayer(name))
 
    def initial_deal(self):
        self.dealer.initial_deal(self.deck)

        for player in self.players:
            player.hit(self.deck)
            player.hit(self.deck)


# main function begins    
while (1):
    print "Welcome to Ben's Blackjack game"
    print "How many players will be playing today?"
    num_players = raw_input()

    game = Game()
