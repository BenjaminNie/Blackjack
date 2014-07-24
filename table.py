class Table:
    def __init__(self):
        self.dealer = BlackjackDealer()
        self.players = {}

    def add_player(self, name):
        self.player[name] = BlackjackPlayer(name)

    def remove_player(self, name):
        del self.players[name]

    def 
