from random import shuffle

class Card:
    suits = ["diamonds",
            "spades",
            "hearts",
            "clubs"]
    values = [None,None,"2","3","4","5","6","7","8","9","Jack","Queen","King","Ace"]
    def __init__(self,v,s):
        self.suit = s
        self.value = v
    def __lt__(self,c2):
        if self.value < c2.value:
            return True
        if self.value==c2.value:
            if self.suit < c2.value:
                return True
        else:
            return False
        return False
    def __gt__(self,c2):
        if self.value > c2.value:
            return True
        if self.value==c2.value:
            if self.suit > c2.value:
                return True
        else:
            return False
        return False
    def __repr__(self):
        v = self.values[self.value] +\
         " of " + \
         self.suits[self.suit]
        return v
        

class Deck:
    def __init__(self):
        self.cards = []
        for i in range(2,15):
            for j in range(4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)
    def rn_cards(self):
        if(len(self.cards) == 0):
            return
        return self.cards.pop()
class Player:
    def __init__(self,name):
        self.name = name
        self.wins = 0
        self.cards = None

class Game:
    def __init__(self):
        name1 = input("PLayer 1 name: ")
        name2 = input("PLayer 2 name: ")
        self.deck = Deck()
        self.p1 = Player(name1)
        self.p2 = Player(name2)
    def wins(self,winner):
        w = "{} wins this round"
        w = w.format(winner)
        print(w)
    def draw(self,p1n,p1c,p2n,p2c):
        d = "{} drew {}, {} drew {}"
        d = d.format(p1n,p1c,p2n,p2c)
        print(d)
    def pg(self):
        cards = self.deck.cards
        print("beggining war...")
        while len(cards) >= 2:
            m = "q to quit.Any key to play:"
            response = input(m)
            if(response == "q"):
                break
            p1c = self.deck.rn_cards()
            p2c = self.deck.rn_cards()
            p1n = self.p1.name
            p2n = self.p2.name
            self.draw(p1n,p1c,p2n,p2c)
            if p1c > p2c:
                self.p1.wins += 1
                self.wins(self.p1.name)
            if p1c < p2c:
                self.p2.wins += 1
                self.wins(self.p2.name)
                
        win = self.winner(self.p1,self.p2)
        print("War is over .{} wins".format(win))
    def winner(p1,p2):
        if p1.wins > p2.wins:
            return p1.name
        if p2.wins > p1.wins:
            return p2.name
        return "It was a tie"
            
game = Game()
game.pg()