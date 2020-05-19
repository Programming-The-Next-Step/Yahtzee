#import packages
from random import randint
import numpy as np
import pandas as pd

#define the Dice class
class Dice:
    def __init__(self):
        self.current_throw = [randint(1, 6) for i in range(0, 5)]       
    def roll(self, throw):
        for j in [int(i) - 1 for i in throw]:
            self.current_throw[j] = randint(1, 6) 
    def manual_set(self, a):
        self.current_throw = a
            
class Category():
    def __init__(self, name, number = 0):
        self.name = name
        self.number = number
        self.possible_points = 0
        self.empty = True
    def score(self, current_throw):                
        if self.empty:
            unique, counts = np.unique(current_throw, return_counts = True)
            if self.name in ['Aces', 'Twos', 'Threes', 'Fours', 'Fives', 'Sixes']:
                self.possible_points = int(np.sum([x for x in current_throw if x == self.number]))
                
            elif self.name in ['Three of a kind', 'Four of a kind', 'Yahtzee']:                
                possible = any(counts >= self.number)                
                if possible and not self.name == 'Yahtzee':
                    self.possible_points = np.sum(current_throw)
                elif possible and self.name == 'Yahtzee':
                    self.possible_points  = 50
                else:
                    self.possible_points = 0 
                    
            elif self.name == 'Full house':
                possible =  any(counts == 3) and any(counts == 2) and len(unique == 2)
                self.possible_points = 25 if possible else 0
                
            elif self.name == 'Small straight':
                string_to_search = ''.join(map(str, np.unique(np.sort(current_throw)))) 
                possible = '1234' in string_to_search or '2345' in string_to_search or '3456' in string_to_search
                self.possible_points = 30 if possible else 0
                
            elif self.name == 'Large straight':
                string_to_search = ''.join(map(str, np.sort(current_throw))) 
                possible = string_to_search in ['12345', '23456']                
                self.possible_points = 40 if possible else 0  
                
            else:
                self.possible_points = np.sum(current_throw)
        else:
            self.possible_points = 0

class Scorecard:
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