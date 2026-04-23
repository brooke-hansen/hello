
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
    
    def add_Tokens(self, amount):
        self.tokens += amount
    
    def remove_tokens(self, amount):
        self.tokens -= amount
        if self.tokens < 0:
            self.tokens = 0
    
    def __str__(self):
        msg = f" Player: {self.name}  Tokens: {self.tokens}"
        return msg

class Baccarat: #Game 
    def __init__(self, player: Player): #What's needed to play
        self.player = player #player
        self.deck = [] #deck of cards (empty dictionary)
        self.player_hand = [] #player's hand (empty dictionary)
        self.banker_hand = [] #banker's hand (empty dictionary)
        self.current_index = 0 #current index position (top card)
        self.bet_type = None #empty for bet type input
        self.bet_amount = 0 #amount being bet (set to 0)
    
    def create_cards(self): #creates deck of 52 cards
        self.deck = [] #empty dictionary to store cards
        ranks = {"A": 1, "2": 2, "3": 3, "4": 4, "5": 5,"6": 6, "7": 7, "8": 8, "9": 9,"10": 0, "J": 0, "Q": 0, "K": 0} #rank and point-value
        suits = ["Hearts", "Diamonds", "Clubs", "Spades"] #different suits
        for suit in suits: #for each suit in suits
            for rank, value in ranks.items(): #for each rank, value in ranks-dictionary
                self.deck.append((rank, suit, value))  #append the rank, suit, and value to deck-dictionary 

    def format_card(self, hand): #function that formats card for pretty print statements
        
        #asked ai how to get the cleanest look
        return ", ".join(f'{rank} of {suit} for {value} points' for rank, suit, value in hand) 
        
        #originally I used:
        #return [f'{rank} of {suit} for {value} points' for rank, suit, value in hand]

    def shuffle_deck(self): #shuffles created deck
        import random #import randomizer
        random.shuffle(self.deck) #random shuffle the created deck
        self.current_index = 0 #set live index position to 0 (top card)

    def deal_cards(self): #deal out cards
        if self.current_index >= len(self.deck): #if index poistion is beyond 52
            self.create_cards() #create new cards
            self.shuffle_deck() #shuffle deck
            
        card = self.deck[self.current_index] #set card to live index position
        self.current_index += 1 #move live index poisiton up one (deal out single card)
        return card #return card dealt

    def calculate_hand(self, hand): #calculates dealt hand values
        total = 0 #start with 0
        for card in hand: #for each card in the hand
            total += card[2] #add the value (index 2) to the total 
        return total % 10 #returns the digits in ones place after totaling points 

    def place_bet(self, bet_type, amount): #place bet
        bet_type = bet_type.capitalize() #allows for any capitalization in accepted answers

        if bet_type not in ["Player", "Banker", "Tie"]: #if not one of acceptable bet types
            print("Try entering Player, Banker, or Tie: ") #asks for a valid bet
            return False

        if amount > self.player.tokens or amount <= 0: #if amount is more than available or less than 0
            print("Unable to Match Bet!") #try again 
            return False

        self.bet_type = bet_type
        self.bet_amount = amount
        return True

    def play_round(self): #how to play the game
        self.reset_round() #triggers reset_round function
        
        #print statement, break in line    
        print('-------------------------------------------------------')
        
        #Initial deal, 2 cards each
        self.player_hand = [self.deal_cards(), self.deal_cards()] #triggers deal_card function twice and inserts into dictionary
        self.banker_hand = [self.deal_cards(), self.deal_cards()] #triggers deal_card function twice and inserts into dictionary

        #calculate initial player score
        player_score = self.calculate_hand(self.player_hand) #triggers calculate_hand function
        #print statements for score
        print("Player's Hand -> ", self.format_card(self.player_hand), end = ' -> ') #triggers format_card function
        print(f'Total score = {player_score}')
        
        #calculate initial banker score
        banker_score = self.calculate_hand(self.banker_hand) #triggers calculate_hand function
        #print statements for score
        print("Banker's Hand -> ", self.format_card(self.banker_hand), end = ' -> ') #triggers format_card function
        print(f'Total score = {banker_score}')

        #print statement, break in line    
        print('-------------------------------------------------------')
        
        #check for a natural win: score of either 8 or 9
        if player_score in [8, 9] or banker_score in [8, 9]: #if scores in range[8,9] 
            print('NATURAL WIN!') #print statement
            return self.determine_winner() #jump to determine winner function

        elif player_score > 5: #if player score more than 5, player doesn't draw
            print("PLAYER HOLDS") #print statement
       
        elif player_score <= 5: #if player score less than 5, player draws again
            print('PLAYER DRAWS ANOTHER CARD!', end = ' -> ') #print statement
            self.player_hand.append(self.deal_cards()) #deals/appends new card to player hand #triggers deal_card function
            print(self.format_card([self.player_hand[2]])) #prints new card #triggers format_card function
            player_score = self.calculate_hand(self.player_hand) #recalculates player's total #triggers calculate_hand function
            #print statements for player's score
            print("Player's Hand -> ", self.format_card(self.player_hand), end = ' -> ') #triggers format_card function
            print(f'Total score = {player_score}')
        
        #print statement, break in line    
        print('-------------------------------------------------------')
        
        #banker rules for drawing:
        #banker's draw depends on the value of the player's 3rd card
        player_third_value = self.player_hand[2][2] if len(self.player_hand) == 3 else None
        
        if player_third_value is None: #if player doesn't draw
            #easy rules
            if banker_score <= 5: #then if banker score < 5
                print('BANKER DRAWS ANOTHER CARD!', end = ' -> ') #print statement
                self.banker_hand.append(self.deal_cards()) #draw/append new card #triggers deal_card function
                print(self.format_card([self.banker_hand[2]])) #print new card #triggers dormat_card function
            else: #if banker score > 5, 
                print("BANKER HOLDS") #banker doesn't draw
        
        else: #complex rules
            if banker_score <= 2: #if banker score <=2 , draw card 
                print('BANKER DRAWS ANOTHER CARD!', end = ' -> ') #print statement
                self.banker_hand.append(self.deal_cards()) #draws/appends new card to banker hand #triggers deal_cards function
                print(self.format_card([self.banker_hand[2]])) #prints new card #triggers format_card function

            elif banker_score == 3 and player_third_value != 8: #if banker score = 3 and player's 3rd card < 8, draw card
                print('BANKER DRAWS ANOTHER CARD!', end = ' -> ') #print statement
                self.banker_hand.append(self.deal_cards()) #draws/appends new card to banker hand #triggers deal_cards function
                print(self.format_card([self.banker_hand[2]])) #prints new card #triggers format_card function


            elif banker_score == 4 and player_third_value in range(2,8): #if banker score = 4 and player's 3rd card is 2-7, draw card
                print('BANKER DRAWS ANOTHER CARD!', end = ' -> ') #print statement
                self.banker_hand.append(self.deal_cards()) #draws/appends new card to banker hand #triggers deal_cards function
                print(self.format_card([self.banker_hand[2]])) #prints new card #triggers format_card function
            
            elif banker_score == 5 and player_third_value in range(4,8): #if banker score = 5 and player's 3rd card is 4-7, draw card
                print('BANKER DRAWS ANOTHER CARD!', end = ' -> ') #print statement
                self.banker_hand.append(self.deal_cards()) #draws/appends new card to banker hand #triggers deal_cards function
                print(self.format_card([self.banker_hand[2]])) #prints new card #triggers format_card function

            elif banker_score == 6 and player_third_value in range(6,8): #if banker score = 6 and player's 3rd card is 6 or 7, draw card
                print('BANKER DRAWS ANOTHER CARD!', end = ' -> ') #print statement    
                self.banker_hand.append(self.deal_cards()) #draws/appends new card to banker hand #triggers deal_cards function
                print(self.format_card([self.banker_hand[2]])) #prints new card #triggers format_card function
            
            else: #otherwise
                print("BANKER HOLDS") #banker doesn't draw

         #recalculate banker's score after holding/drawing card                 
        banker_score = self.calculate_hand(self.banker_hand) #triggers caluclate_hand function
        #print statements for banker's score
        print("Banker's Hand -> ", self.format_card(self.banker_hand), end = ' -> ') #triggers format_card function
        print(f'Total score = {banker_score}')

        #print statement, break in line    
        print('-------------------------------------------------------')
        
        #print statement comparing final scores side by side
        print(f'Total Player = {player_score}', end = ' vs. ')
        print(f'Total Banker = {banker_score}')

        #print statement, break in line    
        print('-------------------------------------------------------')
        
        return self.determine_winner() #trigger determine winner function

    def determine_winner(self): #function that determines winner
        player_score = self.calculate_hand(self.player_hand) #calculates player's hand
        banker_score = self.calculate_hand(self.banker_hand) #calculates banker's hand
        
        if player_score > banker_score: #if player > banker
            return "Player" #player wins
        elif banker_score > player_score: #if banker > player
            return "Banker" #banker wins
        else: #if banker = player
            return "Tie" #tie
    
    def payout(self, result): #payout function
    
        #Tie-Push rule
        if result == "Tie" and self.bet_type in ["Player", "Banker"]: #if it's a tie and player didn't bet tie
            print("Push! No one wins.") #no one wins
            return

        if result == self.bet_type: #if player bet results correctly
            if result == "Banker": #if banker won
                winnings = round(self.bet_amount * 0.95, 2) #player wins .95% of bet
            elif result == "Player": #if player won
                winnings = self.bet_amount #player wins amount betted
            else:  #if tie
                winnings = self.bet_amount * 8 #player wins 8x bet amount

            self.player.tokens += winnings #add winnings to player tokens
            #print statement
            print(f"You've won {winnings} tokens!")
       
        else: #if bet lost
            self.player.tokens -= self.bet_amount #subtract bet from token amounts
            #print statement
            print(f"You lost {self.bet_amount} tokens.")
    
    def reset_round(self): #resets round
        self.player_hand = [] #empties out player's hand
        self.banker_hand = [] #empties out banker's hand
    
    def show_player(self):
        print(self.player)

#Create player and game
name = input("Enter your name: ")
name = name.capitalize()
player = Player(name, 100)
game = Baccarat(player)

game.create_cards()
game.shuffle_deck()

def baccGame():
    #Game loop
    while player.tokens > 0:
        print("\n-------------------")
        game.show_player()

        #Get bet
        bet_type = input("Bet on Player/Banker/Tie: ")
        amount = int(input("Add Bet: "))

        #Place bet
        if not game.place_bet(bet_type, amount):
            continue

        #Play round
        result = game.play_round()
        print("Winner:", result)

        #Payout
        game.payout(result)

        #Continue
        cont = input("Play again? y/n: ").lower()
        if cont != "y":
            return 
            break

    print("Game over!")

baccGame()