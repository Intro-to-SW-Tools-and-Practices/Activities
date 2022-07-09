# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:13:28 2022

@author: Brian Sun
"""

class Card:
    suits = ["spades", "hearts", "diamonds","clubs"]
    
    values = ["Ace","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
    # This defines how the class sets its values
    # Constructor
    def __init__(self,v,s):
        assert v <= 12, "value index out of bounds"
        assert s <= 3, "suit index out of bounds"
        self.value = v
        self.suit = s
        
    def to_String(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

    def get_value(self):
        return self.values[self.value]

    def get_suit(self):
        return self.suits[self.suit]
