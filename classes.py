#import packages
from random import randint
import numpy as np
import pandas as pd

#define the Dice class
class Dice:
    """
    A class used to represent the five dice
    
    ...
    
    Attributes
    ----------
    current_throw : list
        List of integers of the five dice
        
    Methods
    ----------
    roll(throw)
        Assigns random integers to current_throw 
    """
    
    def __init__(self):
        self.current_throw = [randint(1, 6) for i in range(0, 5)]   
        
    def roll(self, throw):
        for j in [int(i) - 1 for i in throw]:
            self.current_throw[j] = randint(1, 6)
    
    def manual_set(self, a):
        self.current_throw = a
        
            
class Category():
    """
    A class used to check the possible categories in both upper and lower section.
    It also calculates the possible score per category and keeps track
    on whether the category is filled in a previous turn.
    
    ...
    
    Attributes
    ----------
    name : str
        Name of the category
    number: int
        Argument used to loop over the three of a kind, four of a kind and Yahtzee category
    possible_points: int
        The possible points for each category
    empty: bool
        Keeps track whether the category is empty
    
        
    Methods
    ----------
    score(current_throw)
        Assigns a score to each category still to be filled in and possible
        based on the current throw.
    """
    def __init__(self, name, number = 0):
        self.name = name
        self.number = number
        self.possible_points = 0
        self.empty = True
    def score(self, current_throw):                
        if self.empty:
            unique, counts = np.unique(current_throw, return_counts = True)
            if self.name in ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']:
                # assign possible_points (sum for occurance of specific number (e.g. 3 x fours))
                self.possible_points = int(np.sum([x for x in current_throw if x == self.number]))
                
            elif self.name in ['Three of a kind', 'Four of a kind', 'Yahtzee']: 
                # assign possible_points (sum of the numbers on the dice) if number occurs 3 or 4 times in the dice
                # assign possible_points (50) if number occurs 5 times in the diceset (Yahtzee)
                # else 0
                possible = any(counts >= self.number)                
                if possible and not self.name == 'Yahtzee':
                    self.possible_points = np.sum(current_throw)
                elif possible and self.name == 'Yahtzee':
                    self.possible_points  = 50
                else:
                    self.possible_points = 0 
                    
            elif self.name == 'Full house':
                # assign possible_points (25) if full house possible (2 of one number, three of one number)
                # else 0
                possible =  any(counts == 3) and any(counts == 2) and len(unique == 2)
                self.possible_points = 25 if possible else 0
                
            elif self.name == 'Small straight':
                # assign possible_points (30) if small straight is possible
                # else 0
                string_to_search = ''.join(map(str, np.unique(np.sort(current_throw)))) 
                possible = '1234' in string_to_search or '2345' in string_to_search or '3456' in string_to_search
                self.possible_points = 30 if possible else 0
                
            elif self.name == 'Large straight':
                # assign possible_points (40) if large straight is possible
                # else 0
                string_to_search = ''.join(map(str, np.sort(current_throw))) 
                possible = string_to_search in ['12345', '23456']                
                self.possible_points = 40 if possible else 0  
                
            else:
                # assign possible_points (sum of all dice). Always possible
                self.possible_points = np.sum(current_throw)
        else:
            self.possible_points = 0

class Scorecard:
    """
    A class used to show and update the scorecard per player per turn
    And prints the final result.
    With this class it is easy to add players to the game and to keep the state
    of the players.
    ...
    
    Attributes
    ----------
    categories : list
        List of Category for each type of category in the game
    scores: array
        The scores of each category (starting with 0) filled in each turn
    possiblescores:
        The scores that are possible based on the throw
    uppersection: int
        Sum of all scores of categories in the upper section
    lowersection: int
        Sum of all scores of categories in the lower section
    bonus: int
        The bonus which can be assigned, based on score in upper section (>= 63)
    total: int
        Sum of lower and upper section and bonus if applicable
        
    Methods
    ----------
    print_scorecard(show_possible_score)
        Prints the scorecard of the player.
        When show_possible_score is True, then print the possible scores too.
        If False, then only the category names and scores are printed
        
    update_possible_scores(current_throw)
        Updates the possiblescores attribute according to the current_throw.
        
    update_category(index)
        Updates the category - which is chosen by player - to True.
        
    print_final_result()
        Prints the lower- and uppersection scores with bonus if applicable.    
    """
    def __init__(self):
        self.categories = [     Category('Aces', 1),
                                Category('Twos', 2),
                                Category('Threes', 3),
                                Category('Fours', 4),
                                Category('Fives', 5),
                                Category('Sixes', 6),
                                Category('Three of a kind', 3),
                                Category('Four of a kind', 4),
                                Category('Full house'),
                                Category('Small straight'),
                                Category('Large straight'),
                                Category('Yahtzee', 5),
                                Category('Chance')                               
                          ]
        self.scores = np.zeros([len(self.categories)], '<U3')
        self.possiblescores = np.zeros([len(self.categories)], '<U3')
        self.categoryname = [category.name for category in self.categories]
        self.uppersection = 0
        self.lowersection = 0
        self.bonus = 0
        self.total = 0
    def print_scorecard(self, show_possible_scores):
        if show_possible_scores:
            scores = {'Categories': self.categoryname, 'Scores': self.scores, 'Possible scores': self.possiblescores}   
        else:
            scores = {'Categories': self.categoryname, 'Scores': self.scores}              
        df_scorecard = pd.DataFrame(data = scores, index = range(1, 14))
        print(df_scorecard, "\n")
    def update_possible_scores(self, current_throw):
        for i, category in enumerate(self.categories):
            category.score(current_throw)
            # keep track of possible records
            self.possiblescores[i] = str(category.possible_points) if category.empty else '' 
    def update_category(self, index):
        self.categories[index].empty = False
        self.scores[index] = self.categories[index].possible_points
    def print_final_result(self):
        self.uppersection = np.sum(self.scores[0:6].astype(int))
        if self.uppersection >= 63:
             self.bonus = 35
        self.lowersection = np.sum(self.scores[6:13].astype(int))
        self.total = self.uppersection + self.bonus + self.lowersection
         
        print('You scored:'+ '\n' + 'upper section: ' + str(self.uppersection) + '\n' +' + ', 'bonus score: ' + str(self.bonus)  + '\n' + ' + ' + 'lower section : ' + str(self.lowersection) + '\n' + '----------------------' + '\n' + 'Total: ' + str(self.total))