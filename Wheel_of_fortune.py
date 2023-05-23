import random

VOWEL_COST = 250
LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
VOWELS = 'AEIOU'

# Write the WOFPlayer class definition (part A) here
class WOFPlayer:
    def __init__(self,name):
        self.name=name
        self.prizeMoney=0
        self.prizes=[]
        
    def addMoney(self,amt):
        self.prizeMoney+=amt
    def goBankrupt(self):
        self.prizeMoney=0
    def addPrize(self,prize):
        self.prizes.append(prize)
        
    def __str__(self):
        return "{} (${})".format(self.name,self.prizeMoney)
        
        
        
        
# Write the WOFHumanPlayer class definition (part B) here

class WOFHumanPlayer(WOFPlayer):
    def __init__(self,name):
        WOFPlayer.__init__(self,name)
    def getMove(self,category, obscuredPhrase, guessed):
        print("{} has ${}".format(self.name,self.prizeMoney))

        print("Category: {}".format(category))
        print("Phrase: {}".format(obscured_phrase))
        print("Guessed: {}".format(guessed))
        
        PlayersGuess=input("Guess a letter, phrase, or type 'exit' or 'pass':")
        return PlayersGuess
    
# Write the WOFComputerPlayer class definition (part C) here

class WOFComputerPlayer(WOFPlayer):
    SORTED_FREQUENCIES="ZQXJKVBPYGFWMUCLDRHSNIOATE"
    def __init__(self,name,difficulty):
        WOFPlayer.__init__(self,name)
        self.SORTED_FREQUENCIES="ZQXJKVBPYGFWMUCLDRHSNIOATE"
        self.difficulty=difficulty
        
    
    def smartCoinFlip(self):
        randomDifficulty=random.randint(1,10)
        if randomDifficulty>self.difficulty:
             return True
        else :
             return False
              
    def getPossibleLetters(self,guessed):     
        VOWEL_COST = 250
        LETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
        VOWELS = 'AEIOU'
        CanBeGuessed=[]
        
        for letter in LETTERS:
            if letter not in guessed and letter not in VOWELS:
                CanBeGuessed.append(letter)
            elif letter not in guessed and letter in VOWELS:
                if self.prizeMoney>250:
                    CanBeGuessed.append(letter)
               
                    
              
        return CanBeGuessed
        
    def getMove(self,category, obscuredPhrase, guessed):
            
        CanBeGuessed=self.getPossibleLetters(guessed)
        if CanBeGuessed==[]:
            return "pass"
        else:
            smartMove=self.smartCoinFlip()
                
            if smartMove ==True:
                i=len(self.SORTED_FREQUENCIES)-1
                while i >=0:
                    if self.SORTED_FREQUENCIES[i] in CanBeGuessed:
                        return self.SORTED_FREQUENCIES[i]
                    else :
                        i-=1
                        continue
            else:
                randLetter=random.choice(CanBeGuessed)
                return randLetter
