import Cards
# Player info

class Player:
    def __init__(self, name):
        self.hand = []
        self.name = name

class BlackjackPlayer(Player):
    def __init__(self, name):
        Player.__init__(self, name)
        self.score = 0
        self.state = PlayerState.Active

    def hit(self, deck):
        self.hand.append(deck.deal())
        self.hand.sort(key=lambda x: x.face, reverse = True)

        for index,item in enumerate(self.hand):
            print "Index " + str(index) + " contains face " + str(item.face)
            
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

        else:
            self.state = PlayerState.Active

    def show_info(self):
        for card in self.hand:
            print "The card has face " + str(card.face) + " and suit " + str(card.suit)

        print "The player state is " + str(self.state)

        print "The player's score is " + str(self.score)

class BlackjackDealer(BlackjackPlayer):
    def __init__(self, name):
       BlackjackPlayer.__init__(self, name)
       

class PlayerState:
    Active = 0
    Stay = 1
    Bust = 2

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
