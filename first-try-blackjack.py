while True:
    print('Welcome to Blackjack!')
    break
    
    # Create & shuffle the deck, deal two cards to each player
import random

suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10,
         'Queen':10, 'King':10, 'Ace':11}

playing = True
    
class Card:
    
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
    
    def __str__(self):
        return self.rank + ' of ' + self.suit
    
class Deck:
    
    def __init__(self):
        self.deck = []  # start with an empty list
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))  # build Card objects and add them to the list
    
    def __str__(self):
        deck_comp = ''  # start with an empty string
        for card in self.deck:
            deck_comp += '\n '+card.__str__() # add each Card object's print string
        return 'The deck has:' + deck_comp

    def shuffle(self):
        random.shuffle(self.deck)
        
    def deal(self):
        self.deck.pop()
    # Set up the Player's chips
class Chips:
    
    def __init__(self):
        self.total = 100  # This can be set to a default value or supplied by a user input
        self.bet = 0
        
    def win_bet(self):
        self.total = self.bet + self.total
    
    def lose_bet(self):
        self.total = self.total - self.bet  
    
    # Prompt the Player for their bet
def take_bet():
    while True:
        try:
            bet = int(input('how much are you betting?'))
        except:
            if bet < 0:
                return ('You cannot bet a negative number!')
            if bet > total:
                return('You cannot bet more than you have!')
            break  
    
    # Show cards (but keep one dealer card hidden)
def show_some(player,dealer,hand):
    for card in hand:
        if player == player:
            for card in hand,card:
                print(card)
    
def show_all(player,dealer):
    if player == dealer:
        for card in hand:
            print (card[0])
    
#    while playing:  # recall this variable from our hit_or_stand function
        
        # Prompt for Player to Hit or Stand
def hit_or_stand(deck,hand):
    global playing  # to control an upcoming while loop
    wantshit = input('do you want to hit, or stay?')
    if wantshit == 'hit':
        hit()
    else:
        playing == False        
        
        # Show cards (but keep one dealer card hidden)
def show_some(player,dealer,hand):
    for card in hand:
        if player == player:
            for card in hand,card:
                print(card)
    
def show_all(player,dealer):
    if player == dealer:
        for card in hand:
            print (card[0]) 
        
        # If player's hand exceeds 21, run player_busts() and break out of loop
if player == player and hand >21:
    player_busts()


   

    # If Player hasn't busted, play Dealer's hand until Dealer reaches 17
if player == player and hand <21 and playing == False:
    if card[1] == '':
        deal(dealer)
    
        # Show all cards
    for card in hand:
        if player == player:
            for card in hand,card:
                print(card)    
def player_busts():
    print('BUSTED!!!')
    total = total - bet

def player_wins():
    print('You WON!!!')
    total = total + bet

def dealer_busts():
    print('Dealer BUSTED!!!')
    total = total + bet
    
def dealer_wins():
    print('Dealer won :o!!!')
    total = total - bet
    
def push():
    print('Push, no one won')        # Run different winning scenarios
        
    
    # Inform Player of their chips total 
print('Your total chips are{}'(format.total))
    
    # Ask to play again

