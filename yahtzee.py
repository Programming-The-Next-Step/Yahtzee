#import packages
from random import randint
import numpy as np
import pygame as pg

'''  Check classes tomorrow for DiceSet?
class Dice:
    def __init__(self, value):
        self.value = value        
 '''      


num_throws = 3
num_dice = 5
dice = np.zeros([num_dice])
for i in range(0, num_throws):
    if i == 0:
        throw_again_idx = range(0, len(dice))
    else:
        throw_again_idx = np.array([int(i) - 1 for i in input().split()])
  
    for j in throw_again_idx:
            dice[j] = randint(1, 6)   
            
    print('Do you want to keep these dice, press k?: ', dice)  
    
    if input() == 'k':
            break