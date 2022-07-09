# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:13:28 2022

@author: Brian Sun
"""

class Card:
    suits = ["spades", "hearts", "diamonds","clubs"]
    
    values = ["Ace","1","2","3","4","5","6","7","8","9","10","Jack","Queen","King"]
    
    def __init__(self,v,s): 
        
        # ERROR CODE
        # 13 would equal King
        # assert v <= 13, "value index out of bounds"
        
        # 3 would equal clubs
        # assert s <= 3, "suit index out of bounds"
        
        assert v not in range(14), "value index out of bounds"
        assert s not in range(4), "suit index out of bounds"
        
        self.value = v
        self.suit = s
        
    def to_String(self):
        return self.values[self.value] + " of " + self.suits[self.suit]

    def get_value(self):
        return self.values[self.value]
