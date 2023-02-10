from itertools import repeat
import random

# Rules
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

# Create a list of all unique cards
unique_cards = ['A', 'J', 'Q', 'K']
for i in range(2,11):
    unique_cards.insert(i-1, str(i))
    
def main():
    while True:
        print("Welcome to Blackjack! Do you want to read the rules? (y/n)")
        rules_ans = input()
        if rules_ans != 'y' and rules_ans != 'n':
            print("Please type 'y' or 'n'")
        else:
            break
    if rules_ans == 'y':
        print('-' * 105)
        print(rules)
        print('-' * 105)
    deck = Deck()
    dealer_hand, player_hand = [], []
    # Initial deal
    deck.deal(player_hand, dealer_hand)
    
    

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
                
        
if __name__ == '__main__':
    main()