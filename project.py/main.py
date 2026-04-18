############################### SLOTS ###############################
# 777 wins jackpot
# any 3 in a row wins smaller ammount  = $5

# starting jackpot ammount: $10,000
# increases by 2% every loss


# symbols: 7 * @ # $ &
# 777 = 300, *** = 3, @@@ = 6, ### = 9, $$$ = 12, &&& = 15


from random import randint

class Slots:
    def __init__(self, user_tokens):
        self._user_tokens = user_tokens
        self._jackpot_amt = 10000
        self._jackpot_amt_original = 10000
        self._symbolsList=["7", "*", "@", "#", "$", "&"]
    
    def spinToDict(self):
        spinResult=self.spin()
        print(spinResult)
        spinDict={"7":10000, "*":1, "@":20, "#":30, "$": 400, "&":54}
        spinScore=0
        for symbol in spinResult:
            spinScore+=spinDict[symbol]
                
        return(spinScore)
    
    def spin(self):
        count=0
        spinResult=""
        while (count<3):
            spinResult+=self._symbolsList[randint(0,5)]
            count+=1
        return spinResult

    def playSlots(self):
        flag = True
        while flag:
            user_input = input("Press enter to spin (Cost: 1 Token), or exit. ")
            if  user_input.lower() == "exit":
                flag = False
                print( "Thanks for playing!")
                print(mainMenu())
            
            else:
                self._user_tokens-=1
                self.winOrLose()
                if (self._user_tokens<=0):
                    print ("You're out of tokens!")
                    flag = False
                    print( "Thanks for playing!")
                    print(mainMenu())
            
                
    
    def winOrLose(self):
        spinScore = self.spinToDict()
        

        if(spinScore == 30000):
            #777
            print(f"JACKPOTT!!!!!!!!!!!!!!!!!!!!!!!! YOU WIN THE POT OF {int(self._jackpot_amt)} TOKENS")
            
            self._user_tokens += int(self._jackpot_amt)
            self._jackpot_amt = self._jackpot_amt_original
            
        elif(spinScore == 3):
            #***
            print(f"Mini jackpot!! + 50 Tokens")
            self._user_tokens += 50
        elif(spinScore == 60):
            #@@@
            print(f"Mini jackpot!! + 50 Tokens")
            self._user_tokens += 50
        elif(spinScore == 90):
            # ###
            print(f"Mini jackpot!! + 50 Tokens")
            self._user_tokens += 50
        elif(spinScore == 1200):
            #$$$
            print(f"Mini jackpot!! + 50 Tokens")
            self._user_tokens += 50
        elif(spinScore == 162):
            #&&&
            print(f"Mini jackpot!! + 50 Tokens")
            self._user_tokens += 50
            
        else:
            self._jackpot_amt += (self._jackpot_amt *.02)
            print(f"Loss! \nCurrent Jackpot: {int(self._jackpot_amt)} Tokens")
        
        print(f"Your Tokens: {self._user_tokens}")


importTokens = 100       #temporaray
slotPlay = Slots(importTokens)
#print(slotPlay.playSlots())
############################### SLOTS ###############################






def setUsername():
    username = input("Enter your username: ")

def mainMenu():
    print("Welcome to the Rush Casino")
    print("1.) See Games\n2.) See Leaderboard\n3.) Leave Casino")
    playOrNo = int(input("What would you like to do? Enter the associated number: "))
    if(playOrNo == 1):
        whatGame()
    elif(playOrNo == 2):
        print("leaderboard coming soon")
    elif(playOrNo == 3):
        print("You chose to leave, you walk out with {tokens} tokens. Your name has been added to the leaderboard.")

    
def whatGame():
    print("Games: \n1.) Slots\n2.) BlackJack\n3.) Baccarat")
    gameSelect = int(input("What game do you want to play? Enter the associated number: "))
    if(gameSelect == 1):
        slotPlay.playSlots()
    elif(gameSelect == 2):
        print("blackjack coming soon")
    elif(gameSelect == 3):
        print("baccarat coming soon")
    else:
        print("Error: Unknown game selected.")





mainMenu()
