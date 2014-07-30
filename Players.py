# Player info

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

    def print_extra_line(self):
        print

class BlackjackPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.score = 0
        self.state = PlayerState.Active
        self.new_card = None

    def hit(self, deck):
        self.new_card = deck.deal()

        self.hand.append(self.new_card)
        self.hand.sort(key=lambda x: x.face, reverse = True)

        """ DEBUG FXN
        for index,item in enumerate(self.hand):
            print "Index " + str(index) + " contains face " + str(item.face)
        """

        self.calculate_score()
        self.show_info()

    def calculate_score(self):
        # calculate the total sum in hand
        self.score = 0

        for card in self.hand:
           if card.face == Face.Two:
              self.score += 2

           elif card.face == Face.Three:
              self.score += 3

           elif card.face == Face.Four:
              self.score += 4

           elif card.face == Face.Five:
              self.score += 5

           elif card.face == Face.Six:
              self.score += 6

           elif card.face == Face.Seven:
              self.score += 7

           elif card.face == Face.Eight:
              self.score += 8

           elif card.face == Face.Nine:
              self.score += 9

           elif card.face == Face.Ten:
              self.score += 10

           elif card.face == Face.Jack:
              self.score += 10

           elif card.face == Face.Queen:
              self.score += 10

           elif card.face == Face.King:
              self.score += 10

           elif card.face == Face.Ace:
              self.calculate_ace()
              break

        self.determine_state()

    def calculate_ace(self):
        number_aces = sum(card.face == 1 for card in self.hand)
        self.score += number_aces + 10

        if self.score > 21:
            self.score -= 10

    def determine_state(self):
        if self.score == 21:
            self.state = PlayerState.Stay

        elif self.score > 21:
            self.state = PlayerState.Bust
            print self.name + " has busted!\n"


        else:
            self.state = PlayerState.Active

    def show_info(self):
        print self.name + " drew a " + self.new_card.face_name + " of " + self.new_card.suit_name
        print self.name + "'s hand now contains:"

        for card in self.hand:
            print str(card.face) + card.suit_name,

        self.show_score()

    def show_score(self):
        print
        print self.name + "'s score is " + str(self.score)
        print

class BlackjackDealer(BlackjackPlayer):
    def __init__(self):
       BlackjackPlayer.__init__(self, "dealer")

    def determine_state(self):
       if 16 < self.score < 22:
            self.state = PlayerState.Stay

       elif self.score > 21:
            self.state = PlayerState.Bust

       else:
            self.state = PlayerState.Active

    def dealer_twentyone(self):
       self.hand.sort(key=lambda x: x.face, reverse = True)
       self.calculate_score()

       if self.score == 21:
          return True

       else:
          return False

    def initial_hit(self, deck):
        self.hand.append(deck.deal())
        self.new_card = deck.deal()
        self.hand.append(self.new_card)

        print "Dealer's face-up card is a " + self.hand[0].face_name
        self.print_extra_line()

        self.calculate_score()

class PlayerState:
    Active = 0
    Bust = 1
    Stay = 2

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

