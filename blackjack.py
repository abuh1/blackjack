from itertools import repeat
import random

# Initial starting money
balance = 1000
# Create a list of all unique cards
unique_cards = ['A', 'J', 'Q', 'K']
for i in range(2,11):
    unique_cards.insert(i-1, str(i))
# Points for each card in a dict
points = {k:k for k in unique_cards}
# Change A, J, Q, K value in dict. A will be 11 unless total is over 21, then it will change to 1.
points['A'] = 11
for n in range(2,11):
    points[str(n)] = n
points['J'], points['Q'], points['K'] = 10, 10, 10

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

# Deck class
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
    # Draw card into dealer or player's hand, and appends it to burned to keep all removed cards for reshuffling later
    def draw(self, hand):
        top_card = self.deck.pop()
        hand.append(top_card)
        self.burned.append(top_card)
    # Initial deal
    def deal(self, *args: list):
        # Reshuffle the deck when it gets down to half
        if len(self.deck) <= 26:
            for i in self.burned:
                self.deck.append(i)
            self.burned = []
            self.shuffle_burn()
        # Deals two cards to each player
        count = 0
        while count < 2:
            for p in args:
                self.draw(p)
            count += 1

# Main loop
def main():
    global balance
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
    
    # Game loop, ends when player stops or loses all money
    while balance > 0:
        round()
            
# One full round
def round():
    global balance
    start = True
    while start:
        print("Your Balance:", balance)
        bet = place_bet(balance)
        balance -= bet
        # Creates deck and shuffles it
        deck = Deck()
        deck.shuffle_burn()
        
        dealer_hand, player_hand = [], []
        # Initial deal - 2 cards each
        deck.deal(player_hand, dealer_hand)
        dealer_hidden = [dealer_hand[0], "?"]
        # Total points for current hands
        p_score = sum(points[n] for n in player_hand)
        d_score = sum(points[n] for n in dealer_hand)
        
        print("-" * 105)
        print(f"\nDEALER HAND: {dealer_hidden}\n\n")
        print(f"YOUR HAND: {player_hand}\n")
        print("-" * 105)
        # Check naturals
        if p_score == 21 and d_score == 21:
            print("\n>The dealer and the player both have blackjack! Returning bets...")
            print("-" * 105)
            balance += bet
        elif p_score == 21 and d_score != 21:
            print("\nThe player has a blackjack! 1.5x return...")
            print("-" * 105)
            balance += 1.5*bet
        elif d_score == 21 and p_score != 21:
            print("\nThe dealer had a blackjack! Sorry, you lose this round...")
            print(f"\nDealer's hand was: {dealer_hand}\n")
            print("-" * 105)
        else:
            start = False
    # Hit or stand
    while True:
        move = input("Type 1 to hit, or 2 to stand.\n")
        try:
            move = int(move)
            if move != 1 and move != 2:
                print("Error: Type 1 or 2")
            else:
                break
        except ValueError:
            print("Error: Type 1 or 2")
    

# Recursive function to keep hitting as long as user does not go bust, returns new hand
def hit(hand, score, deck):
    top_card = deck.deck[-1]
    score += points[top_card]
    deck.draw(hand)
    print("\nACTION: HIT\n")
    print(f"NEW HAND: {hand}\n")
    print("-" * 105)
    if score > 21:
        return hand, score
    elif score == 21:
        return hand, score
    else:
        again = int(input("Hit again? (1 for yes, 2 for no)\n"))
        if again == 1:
            hand, score = hit(hand, score, deck)
        elif again == 2:
            return hand, score
    return hand, score
        
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
        
if __name__ == '__main__':
    main()