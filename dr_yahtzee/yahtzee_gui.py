#tkinter
import tkinter as tk 
import dr_yahtzee.classes as c
import glob as glob
import os

DEFAULT_BUTTON_COLOUR = 'SystemButtonFace'
ROLL_AGAIN_COLOUR = 'red'
CATEGORY_COLOUR = 'white'
CATEGORY_FILLED_COLOUR = 'PaleGreen3'
BACKGROUND_COLOUR_1 = 'darkgreen'
BACKGROUND_COLOUR_2 = 'green'
CURRENT_WORKING_DIRECTORY = os.getcwd()
IMAGES_DIRECTORY = os.path.join(CURRENT_WORKING_DIRECTORY, 'Images')
INSTRUCTION_DIRECTORY = os.path.join(CURRENT_WORKING_DIRECTORY, 'Instruction')


class GUI_game:
    
    """
    A class used to create the GUI of the Yahtzee game. 
    
    ...
    
    Attributes
    ----------
    dice_filenames : list of str
        A list of the path directories of the dice images
    dice_images: list
        A 
    *_frame: tkinter.Frame
        All the attributes that end with _frame are defined to make different frames in the window.
        See below for the structure with all the frames
    Scorecards: list
        A list of the Scorecard() used to show and update the scorecard per player per turn. 
    currentScorecard: class
        Create a new scorecard, for the current player.
    dice: class
         A class used to represent the five dice.
    throw_again_dices: list
        An empty list that is filled with the dices/buttons that are pressed.    
    turn: int
        An integer that keeps track of the turn of the player.   
    dice_buttons: list
        List that is appended with the button that is created based on the throw.
    categories_labels: list
        List that creates the different labels of each category to present in the correct frame
    categories_buttons: list
        List that creates the different buttons to present categories at the correct frame
    *_label_name: tkinter.Label
        Creates a label for the uppersection, the lower section, the bonus and the total score
    *_label_score: tkinter.Label
        Creates a label with the current score on the uppersection, lowersection, bonus, and the total score
    *_button: tkinter.Button
        Creates a button in the choice frame. The buttons are to keep_dice(), to roll_(), to next_turn(),
        or to open a new window with the instruction()
        
    
    
    ----------   
    
    Structure of _frames:
    +--------------------------------------------------------------------------------------+
    |                                      dice_frame                                      |
    +--------------------------------------------------------------------------------------+
    |                                  player_name_frame                                   |
    +--------------------------------------------------------------------------------------+
    |                                   scorecard_frame                                    |
    |  +--------------------------------------+  +--------------------------------------+  |
    |  |              us_frame                |  |              ls_frame                |  |
    |  |  +---------------+----------------+  |  |  +---------------+----------------+  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  | up_left_frame | up_right_frame |  |  |  | ls_left_frame | ls_right_frame |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  |               |                |  |  |  |               |                |  |  |
    |  |  +---------------+----------------+  |  |  +---------------+----------------+  |  |
    |  |                                      |  |                                      |  |
    |  +--------------------------------------+  +--------------------------------------+  |
    |                                                                                      |
    +--------------------------------------------------------------------------------------+
    |                                    choice_frame                                      |
    +--------------------------------------------------------------------------------------+
    """
    
    def __init__(self, master):
        """
        Constructor for the GUI_game class. Takes the argument master.
        """
        
        super().__init__()
        self.master = master
        
        # opens and loads in the image files        
        self.dice_filenames = glob.glob(IMAGES_DIRECTORY + r'\dice*_white.png')
        self.dice_images = self.load_images(self.dice_filenames)            
        
        #creates all the frames (see structure of frames)
        self.dice_frame = tk.Frame(master) 
        self.player_name_frame = tk.Frame(master)
        self.scorecard_frame = tk.Frame(master)
        self.choice_frame = tk.Frame(master)
        self.us_frame = tk.Frame(self.scorecard_frame)
        self.us_left_frame = tk.Frame(self.us_frame)
        self.us_right_frame = tk.Frame(self.us_frame)
        self.ls_frame = tk.Frame(self.scorecard_frame)
        self.ls_left_frame = tk.Frame(self.ls_frame)
        self.ls_right_frame = tk.Frame(self.ls_frame)
    
        # pack the frames        
        self.dice_frame.pack(side = tk.TOP, fill = tk.BOTH)
        self.player_name_frame.pack(side = tk.TOP, fill = tk.BOTH)
        self.scorecard_frame.pack(side = tk.TOP, fill = tk.BOTH, expand = True) 
        self.choice_frame.pack(side = tk.BOTTOM, fill = tk.BOTH)
        self.us_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True) 
        self.us_left_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.us_right_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
        self.ls_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True) 
        self.ls_left_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.ls_right_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
                
        # Use the classes
        self.currentScorecard = c.Scorecard('__init__')
        self.dice = c.Dice()
        
        # Allocating some variables used below
        self.Scorecards = []
        self.throw_again_dices = []
        self.turn = 1
        self.players_turn = 0
        self.dice_buttons = []        
        self.categories_labels = []
        self.categories_buttons = []
        
        for i in range(0, len(self.dice.current_throw)):
            # i+1 for dice.roll indices
            # create a new dice_button in the loop.
            self.dice_buttons.append(tk.Button(self.dice_frame, bg = DEFAULT_BUTTON_COLOUR, state = 'disabled', command = lambda c=i: self.choose_dice(c+1)))
            self.dice_buttons[i].pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
            
        for i, category in enumerate(self.currentScorecard.categoryname):
            # for-loop to make sure that all the category labels belonging to the
            # uppersection are placed in the right frame and the lowersection categories
            # are placed in the left frame
            label_frame = self.us_left_frame if i < 6 else self.ls_left_frame                
            self.categories_labels.append(tk.Label(label_frame, text=category, bg = CATEGORY_COLOUR))
            self.categories_labels[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            button_frame = self.us_right_frame if i < 6 else self.ls_right_frame                     
            self.categories_buttons.append(tk.Button(button_frame, text='', state = 'disabled', command = lambda c=i: self.choose_category(c)))
            self.categories_buttons[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        #create label for displaying name of player
        self.player_name_label = tk.Label(self.player_name_frame, text = '', bg = 'cyan3')
        self.player_name_label.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
        # create two labels with the score and the name of the uppersection categories
        self.uppersection_label_name = tk.Label(self.us_left_frame, text = 'Upper section score', bg = CATEGORY_COLOUR)
        self.uppersection_label_score = tk.Label(self.us_right_frame, text = '0', bg = CATEGORY_COLOUR)
        self.uppersection_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.uppersection_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        
        # create two labels with the score and the name of the bonus category
        self.bonus_label_name = tk.Label(self.us_left_frame, text = 'Bonus', bg = CATEGORY_COLOUR)
        self.bonus_label_score = tk.Label(self.us_right_frame, text = '0', bg = CATEGORY_COLOUR)
        self.bonus_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)        
        self.bonus_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)    
        
        # create two labels with the score and the name of the lowersection categories
        self.lowersection_label_name = tk.Label(self.ls_left_frame, text = 'Lower section score', bg = CATEGORY_COLOUR)
        self.lowersection_label_score = tk.Label(self.ls_right_frame, text = '0', bg = CATEGORY_COLOUR)
        self.lowersection_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)        
        self.lowersection_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)  
        
        # create two labels with the score and the name of the total score
        self.total_label_name = tk.Label(self.ls_left_frame, text = 'Total score', bg = CATEGORY_COLOUR)
        self.total_label_score = tk.Label(self.ls_right_frame, text = '0', bg = CATEGORY_COLOUR)
        self.total_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.total_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)  

        # Create the buttons in the choice frame. roll_button uses the roll_dice function to roll the selected dice, keep_button uses the keep_dice function
        # to keep all the dice, turn_button uses the next_turn function to go to the next turn, and instruction_button uses the function instruction
        # to open the instruction in a new window when pressed.
        self.roll_button = tk.Button(self.choice_frame, text = "Roll again", state = 'disabled', command = lambda: self.roll_dice())
        self.roll_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.keep_button = tk.Button(self.choice_frame, text = "Keep all the dice", state = 'disabled', command = lambda: self.keep_dice())
        self.keep_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.turn_button = tk.Button(self.choice_frame, text = "Next turn!", state = 'disabled', command = lambda: self.next_turn())
        self.turn_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.instruction_button = tk.Button(self.choice_frame, text = '?', width = 5, state = 'disabled', command = lambda: self.instruction())
        self.instruction_button.pack(side = tk.LEFT)
        
        
        self.players_window = None
        self.player_names_entry = []
        self.init_player_names()
        

    def load_images(self, filenames):
        """
        Function that loads in images according to filenames
        """
        images = []
        for i, filename in enumerate(filenames):
            images.append(tk.PhotoImage(file = filename, master = self.master)) 
        return images
    
            
    def init_player_names(self):
        """
        Function to initialize the players such that the players can fill in their names.
        """
        self.players_window = tk.Toplevel(self.master)
        self.players_window.geometry('300x300')
        self.players_window.title('Enter player names')
        #making sure the player window is presented on the foreground.
        self.players_window.attributes('-topmost', 'true')
        self.player_name_new_entry(1)
        play_button = tk.Button(self.players_window, text = 'Play!', command = lambda: self.start_to_play())
        play_button.pack(side = tk.BOTTOM, fill = tk.X )

    def instruction(self):
        """
        Function that opens an extra window with Yahtzee instructions when the ? button is pressed. 
        """
        instruction_text = open(INSTRUCTION_DIRECTORY + r'\Instruction_text.txt')
        print_instruction_text = instruction_text.read()
        instruction = tk.Toplevel(self.master)
        instruction.geometry('1300x530')
        instruction.title('Instruction')
        instruction_label = tk.Label(instruction, text = print_instruction_text)
        instruction_label.pack()
        
    def choose_dice(self, number):
        """
        Function that allows to click on the button, which you want to replace. 
        It also keeps track of the indices of the dices that are clicked.
        """
        if number in self.throw_again_dices:
            self.throw_again_dices.remove(number)
            self.dice_buttons[number - 1].config(bg = DEFAULT_BUTTON_COLOUR)
        else:
            self.throw_again_dices.append(number)
            self.dice_buttons[number - 1].config(bg = ROLL_AGAIN_COLOUR)
    
    def update_button_images(self):
        """
        Updates the dice images
        """
        for i, button in enumerate(self.dice_buttons):
            #For example, dice.current_throw[3] equals 2 then 2 minus 1 because 
            #the image of dice with 2 eyes is in dice_images[1] (one index lower)
            button.config(image=self.dice_images[self.dice.current_throw[i] - 1])            
            button.config(text=str(self.dice.current_throw[i]))
           
    def roll_dice(self):
        """
        Function that keeps track of the turns per player (3 max.) and rolls the dices again.
        Lastly, the function sets the environment back to start-position.
        """
        self.turn += 1
        self.dice.roll(self.throw_again_dices)
        self.update_button_images()        
        self.throw_again_dices = []
        self.default_color_buttons(self.dice_buttons)
        if self.turn == 3:
            self.keep_dice()
            
    def disable_buttons(self, button_set):
        """
        Function that disables buttons.
        Takes in the argument button_set, which is an array of buttons.
        """
        for i, button in enumerate(button_set):
             button.config(state = 'disabled')     
             
    def enable_buttons(self, button_set):
        """
        Function that enables buttons.
        Takes in the argument button_set, which is an array of buttons.
        """
        for i, button in enumerate(button_set):
             button.config(state = 'active')         
            
    def default_color_buttons(self, button_set):
        """
        Function that sets the colour of a button_set to the default colour.
        Takes in the argument button_set, which is an array of buttons.
        """
        for i, button in enumerate(button_set):
             button.config(bg = DEFAULT_BUTTON_COLOUR)       
    
    def display_possible_scores(self):
        """
        Function that displays possible scores per category for current scorecard.
        """
        for i, category in enumerate(self.currentScorecard.categories):
            if category.empty:
                self.categories_buttons[i].config(text=str(self.currentScorecard.possiblescores[i])) 
        
    def keep_dice(self):
        """
        Function that sets the environment to the current state. And shows
        updates of the possible scores per category.
        """
        self.disable_buttons([self.roll_button, self.keep_button])
        self.default_color_buttons(self.dice_buttons)
        self.disable_buttons(self.dice_buttons)
        self.currentScorecard.update_possible_scores(self.dice.current_throw)
        self.display_possible_scores()
        for i, category in enumerate(self.currentScorecard.categories):
            if category.empty:
                self.enable_buttons([self.categories_buttons[i]])
        
    def display_scores(self):
        """
        Function that displays actual scores per category for current scorecard.
        """
        for i, category in enumerate(self.categories_buttons):
            category.config(text=str(self.currentScorecard.scores[i]))
            
    def update_label_scores(self):
        """
        Updates upper and lower section scores, and the bonus and total scores labels for the current scorecard
        """
        self.uppersection_label_score.config(text = str(self.currentScorecard.uppersection))
        self.lowersection_label_score.config(text = str(self.currentScorecard.lowersection))
        self.bonus_label_score.config(text = str(self.currentScorecard.bonus))
        self.total_label_score.config(text = str(self.currentScorecard.total))
            
    def choose_category(self, index):
        """
        Function that allows player to choose a category.
        Updates upper and lower section scores, and the bonus and total scores labels.
        Takes the argument index, which is the index of the chosen category.
        """
        self.currentScorecard.update_category(index)
        self.display_scores()
        self.categories_buttons[index].config(bg = CATEGORY_FILLED_COLOUR)
        self.disable_buttons(self.categories_buttons)
        self.enable_buttons([self.turn_button])
        self.update_label_scores()
        
    def check_filled_scorecard(self):
        """
        Checks whether all categories are filled in each scorecard of the players.
        Returns bool
        """
        for scorecard in self.Scorecards:
            for category in scorecard.categories:
                if category.empty:
                    return False
        return True
    
    def next_turn(self):
        """
        Function that makes sure that the new turn is created: sets environment for next player.
        """
        if not self.check_filled_scorecard():
            self.enable_buttons(self.dice_buttons)
            self.enable_buttons([self.roll_button, self.keep_button])
            self.disable_buttons([self.turn_button])
            self.update_button_images()
            self.turn = 1
            self.players_turn += 1
            self.next_player()
        #At the end of all the turns, the player can end the game by clicking the turn_button
        elif self.turn_button.cget('text') == 'Show final results':
            self.final_scores()
            self.disable_buttons([self.turn_button])
        else:
            self.turn_button.config(text = 'Show final results')      
        
    def player_name_new_entry(self, number):
        """
        Function that enables players to add their names in new entries up to 4 players.
        Takes in the argument number, which is used to count the number of players.
        """
        # Maximum number of players fixed to 4
        if number <= 4:
            player_frame = tk.Frame(self.players_window)
            player_frame.pack(side = tk.TOP, fill = tk.BOTH)
            player_names_label = tk.Label(player_frame, text = 'Player ' + str(number) + ':')
            player_names_label.pack(side = tk.LEFT)
            self.player_names_entry.append(tk.Entry(player_frame))
            self.player_names_entry[number - 1].pack(side = tk.LEFT)
            player_names_button = tk.Button(player_frame, text = '+', command = lambda: self.player_name_new_entry(number + 1))
            player_names_button.pack(side = tk.LEFT)
            
    def start_to_play(self):
        """
        Function that enables that the player can start the game, sets the environment.
        """
        for entry in self.player_names_entry:
            self.Scorecards.append(c.Scorecard(entry.get()))   
        self.players_window.destroy()
        # enable all required buttons
        self.enable_buttons(self.dice_buttons)
        self.enable_buttons([self.roll_button, self.keep_button, self.instruction_button])
        
        self.next_player()
        
    def next_player(self):
        """
        Function that assigns the current scorecard and sets the environment.
        """
        self.currentScorecard = self.Scorecards[self.players_turn % len(self.Scorecards)]
        self.dice = c.Dice()
        self.display_scores()
        self.update_button_images()
        self.default_color_buttons(self.categories_buttons)
        self.update_label_scores()
        self.player_name_label.config(text = 'Scorecard of ' + self.currentScorecard.name)
    
    def final_scores(self):
        """
        Function that opens an extra window with the final results of the game. 
        """
        
        sorted_scorecards = sorted(self.Scorecards, key = c.Scorecard.get_total, reverse = True)        
        
        final_results = tk.Toplevel(self.master)
        final_results.geometry('300x300')
        final_results.title('And the winner is...')
        
        for i, scorecard in enumerate(sorted_scorecards):
            color = CATEGORY_FILLED_COLOUR if i == 0 else DEFAULT_BUTTON_COLOUR
            total_score_frame = tk.Frame(final_results)
            total_score_frame.pack(side = tk.TOP, fill = tk.BOTH)
            total_score_rank_label = tk.Label(total_score_frame, text = str(i + 1), bg = color)
            total_score_name_label = tk.Label(total_score_frame, text = str(scorecard.name), bg = color)
            total_score_total_label = tk.Label(total_score_frame, text = str(scorecard.total), bg = color)
            total_score_rank_label.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
            total_score_name_label.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
            total_score_total_label.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
            
        quit_button = tk.Button(final_results, text = 'Quit!', command = lambda: self.quit())
        quit_button.pack(side = tk.BOTTOM, fill = tk.X )
        
    def quit(self):
        """
        Function to exit the game by destroying the master (root).
        """
        self.master.destroy()


def gui_game():
    """
    #Function to start the game in the GUI.
    """
    root = tk.Tk()
    root.geometry('600x600')
    root.title('Yahtzee!')
    root.configure(background = BACKGROUND_COLOUR_1)
    app = GUI_game(root)
    root.mainloop()