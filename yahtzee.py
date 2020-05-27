#import packages
import numpy as np
import classes as c


def game():
    """
    Function that can be used to play a game of Yahtzee. 
    The game can be played with multiple players.
    The scorecard of each player is updated in each turn.
        
    """

    # ask with how many players you want to play the game, assigns integer to num_players
    num_players = int(input('With how many players do you want to play Yahtzee? Enter a number in digits: ')) 
    name_players = input("Enter the names of the players separated by space: ")
    name_players_list = name_players.split()

    
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
                keep_dice = np.array(input('Press y if you want to keep all the dice, press any key if you want to roll the dice again: '))
                # if the player want to keep all the dice, break the loop
                if keep_dice == 'y':
                    print(current_scorecard.name + ' throw is: ', dice.current_throw)
                    break
                throw_again_idx = np.array(input('Which di(c)e would you like to roll again? use a space between the numbers (e.g. 1 2 5) ').split())
                # dice.roll (part of dice class) makes sure the correct indices (dice) are rolled again
                dice.roll(throw_again_idx) 
                
            print(current_scorecard.name + ' rolled: ', dice.current_throw)
        
        current_scorecard.update_possible_scores(dice.current_throw)
        current_scorecard.print_scorecard(show_possible_scores = True)    
        
        while True:     
            answer = int(input('Which Category do you like to fill in? ')) - 1
            if answer < 0 or answer >= 13:
                print('Write a number from 1 to 13')
            elif current_scorecard.categories[answer].empty:
                current_scorecard.update_category(answer)
                break
            else:
                print('Already filled, please try again...') 
                
        current_scorecard.print_scorecard(show_possible_scores = False)    
    
    for scorecard in scorecards:
        scorecard.print_final_result()
        
        
