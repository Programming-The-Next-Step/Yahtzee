#import packages
import numpy as np
import pygame as pg
from win32api import GetSystemMetrics 
import classes as c

"""
#set Display
pg.init()

display_width = GetSystemMetrics((0))
display_height = GetSystemMetrics((1))

#set colours
black = (0, 0, 0)
white = (255, 255, 255)

#initialize the display
gameDisplay = pg.display.set_mode((display_width,display_height))

#instruction
pg.display.set_caption('Yahtzee!')
font = pg.font.Font('freesansbold.ttf', 8) 
instruction = open('.\Instruction\Instruction_text.txt', 'r').read()
text = font.render(instruction, True, black)
textRect = text.get_rect()

while True : 
  
    # completely fill the surface object 
    # with white color 
    gameDisplay.fill(white) 
  
    # copying the text surface object 
    # to the display surface object  
    # at the center coordinate. 
    gameDisplay.blit(text, textRect)
    
    for event in pg.event.get() : 
  
        # if event object type is QUIT 
        # then quitting the pygame 
        # and program both. 
        if event.type == pg.QUIT : 
  
            # deactivates the pygame library 
            pg.quit() 
  
            # quit the program. 
            quit() 
  
        # Draws the surface object to the screen.   
        pg.display.update()  
"""    


num_players = int(input('With how many players do you want to play Yahtzee?'))
scorecards = [None] * num_players
for player in range(0, num_players):
    scorecards[player] = c.Scorecard()


for turn in range(0, 13 * num_players):    
    # present throw, ask input player, roll again
    num_throws = 3
    for i in range(0, num_throws):
        if i == 0:
            dice = c.Dice()
            #dice.manual_set([6,2,5,4,3])
        else:
            keep_dice = np.array(input('Press y if you want to keep all the dice, press any key if you want to roll the dice again '))
            if keep_dice == 'y':
                print('Your throw is: ', dice.current_throw)
                break
            throw_again_idx = np.array(input('Which di(c)e would you like to roll again? use a space between the numbers (e.g. 1 2 5) ').split())
            dice.roll(throw_again_idx)            
    
        print('You rolled: ', dice.current_throw)
        
    current_scorecard = scorecards[turn % num_players]   
    current_scorecard.update_possible_scores(dice.current_throw)
    current_scorecard.print_scorecard(show_possible_scores = True)    
    
    while True:     
        answer = int(input('Which Category do you like to fill in?')) - 1               
        if current_scorecard.categories[answer].empty:
            current_scorecard.update_category(answer)
            break
        else:
            print('Already filled, please try again...') 
            
    current_scorecard.print_scorecard(show_possible_scores = False)    

for player in range(0, num_players):
    scorecards[player].print_final_result()