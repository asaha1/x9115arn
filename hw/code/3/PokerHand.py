"""This module contains code from
Think Python by Allen B. Downey
http://thinkpython.com

Copyright 2012 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html

"""

from Card import *
frequency_of_poker_hands = {0:0,
                            1:0,
                            2:0,
                            3:0,
                            4:0,
                            5:0,
                            6:0,
                            7:0}

class PokerHand(Hand):

    def suit_hist(self):
        """Builds a histogram of the suits that appear in the hand.

        Stores the result in attribute suits.
        """
        self.suits = {}
        for card in self.cards:
            self.suits[card.suit] = self.suits.get(card.suit, 0) + 1

    def has_flush(self):
        """Returns True if the hand has a flush, False otherwise.
      
        Note that this works correctly for hands with more than 5 cards.
        """
        self.suit_hist()
        for val in self.suits.values():
            if val >= 5:
                return True
        return False
        
    def rank_hist(self):
        """Builds a histogram of the ranks that appear in the hand.

        Stores the result in attribute ranks.
        """
        self.ranks = {}
        for card in self.cards:
            self.ranks[card.rank] = self.ranks.get(card.rank, 0) + 1
        #print self.ranks
        
    def has_pair(self):
        """Returns True if the hand has a pair, False otherwise.
        """
        if self.count_pairs() >= 1:
            return True
        return False
        
    def has_twopair(self):
        """Returns True if the hand has a pair, False otherwise.
        """
        if self.count_pairs() >= 2:
            return True
        return False
                
    def count_pairs(self):
        """Returns True if the hand has two pairs, False otherwise.
        """
        num_of_pairs = 0
        for rank in self.ranks:
            if self.ranks[rank] >= 2:
                num_of_pairs = num_of_pairs + 1
        return num_of_pairs
        
    def has_three_of_a_kind(self):
        """Returns True if the hand has three of a kind, False otherwise.
        """
        for rank in self.ranks:
            if self.ranks[rank] >= 3:
                return True
        return False
        
    def has_straight(self):
        """Returns True if the hand has straight, False otherwise.
        """
        for rank in self.ranks:
            if rank + 1 in self.ranks and rank + 2 in self.ranks and rank + 3 in self.ranks and rank + 4 in self.ranks:
                return True
                
        #for 10, J, Q, K A
        if 1 in self.ranks and 10 in self.ranks and 11 in self.ranks and 12 in self.ranks and 13 in self.ranks:
            return True
        return False
        
    def has_full_house(self):
        """Returns True if the hand has Full House, False otherwise.
        """
        if self.has_three_of_a_kind() and self.count_pairs() >= 2:
            return True
        return False
        
    def has_four_of_a_kind(self):
        """Returns True if the hand has 4 of a kind, False otherwise.
        """
        for rank in self.ranks:
            if self.ranks[rank] >= 4:
                return True
        return False
        
    def has_straight_flush(self):
        """Returns True if the hand has straight flush, False otherwise.
        """
        if self.has_flush() and self.has_straight():
            return True
        return False
        
    hand_order = [has_straight_flush, has_four_of_a_kind, has_full_house, has_flush, has_straight, has_three_of_a_kind, has_twopair, has_pair]
    
                                
    def classify(self):
        for i in range(8):
            if self.hand_order[i](self):
                frequency_of_poker_hands[i] += 1
                break
    
if __name__ == '__main__':
    
    #deal the cards and classify the hands
    for i in range(1000000):
        #make a deck
        deck = Deck()
        deck.shuffle()
        hand = PokerHand()
        deck.move_cards(hand, 5)
        hand.sort()
        hand.rank_hist()
        hand.suit_hist()
        hand.classify()
    
    print [float(value)/10000 for value in frequency_of_poker_hands.values()]
        
    #print frequency_of_poker_hands
    # hand = PokerHand()
    # card1 = Card(1, 1)
    # card2 = Card(2, 1)
    # card3 = Card(3, 1)
    # card4 = Card(0, 1)
    # card5 = Card(1, 5)

    # hand.add_card(card1)
    # hand.add_card(card2)
    # hand.add_card(card3)
    # hand.add_card(card4)
    # hand.add_card(card5)
    # hand.rank_hist()
    # hand.suit_hist()
    # print hand
    # print hand.has_three_of_a_kind()