from itertools import repeat
import random

# Rules of blackjack
rules = """Here are the rules:
The dealer will deal two cards to each player, including the dealer himself. You will be able to see both
your cards but you will not be able to see one of the dealers cards.
Number cards will be worth as many points as the number on the card. (For example, 9 is worth 9 points,
3 is worth 3 points).
The A (Ace) card is worth either 1 or 11 points. The face cards (Jack, Queen, King) are worth 10 points.
The goal of the game is to get the sum of your cards as close to 21 as possible (this is including 21).
If you go over 21, you bust and you lose the round. You win the round if your number is higher than the
dealer's number.
For example, if you have a 7 and a J, your hand is worth 17 points. If the dealer has an 8 and a Q, the
dealer's hand is worth 18 points, and so you lose.
If your hand is worth 17 points but the dealer only has a 5 and an 8 (total = 13), you win!
Each round, you will be able to hit (draw another card) or stand (keep your current cards and don't draw). 
"""

STARTING_CASH = 1000
# Create a list of all unique cards
unique_cards = ['A', 'J', 'Q', 'K']
for i in range(2,11):
    unique_cards.insert(i-1, str(i))
# Points for each card in a dict
points = {k:k for k in unique_cards}
# Change A, J, Q, K value in dict. A will be 11 unless total is over 21, then it will change to 1.
points['A'] = '11'
points['J'], points['Q'], points['K'] = '10', '10', '10'
    
def main():
    print("TYPE CTRL+C IF YOU WAN'T TO STOP THE PROGRAM AT ANY TIME\n" + "-" * 105)
    # Asks user if they want to read the rules
    while True:
        print("Welcome to Blackjack! Do you want to read the rules? (y/n)")
        rules_ans = input(">").lower()
        if rules_ans != 'y' and rules_ans != 'n':
            print("Please type 'y' or 'n'\n")
        else:
            break
    if rules_ans == 'y':
        print('-' * 105)
        print(rules)
        print('-' * 105)
    # Round loop
    while True:
        cash = STARTING_CASH
        print("Your Balance:", cash)
        bet = place_bet(cash)
        cash -= bet
        deck = Deck()
        dealer_hand, player_hand = [], []
        # Initial deal - 2 cards each
        deck.deal(player_hand, dealer_hand)
        dealer_hidden = [dealer_hand[0], "?"]
        dealer_hand[0] = 'A'
        dealer_hand[1] = '10'
        
        round(player_hand, dealer_hand, dealer_hidden, bet)
        
class Deck():
    def __init__(self):
        self.deck = []
        self.burned = []
        for u in unique_cards:
            self.deck.extend(repeat(u, 4))
    def __repr__(self):
        return str(self.deck)
    # Initial shuffle
    def shuffle_burn(self):
        # Shuffle and burn top card
        random.shuffle(self.deck)
        burn = self.deck.pop()
        self.burned.append(burn)
    # Draw card into dealer or player's hand
    def draw(self, hand):
        hand.append(self.deck.pop())
    # Initial deal
    def deal(self, *args: list):
        self.shuffle_burn()
        # Deals two cards to each player
        count = 0
        while count < 2:
            for p in args:
                self.draw(p)
            count += 1

# Function to place bets
def place_bet(balance):
    while True:
        print("Please place your bet: (2.00 to 500.0)")
        bet = input(">")
        try:
            bet = int(bet)
            if bet > balance:
                print(f"You do not have enough money. Your current balance is: {balance}\n")
            elif bet < 2 or bet > 500:
                print("You must enter a value between 2 and 500.\n")
            else:
                break
        except ValueError:
            print("Please enter an integer.\n")
    return bet
            
# This will loop per round
def round(player, dealer, dealer_hidden, bet):
    print("-" * 105)
    print(f"DEALER HAND: {dealer_hidden}\n\n")
    print(f"YOUR HAND: {player}\n")
    print("-" * 105)
    # Check naturals
    dealer_bj = False
    player_bj = False
    if int(points[player[0]]) + int(points[player[1]]) == 21:
        player_bj = True
    if int(points[dealer[0]]) + int(points[dealer[1]]) == 21:
        dealer_bj = True
    if player_bj and dealer_bj:
        print("The dealer and the player both have blackjack! Returning bets...")
        print("-" * 105)
        cash += bet
    elif player_bj and not dealer_bj:
        print("The player has a blackjack! 1.5x return...")
        print("-" * 105)
        cash += 1.5*bet
    elif dealer_bj and not player_bj:
        print("The dealer has a blackjack! Sorry, you lose this round...")
        print("-" * 105)
        
    
        
if __name__ == '__main__':
    main()