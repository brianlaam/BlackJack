import random
import time

# Game Settings
suits = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
ranks = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King', 'Ace')
values = {'Two':2, 'Three':3, 'Four':4, 'Five':5, 'Six':6, 'Seven':7, 'Eight':8, 'Nine':9, 'Ten':10, 'Jack':10, 'Queen':10, 'King':10, 'Ace':11}

# Visual Effetcs Functions
def EmptyLine():
    print()

def DottedLine():
    print("============")

def GameStartLine():
    print("==============")
    print("New Game Start")
    print("==============")
    print()        

# Basic Functions
class Card:
    def __init__(self,suit,rank):
        self.suit = suit
        self.rank = rank
  
    def __str__(self):
        return self.rank + ' of ' + self.suit

class Deck:
    def __init__(self): # Create 52 cards
        self.deck = []
        for suit in suits:
            for rank in ranks:
                self.deck.append(Card(suit,rank))
  
    def shuffle(self):  # Randomizes order
        random.shuffle(self.deck)
    
    def deal(self):
        single_card = self.deck.pop()   # Take 1 card off the deck
        return single_card

class Hand:
    def __init__(self):
        self.cards = []
        self.value = 0
        self.aces = 0
  
    def add_card(self,card):
        self.cards.append(card)
        self.value += values[card.rank]
    
        if card.rank == 'Ace':
            self.aces += 1
  
    def adjust_for_ace(self):
        while self.value > 21 and self.aces > 0:
            self.aces -= 1
            self.value -= 10

def ShowPlayerCard():
    print("Player hand: ", end = "")        
    for card in player_hand.cards:
        print("[",card,"]" , end=" ")  

def ShowFinalCard():
    print("Final Player hand: ", end = "")        
    for card in player_hand.cards:
        print("[",card,"]" , end=" ")
    print(player_hand.value)    
    print("Final Dealer hand: ", end = "")
    for card in dealer_hand.cards:
        print("[",card,"]" , end=" ")    
    print(dealer_hand.value) 

def ShowGameStat(stats):
    EmptyLine()
    print("=======================================")
    print(f"                  Wins: {stats.wins}")
    print(f"    Highest Win Streak: {stats.highest_win_streak}")
    print(f"                Losses: {stats.losses}")
    print(f"   Highest Loss Streak: {stats.highest_loss_streak}")
    print(f"              Win Rate: {(stats.wins/stats.games_played):.2%}")
    print(f"       Remaining Money: {(stats.new_money)}")
    print(f"        Net Win / Loss: {(stats.earnings)}")
    print("=======================================")

def AskDoubleDown(player_money,player_bet):
    while True:
        EmptyLine()
        doubledown = input("Do you wanna double down? (yes/no) ").lower()
        EmptyLine()
        if doubledown == "yes":
            player_money -= player_bet
            player_bet *= 2
            break
        elif doubledown == "no":
            break
        else:
            print("Invalid input. Please enter again. ")
    return doubledown         

# Winner Check 
def Dragon(hand):
    if len(hand.cards) == 5 and hand.value <= 21:
        return True
    else: 
        return False

def Straight(hand,values):
    if len(hand.cards) == 3 and hand.value <= 21:
        ranks = [values[card.rank] for card in hand.cards]
        ranks.sort()
        return ranks[-1] - ranks[0] == 2  
    else:
        return False

def Straight_Flush(hand):
    if not Straight(hand,values):
        return False
    suits = [card.suit for card in hand.cards]
    return len(set(suits)) == 1

player_money = 100

# Game Statistics
class GameStats:
    def __init__(self):
        self.games_played = 0
        self.wins = 0
        self.losses = 0
        self.win_streak = 0
        self.loss_streak = 0
        self.highest_win_streak = 0
        self.highest_loss_streak = 0
        self.earnings = 0
        self.new_money = 0

    def record_game(self, win, tie, new_player_money):
        self.games_played += 1
        self.new_money = new_player_money
        self.earnings = new_player_money - 100
        if tie == False:    
            if win:
                self.wins += 1
                self.win_streak += 1
                self.loss_streak = 0
                if self.win_streak > self.highest_win_streak:
                    self.highest_win_streak = self.win_streak
                else:
                    pass    
            elif win == False:
                self.losses += 1
                self.loss_streak += 1
                self.win_streak = 0  
                if self.loss_streak > self.highest_loss_streak:
                    self.highest_loss_streak = self.loss_streak
                else:
                    pass              
        else:
            pass

stats = GameStats()

