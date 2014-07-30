from Cards import *
from Players import *

class Game:
    def __init__(self):

        # varibles
        self.dealer = BlackjackDealer()
        self.players = []
        self.deck = Deck()
        self.state = GameState.Active
        self.highest_score = 0

        # methods
        self.start_game()

        if self.state == GameState.Active:
            self.players_turn()
            self.dealers_turn()

        self.calculate_score()

    def add_player(self, name):
        self.players.append(BlackjackPlayer(name))

    def start_game(self):
        print "Welcome to Ben's Blackjack game"
        num_players = int(raw_input("How many players will be playing today?"))

        # create players
        self.create_players(num_players)

        # initial deal
        self.initial_deal()

    def create_players(self, num_players):
        i = 1
        while (i <= num_players):
            name = raw_input("What is player " + str(i) + "'s name?")
            self.add_player(name)
            i += 1

    def players_turn(self):
        for player in self.players:
            while player.state == PlayerState.Active:
                print "It is " + player.name + "'s turn"
                print player.name + " has a score of " + str(player.score)
                choice = int(raw_input("Press 1 to hit and 0 to stay"))

                if choice == 1:
                    player.hit(self.deck)

                elif choice == 0:
                    player.state = PlayerState.Stay

                else:
                    print "Invalid choice.  Please select again"
        self.update_highest_score()

    def dealers_turn(self):
        while self.dealer.score <= self.highest_score and self.dealer.score < 17 and self.dealer.state == PlayerState.Active:
            self.dealer.hit(self.deck)

        self.dealer.show_info()

    def update_highest_score(self):
        for player in self.players:
            if (player.score > self.highest_score):
                self.highest_score = player.score

    def initial_deal(self):
        self.initial_deal_dealer()
        self.initial_deal_players()

    def initial_deal_dealer(self):
        for x in range(2):
            self.dealer.hit(self.deck)

        print "Dealer's face-up card is a " + self.dealer.hand[0].face_name

        if (self.dealer.dealer_twentyone() == True):
            print "Dealer hit Blackjack!"
            self.state = GameState.DealerBJ

    def initial_deal_players(self):
        for player in self.players:
            player.hit(self.deck)
            player.hit(self.deck)

    def calculate_score(self):
        # dealer reached 17 or hit blackjack
        if self.dealer.state == PlayerState.Stay:

            for player in self.players:

                if player.state == PlayerState.Bust:
                    print player.name + " lost to dealer"

                if player.state == PlayerState.Stay:
                    if player.score > self.dealer.score:
                        print player.name + " beat the dealer"
                    elif player.score == self.dealer.score:
                        print player.name + " tied the dealer"
                    elif player.score < self.dealer.score:
                        print player.name + " lost to dealer"

        # dealer busted
        elif self.dealer.state == PlayerState.Bust:

            for player in self.players:

                if player.state == PlayerState.Stay:
                    print player.name + " beat the dealer"
                else:
                    print player.name + " lost to dealer"

class GameState:
    Active = 0
    DealerBJ = 1

# main function begins
while (1):
    game = Game()

