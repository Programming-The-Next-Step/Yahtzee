#tkinter
import tkinter as tk 
import classes as c
import glob as glob

DEFAULT_BUTTON_COLOUR = 'SystemButtonFace'
ROLL_AGAIN_COLOUR = 'red'
CATEGORY_COLOUR = 'white'
CATEGORY_FILLED_COLOUR = 'PaleGreen3'
BACKGROUND_COLOUR_1 = 'darkgreen'
BACKGROUND_COLOUR_2 = 'green'

class TEST:
    def __init__(self, master):
        super().__init__()
        self.master = master
        
        self.dice_filenames = glob.glob(r'C:\Users\danar\GitHub\Yahtzee\Images\dice*_white.png')
        self.dice_images = self.load_images(self.dice_filenames)            

        self.dice_frame = tk.Frame(master, bg = 'white', height = 200) 
        self.choice_frame = tk.Frame(master, bg = 'white', height = 100)
        self.scorecard_frame = tk.Frame(master,  height = 300)
        self.us_frame = tk.Frame(self.scorecard_frame)
        self.us_left_frame = tk.Frame(self.us_frame, bg = 'darkgreen')
        self.us_right_frame = tk.Frame(self.us_frame, bg = 'green')
        self.ls_frame = tk.Frame(self.scorecard_frame)
        self.ls_left_frame = tk.Frame(self.ls_frame, bg = 'darkgreen')
        self.ls_right_frame = tk.Frame(self.ls_frame, bg = 'green')
        
        self.dice_frame.pack(side = tk.TOP, fill = tk.BOTH)
        self.scorecard_frame.pack(side = tk.TOP, fill = tk.BOTH, expand = True) 
        self.choice_frame.pack(side = tk.BOTTOM, fill = tk.BOTH)
        self.us_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True) 
        self.us_left_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.us_right_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
        self.ls_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True) 
        self.ls_left_frame.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.ls_right_frame.pack(side = tk.RIGHT, fill = tk.BOTH, expand = True)
        
        self.Scorecards = []
        self.currentScorecard = c.Scorecard()
        self.dice = c.Dice()
        self.throw_again_dices = []
        self.turn = 1
        self.dice_buttons = []        
        self.categories_labels = []
        self.categories_buttons = []
        
        for i in range(0,5):
            # i+1 for dice.roll indeces
            self.dice_buttons.append(tk.Button(self.dice_frame, bg = DEFAULT_BUTTON_COLOUR, command=lambda c=i: self.choose_dice(c+1)))
            self.dice_buttons[i].pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
            
        for i, category in enumerate(self.currentScorecard.categoryname):
            label_frame = self.us_left_frame if i < 6 else self.ls_left_frame                
            self.categories_labels.append(tk.Label(label_frame, text=category, bg = CATEGORY_COLOUR))
            self.categories_labels[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            button_frame = self.us_right_frame if i < 6 else self.ls_right_frame                     
            self.categories_buttons.append(tk.Button(button_frame, text='', state = 'disabled', command=lambda c=i: self.choose_category(c)))
            self.categories_buttons[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
        self.uppersection_label_name = tk.Label(self.us_left_frame, text='Upper section score', bg = CATEGORY_COLOUR)
        self.uppersection_label_score = tk.Label(self.us_right_frame, text='0', bg = CATEGORY_COLOUR)
        self.uppersection_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.uppersection_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.bonus_label_name = tk.Label(self.us_left_frame, text='Bonus', bg = CATEGORY_COLOUR)
        self.bonus_label_score = tk.Label(self.us_right_frame, text='0', bg = CATEGORY_COLOUR)
        self.bonus_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)        
        self.bonus_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)        
        self.lowersection_label_name = tk.Label(self.ls_left_frame, text='Lower section score', bg = CATEGORY_COLOUR)
        self.lowersection_label_score = tk.Label(self.ls_right_frame, text='0', bg = CATEGORY_COLOUR)
        self.lowersection_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)        
        self.lowersection_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)        
        self.total_label_name = tk.Label(self.ls_left_frame, text='Total score', bg = CATEGORY_COLOUR)
        self.total_label_score = tk.Label(self.ls_right_frame, text='0', bg = CATEGORY_COLOUR)
        self.total_label_name.pack(side = tk.TOP, fill = tk.BOTH, expand = True)
        self.total_label_score.pack(side = tk.TOP, fill = tk.BOTH, expand = True)                
        
        self.roll_button = tk.Button(self.choice_frame, text="Roll again", command = lambda: self.roll_dice())
        self.roll_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.keep_button = tk.Button(self.choice_frame, text = "Keep all the dice", command = lambda: self.keep_dice())
        self.keep_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.turn_button = tk.Button(self.choice_frame, text = "Next turn!", state = 'disabled', command = lambda: self.next_turn())
        self.turn_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        
        self.update_buttontext()
      
    def load_images(self, filenames):
        images = []
        for i, filename in enumerate(filenames):
            images.append(tk.PhotoImage(file = filename, master = self.master)) 
        return images
        
    def choose_dice(self, number):
         if number in self.throw_again_dices:
             self.throw_again_dices.remove(number)
             self.dice_buttons[number - 1].config(bg = DEFAULT_BUTTON_COLOUR)
         else:
             self.throw_again_dices.append(number)
             self.dice_buttons[number - 1].config(bg = ROLL_AGAIN_COLOUR)
    
    def update_buttontext(self):
        for i, button in enumerate(self.dice_buttons):
            button.config(image=self.dice_images[self.dice.current_throw[i] - 1])            
            button.config(text=str(self.dice.current_throw[i]))
           
    def roll_dice(self):
        self.turn += 1
        self.dice.roll(self.throw_again_dices)
        self.update_buttontext()        
        self.throw_again_dices = []
        self.default_color_dices()
        if self.turn == 3:
            self.keep_dice()
            
    def disable_buttons(self, button_set):
        for i, button in enumerate(button_set):
             button.config(state = 'disabled')     
             
    def enable_buttons(self, button_set):
        for i, button in enumerate(button_set):
             button.config(state = 'active')         
            
    def default_color_dices(self):
        for i, button in enumerate(self.dice_buttons):
             button.config(bg = DEFAULT_BUTTON_COLOUR)        
        
    def keep_dice(self):
        self.roll_button.config(state = 'disabled')
        self.keep_button.config(state = 'disabled')
        self.default_color_dices()
        self.disable_buttons(self.dice_buttons)
        self.currentScorecard.update_possible_scores(self.dice.current_throw)
        self.display_possible_scores()
        for i, category in enumerate(self.currentScorecard.categories):
            if category.empty:
                self.categories_buttons[i].config(state = 'active')
        
    def display_possible_scores(self):
        for i, category in enumerate(self.currentScorecard.categories):
            if category.empty:
                self.categories_buttons[i].config(text=str(self.currentScorecard.possiblescores[i]))     
        
    def display_scores(self):
        for i, category in enumerate(self.categories_buttons):
            category.config(text=str(self.currentScorecard.scores[i]))
            
    def choose_category(self, index):
        self.currentScorecard.update_category(index)
        self.display_scores()
        self.categories_buttons[index].config(bg = CATEGORY_FILLED_COLOUR)
        self.disable_buttons(self.categories_buttons)
        self.turn_button.config(state = 'active')
        self.update_label_scores()
    
    def update_label_scores(self):
        self.uppersection_label_score.config(text = str(self.currentScorecard.uppersection))
        self.lowersection_label_score.config(text = str(self.currentScorecard.lowersection))
        self.bonus_label_score.config(text = str(self.currentScorecard.bonus))
        self.total_label_score.config(text = str(self.currentScorecard.total))
    
    def check_filled_scorecard(self):
        for i, category in enumerate(self.currentScorecard.categories):
            if category.empty:
                return False
        return True
    
    def next_turn(self):
        if not self.check_filled_scorecard():
            self.enable_buttons(self.dice_buttons)
            self.roll_button.config(state = 'active')
            self.keep_button.config(state = 'active')
            self.turn_button.config(state = 'disabled')
            self.dice = c.Dice()
            self.update_buttontext()
            self.turn = 1
        elif self.turn_button.cget('text') == 'End game':
            root.destroy()
        else:
            self.turn_button.config(text = 'End game')
            
                

root = tk.Tk()
root.geometry('600x600')
root.configure(background = 'darkgreen')
app = TEST(root)
root.mainloop()

'''
def main():
    
    root = tk.Tk()
    root.geometry('400x600')
    root.configure(background='darkgreen')
    app = TEST(root)
    root.mainloop()

if __name__ == '__main__':
    main()
'''