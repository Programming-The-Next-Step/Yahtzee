#import packages
import numpy as np
import dr_yahtzee.classes as c
import os

CURRENT_WORKING_DIRECTORY = os.getcwd()
INSTRUCTION_DIRECTORY = os.path.join(CURRENT_WORKING_DIRECTORY, 'Instruction')
instruction_text = open(INSTRUCTION_DIRECTORY + r'\Instruction_text.txt')
    
def try_cast_int(number):
    """
    Function that returns True when you can cast the number into an integer else it returns False
    Take in a type as parameter.
    """
    try:
        int(number)
        return True
    except ValueError:
        return False

def terminal_game():
    """
    Function that can be used to play a game of Yahtzee. 
    The game can be played with multiple players.
    The scorecard of each player is updated in each turn.
        
    """
    print(instruction_text.read())
    
    # ask with how many players you want to play the game, assigns integer to num_players
    while True:
        try:
            num_players = int(input('With how many players do you want to play Yahtzee? Enter a number in digits: ')) 
            break
        except ValueError:
            print("Enter the number in digits!")
    while True:
        name_players = input("Enter the names of the players separated by a space: ")
        name_players_list = name_players.split()
        if len(name_players_list) == num_players:
            break
        else:
            print('Please, give as many names as players ')
      
    # allocates the scorecard list for the number of players
    scorecards = [None] * num_players 
    for i, player_name in enumerate(name_players_list):
        scorecards[i] = c.Scorecard(player_name)
    
    num_categories = len(scorecards[0].categories)
    
    for turn in range(0, num_categories * num_players):
        
        # Use modulo to make sure the players can take turn and the correct scorecard is updated    
        current_scorecard = scorecards[turn % num_players] 
        
        num_throws = 3
        for i in range(0, num_throws):
            # in the first roll, set the dice class
            if i == 0:
                dice = c.Dice()
            else:
                # ask which dices should be rolled again
                keep_dice = np.array(input('Press y if you want to keep all the dice;\nPress q if you want to quit the game;\nPress any other key if you want to roll the dice again: '))
                # if the player want to keep all the dice, break the loop
                if keep_dice == 'y':
                    print(current_scorecard.name + ' throw is: ', dice.current_throw)
                    break
                if keep_dice == 'q':
                    return
                while True:
                    throw_again_idx = np.array(input('Which di(c)e would you like to roll again? Use a space between the numbers (e.g. if you want to throw the first and fifth dice again type : 1 5)  ').split())
                    test_throw = [try_cast_int(i) for i in throw_again_idx]
                    if all(test_throw):
                        break
                    else:
                        print("Enter the number in digits!")
                    
                # dice.roll (part of dice class) makes sure the correct indices (dice) are rolled again
                dice.roll(throw_again_idx) 
                
            print(current_scorecard.name + ' rolled: ', dice.current_throw)
        
        current_scorecard.update_possible_scores(dice.current_throw)
        current_scorecard.print_scorecard(show_possible_scores = True)    
        
        while True:
            try: 
                answer = int(input('Which Category do you like to fill in? ')) - 1
                if answer < 0 or answer >= 13:
                    print('Write a number from 1 to 13')
                elif current_scorecard.categories[answer].empty:
                    current_scorecard.update_category(answer)
                    break
                else:
                    print('Already filled, please try again...') 
            except ValueError:
                print("Enter the category in digits, presented before the categories")
         
    
    current_scorecard.print_scorecard(show_possible_scores = False)   
    
    
    for scorecard in scorecards:
        scorecard.print_final_result()