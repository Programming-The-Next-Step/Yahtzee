#import packages
from random import randint
import numpy as np
import pygame as pg

 
 #define the Dice class
class Dice:
    def __init__(self):
        self.current_throw = [randint(1, 6) for i in range(0, 5)]       
    def roll(self, throw):
        for j in [int(i) - 1 for i in throw]:
            self.current_throw[j] = randint(1, 6) 
    def manual_set(self, a):
        self.current_throw = a

# present throw, ask input player, roll again
num_throws = 3
for i in range(0, num_throws):
    if i == 0:
        player1 = Dice()
    else:
        keep_dice = np.array(input('Press y if you want to keep all the dice, press any key if you want to roll the dice again '))
        if keep_dice == 'y':
            print('Your throw is: ', player1.current_throw)
            break
        throw_again_idx = np.array(input('Which di(c)e would you like to roll again? use a space between the numbers (e.g. 1 2 5) ').split())

        player1.roll(throw_again_idx) 
        
        
    print('You rolled: ', player1.current_throw)


class Aces:
    def __init__(self):
        self.name = 'Aces'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(unique == 1):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 1])
        
class Twos:
    def __init__(self):
        self.name = 'Twos'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(unique == 2):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 2])

class Threes:
    def __init__(self):
        self.name = 'Threes'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(unique == 3):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 3])
        
class Fours:
    def __init__(self):
        self.name = 'Fours'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(unique == 4):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 4])
        
class Fives:
    def __init__(self):
        self.name = 'Fives'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(unique == 5):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 5])
        
class Sixes:
    def __init__(self):
        self.name = 'Sixes'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(unique == 6):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum([x for x in current_throw if x == 6])
        
class Three_of_kind:
    def __init__(self):
        self.name = 'Three of a kind'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts= np.unique(current_throw, return_counts = True)
        if any(counts >= 3):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum(current_throw)
            
class Four_of_kind:
    def __init__(self):
        self.name = 'Four of a kind'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        if any(counts >= 4):
            self.possible = True
    def score(self, current_throw):
        self.points = np.sum(current_throw)      

class Full_house:
    def __init__(self):
        self.name = 'Full House'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        if any(counts == 3) and any(counts == 2) and len(unique == 2):
            self.possible = True
    def score(self, current_throw):
        self.points = 25  

class Small_straight:
    def __init__(self):
        self.name = 'Small Straight'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        if len(unique) >= 4:
            self.possible = True
    def score(self, current_throw):
        self.points = 30  
    
class Large_straight:
    def __init__(self):
        self.name = 'Large Straight'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        if len(unique) == 5:
            self.possible = True
    def score(self, current_throw):
        self.points = 40 

class Yahtzee:
    def __init__(self):
        self.name = 'Yahtzee'
        self.possible = False
        self.points = 0
    def is_possible(self, current_throw):
        unique, counts = np.unique(current_throw, return_counts = True)
        if any(counts == 5):
            self.possible = True
    def score(self, current_throw):
        self.points = 50

class Chance:
    def __init__(self):
        self.name = 'Chance'
        self.possible = False
        self.points = 0
        self.filled = False
    def is_possible(self, current_throw):
        self.possible = True
    def score(self, current_throw):
        self.points = np.sum(current_throw)
        
     

aces = Aces()
twos = Twos()
threes = Threes()
fours = Fours()
fives = Fives()
sixes = Sixes()
three_of_kind = Three_of_kind()
four_of_kind = Four_of_kind()
full_house = Full_house()
small_straight = Small_straight()
large_straight = Large_straight()
chance = Chance()
yahtzee = Yahtzee()

scorecard = [aces, twos, threes, fours, fives, sixes, three_of_kind, four_of_kind, full_house, small_straight, large_straight, yahtzee, chance]

for i, category in enumerate(scorecard):
    category.is_possible(player1.current_throw)
    category.score(player1.current_throw)

    print(category.name, ' is possible: ', category.possible, 'points: ', category.points )





    
    
    
    