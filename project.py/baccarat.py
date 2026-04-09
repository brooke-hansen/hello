
class Player:
    def __init__(self, name, tokens=100):
        self.name = name
        self.tokens = tokens
    
    def getName(self):
        return self.name
    
    def changeName(self, newname):
        self.name = newname
    
    def getTokens(self):
        return self.tokens
    
    def changeTokens(self, newbal):
        self.tokens = newbal
    
    def __str__(self):
        msg = f" Player: {self.name}  Tokens: {self.tokens}"
        return msg

class Baccarat:
    def __init__(self, player):
        self.player = Player
        self.deck = []
        self.player_hand = []
        self.bank_hand = []
        self.current_index = 0
    
    def create_cards(self):
        self.deck = []
        ranks = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9,"10": 0, "J": 0, "Q": 0, "K": 0}
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"]
        for suit in suits:
            for rank, value in ranks.items():
                self.deck.append((rank, suit, value))

    def shuffle_deck(self):
        import random
        random.shuffle(self.deck)
        self.current_index = 0

    def deal_cards(self):
        if self.current_index >= len(self.deck):
            print("Deck is empty!")
            return None
        card = self.deck[self.current_index]
        self.current_index += 1
        return card

    def calculate_hand(self, hand):
        pass

    def place_bet(self, bet_type, amount):
        pass

    def play_round(self):
        pass

    def determine_winner(self):
        pass
    
    def payout(self, result):
        pass
    
    def reset_round(self):
        self.player_hand = []
        self.banker_hand = []
    
    def show_player(self):
        print(self.player)
