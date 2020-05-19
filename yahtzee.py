#import packages
import numpy as np
import pygame as pg
from win32api import GetSystemMetrics 
import classes as c


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
   


def game():
    """
    Function that can be used to play a game of Yahtzee. 
    The game can be played with multiple players.
    The scorecard of each player is updated in each turn.
        
    """

    # ask with how many players you want to play the game, assigns integer to num_players
    num_players = int(input('With how many players do you want to play Yahtzee?')) 
    # allocates the scorecard list for the number of players
    scorecards = [None] * num_players 
    for player in range(0, num_players):
        scorecards[player] = c.Scorecard()
    
    num_categories = len(scorecards[0].categories)
    
    for turn in range(0, num_categories * num_players):
        num_throws = 3
        for i in range(0, num_throws):
            # in the first roll, set the dice class
            if i == 0:
                dice = c.Dice()
            else:
                # ask which dices should be rolled again
                keep_dice = np.array(input('Press y if you want to keep all the dice, press any key if you want to roll the dice again '))
                # if the player want to keep all the dice, break the loop
                if keep_dice == 'y':
                    print('Your throw is: ', dice.current_throw)
                    break
                throw_again_idx = np.array(input('Which di(c)e would you like to roll again? use a space between the numbers (e.g. 1 2 5) ').split())
                # dice.roll (part of dice class) makes sure the correct indices (dice) are rolled again
                dice.roll(throw_again_idx) 
                
            print('Player ' + str(turn % num_players + 1) + ' rolled: ', dice.current_throw)
        
        # Use modulo to make sure the players can take turn and the correct scorecard is updated    
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
game()