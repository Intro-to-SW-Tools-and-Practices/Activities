# -*- coding: utf-8 -*-
"""
Created on Fri Jan 28 15:35:48 2022

@author: Brian Sun
"""
import Card
from random import shuffle

class Deck:
    
    cards=list()
    
    def __init__(self):
        self.cards = list()
        for values in range(13):
            for suits in range(4):
               self.cards.append(Card.Card(values,suits)) 
              
                
    def display(self):
        for c in self.cards:
            print(c.to_String())
                
    def shuffle(self):
        shuffle(self.cards)
    
    def draw(self):
        return self.cards.pop()
