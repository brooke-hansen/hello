
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
        self.player = player
        self.deck = []
        self.player_hand = []
        self.banker_hand = []
        self.current_index = 0
        self.bet_type = None
        self.bet_amount = 0
    
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
            self.create_cards()
            self.shuffle_deck()
            
        card = self.deck[self.current_index]
        self.current_index += 1
        return card

    def calculate_hand(self, hand):
        total = sum(card[2] for card in hand)
        return total % 10

    def place_bet(self, bet_type, amount):
        bet_type = bet_type.capitalize()

        if bet_type not in ["Player", "Banker", "Tie"]:
            print("Invalid bet!")
            return False

        if amount > self.player.tokens or amount <= 0:
            print("Invalid amount!")
            return False

        self.bet_type = bet_type
        self.bet_amount = amount
        return True
        

    def play_round(self):
        self.reset_round()
      
        # Initial deal
        self.player_hand = [self.deal_cards(), self.deal_cards()]
        self.banker_hand = [self.deal_cards(), self.deal_cards()]

        player_score = self.calculate_hand(self.player_hand)
        banker_score = self.calculate_hand(self.banker_hand)

        # Natural check
        if player_score in [8, 9] or banker_score in [8, 9]:
            print("Player hand:", self.player_hand, "Score:", self.calculate_hand(self.player_hand))
            print("Banker hand:", self.banker_hand, "Score:", self.calculate_hand(self.banker_hand))
            return self.determine_winner()

        # Player draws
        if player_score <= 5:
            self.player_hand.append(self.deal_cards())

        player_score = self.calculate_hand(self.player_hand)

     # Simplified banker rule (we can fix later)
        if banker_score <= 5:
         self.banker_hand.append(self.deal_cards())
         print("Player hand:", self.player_hand, "Score:", self.calculate_hand(self.player_hand))
         print("Banker hand:", self.banker_hand, "Score:", self.calculate_hand(self.banker_hand))

        return self.determine_winner()

    def determine_winner(self):
        player_score = self.calculate_hand(self.player_hand)
        banker_score = self.calculate_hand(self.banker_hand)
        if player_score > banker_score:
            return "Player"
        elif banker_score > player_score:
            return "Banker"
        else:
            return "Tie"
    
    def payout(self, result):
    # Tie push rule
        if result == "Tie" and self.bet_type in ["Player", "Banker"]:
            print("Push! No one wins.")
            return

        if result == self.bet_type:
            if result == "Banker":
                winnings = round(self.bet_amount * 0.95, 2)
            elif result == "Player":
                winnings = self.bet_amount
            else:  # Tie
                winnings = self.bet_amount * 8

            self.player.tokens += winnings
            print(f"You won {winnings} tokens!")
        else:
            self.player.tokens -= self.bet_amount
            print(f"You lost {self.bet_amount} tokens.")
    
    def reset_round(self):
        self.player_hand = []
        self.banker_hand = []
    
    def show_player(self):
        print(self.player)

# Create player and game
name = input("Enter your name: ")
player = Player(name, 100)
game = Baccarat(player)

game.create_cards()
game.shuffle_deck()

# Game loop
while player.tokens > 0:
    print("\n-------------------")
    game.show_player()

    # Get bet
    bet_type = input("Bet on (Player/Banker/Tie): ")
    amount = int(input("Bet amount: "))

    # Place bet
    if not game.place_bet(bet_type, amount):
        continue

    # Play round
    result = game.play_round()
    print("Result:", result)

    # Payout
    game.payout(result)

    # Continue?
    cont = input("Play again? (y/n): ").lower()
    if cont != "y":
        break

print("Game over!")