# Game Running
playing = True
while playing:    
    deck = Deck()
    deck.shuffle()

    player_hand = Hand()
    dealer_hand = Hand()

    # Deal first 2 cards
    player_hand.add_card(deck.deal())
    player_hand.add_card(deck.deal())

    dealer_hand.add_card(deck.deal())
    dealer_hand.add_card(deck.deal())

    player_hand.adjust_for_ace()
    dealer_hand.adjust_for_ace()

    print("==========================")
    print("Welcome to BlackJack Game!")
    print("==========================")
    print(f"   You  have  ${player_money}  now   ")
    print("==========================")
    EmptyLine()
    GameStartLine()
    time.sleep(0.5)
    
    # Player turns  
    while True:
        while True:
            player_bet = input(f"How much you wanna bet? (${player_money} left) ")
            if player_bet.isdecimal():
                player_bet = int(player_bet)
                break
            else:
                print("Invalid input. Please enter again.")

        #player_money -= player_bet
        EmptyLine()
        ShowPlayerCard()
        print(player_hand.value)
        print(f"Dealer hand: [ {dealer_hand.cards[0]} ] {values[dealer_hand.cards[0].rank]}")
        
        if player_hand.value > 21:
            time.sleep(0.5)
            print("Busted!")
            EmptyLine()
            break
        elif player_hand.value == 21:
            time.sleep(0.5)
            break
        elif player_hand.value < 21 and player_money >= 2 * player_bet:
            doubledown = AskDoubleDown(player_money,player_bet)
            if doubledown == "yes":
                player_bet *= 2
                player_hand.add_card(deck.deal())
                player_hand.adjust_for_ace()
                ShowPlayerCard()
                print(player_hand.value)
                print(f"Dealer hand: [ {dealer_hand.cards[0]} ] {values[dealer_hand.cards[0].rank]}")
            else:
                pass 
        else:
            doubledown = "no"           
    
        while player_hand.value < 15 and len(player_hand.cards) < 5 and doubledown == "no":
            EmptyLine()
            print("====================================================")
            print("You get less than 15. You have to get one more card.")
            print("====================================================")
            EmptyLine()
                
            time.sleep(1)

            player_hand.add_card(deck.deal())
            player_hand.adjust_for_ace()
            ShowPlayerCard()
            print(player_hand.value)
            print(f"Dealer hand: [ {dealer_hand.cards[0]} ] {values[dealer_hand.cards[0].rank]}")

        if len(player_hand.cards) < 5 and player_hand.value < 21 and doubledown == "no":
            while True:
                EmptyLine()
                move = input("Hit or stand? ").lower() 
                if move == 'hit':
                    EmptyLine()
                    player_hand.add_card(deck.deal())
                    player_hand.adjust_for_ace()
                    break          
                elif move == 'stand':
                    break
                else:
                    EmptyLine()
                    print("Invalid input. Please enter again.")
            break        
        else:
            #EmptyLine()
            break
    
    # Dealer turns
    while dealer_hand.value <= 16:
        dealer_hand.add_card(deck.deal())
        dealer_hand.adjust_for_ace()

    if player_hand.value > dealer_hand.value and dealer_hand.value < 21 and player_hand.value < 21 and player_hand.value - dealer_hand.value > 3 :
        dealer_hand.add_card(deck.deal())
        dealer_hand.adjust_for_ace()      
    else:
        pass
    
    # Show hand
    EmptyLine()
    print("==========")
    print("Show hand!")
    print("==========")
    time.sleep(0.5)
    
    # Final hands  
    ShowFinalCard()

    # Winner Check
    PDrag = Dragon(player_hand)
    DDrag = Dragon(dealer_hand)
    PStra = Straight(player_hand, values)
    DStra = Straight(dealer_hand, values)
    PSF = Straight_Flush(player_hand)
    DSF = Straight_Flush(dealer_hand)

    tie = False
    BlackJack = False
    EmptyLine()
    if dealer_hand.value == 21 and player_hand.value != 21:
        print("Dealer Blackjack! You lose.")
        player_win = False
        BlackJack = True
    elif player_hand.value == 21 and dealer_hand.value != 21:
        print("Blackjack! You win!")
        player_win = True
        BlackJack = True
    elif dealer_hand.value > 21 and player_hand.value > 21:
        print("You & Dealer both busted. You lose.")
        player_win = False
    elif dealer_hand.value > 21 and player_hand.value < 21:
        print("Dealer busted. You win!")
        player_win = True
    elif player_hand.value > 21 and dealer_hand.value < 21:
        print("Busted! You lose.")
        player_win = False    
    elif player_hand.value > dealer_hand.value and player_hand.value < 21: 
        if PDrag:
            print("Dragon! You win!")
        elif PStra:
            print("Straight! You win!")
        elif PSF:
            print("Straight Flush! You win")
        else:
            print("You win!")
        player_win = True
    elif player_hand.value < dealer_hand.value and dealer_hand.value < 21: 
        if DDrag:
            print("Dealer Dragon! You win!")
        elif DStra:
            print("Dealer Straight! You win!")
        elif DSF:
            print("Dealer Straight Flush! You win")
        else:
            print("Dealer win!")
        player_win = False
    elif player_hand.value == dealer_hand.value:
        print("Tie game.")
        tie = True
        player_win = False  
    else:
        pass
    
    # Game Bet
    if player_win == True:
        if BlackJack == True:
            player_money += player_bet * 1.5
        if PDrag:
            player_money += player_bet * 3
        if PStra:
           player_money += player_bet * 10
        if PSF:
            player_money += player_bet * 40
        if BlackJack == PDrag == PStra == PSF == False:
            player_money += player_bet
    elif player_win == False:
        if tie == True:
            player_money = player_money
        elif tie == False:
            if BlackJack == True:
                player_money -=  player_bet 
            if DDrag:    
                player_money += player_bet * 3
            if DStra:
                player_money -= player_bet * 10
            if DSF:
                player_money -= player_bet * 40
            if BlackJack == DDrag == DStra == DSF == False:
                player_money -=  player_bet     
    else:
        pass

    # Display Game Statstics 
    GameStatsDisplay = []
    stats.record_game(player_win, tie, player_money)
    time.sleep(0.5)
    ShowGameStat(stats)

    if player_money <= 0:
        EmptyLine()
        print("====================")
        print("Remaining Money = $0")
        print("   Game     Over    ")
        print("====================")
        break
    else:
        pass    

    while player_money > 0:
        EmptyLine()
        play_again = input("Play again? (Yes/No) ").lower()
        EmptyLine()
        if play_again == "yes":
            break
        elif play_again == "no":
            print("See you next time!")
            playing = False
            break
        else:
            EmptyLine()
            print("Invalid input. Please enter again.")