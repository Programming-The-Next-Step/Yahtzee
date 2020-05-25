#tkinter
import tkinter as tk 
import classes as c

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
        self.buttons = []        
        self.categories_label = []
        self.categories_button = []
        
        for i in range(0,5):
            # i+1 for dice.roll indeces
            self.buttons.append(tk.Button(self.dice_frame, text=str(self.dice.current_throw[i]), bg = DEFAULT_BUTTON_COLOUR, command=lambda c=i: self.choose_dice(c+1)))
            self.buttons[i].pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
            
        for i, category in enumerate(self.currentScorecard.categoryname):
            label_frame = self.us_left_frame if i < 6 else self.ls_left_frame                
            self.categories_label.append(tk.Label(label_frame, text=category, bg = CATEGORY_COLOUR))
            self.categories_label[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True)
            
            button_frame = self.us_right_frame if i < 6 else self.ls_right_frame                     
            self.categories_button.append(tk.Button(button_frame, text='', command=lambda c=i: self.choose_category(c)))
            self.categories_button[i].pack(side = tk.TOP, fill = tk.BOTH, expand = True)
                
        
        self.roll_button = tk.Button(self.choice_frame, text="Roll again", command = lambda: self.roll_dice())
        self.roll_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        self.keep_button = tk.Button(self.choice_frame, text = "Keep all the dice", command = lambda: self.keep_dice())
        self.keep_button.pack(side = tk.LEFT, fill = tk.BOTH, expand = True)
        
    def choose_dice(self, number):
         if number in self.throw_again_dices:
             self.throw_again_dices.remove(number)
             self.buttons[number - 1].config(bg = DEFAULT_BUTTON_COLOUR)
         else:
             self.throw_again_dices.append(number)
             self.buttons[number - 1].config(bg = ROLL_AGAIN_COLOUR)
    
    def update_buttontext(self):
        for i, button in enumerate(self.buttons):
            button.config(text=str(self.dice.current_throw[i]))
           
    def roll_dice(self):
        self.turn += 1
        self.dice.roll(self.throw_again_dices)
        self.update_buttontext()        
        self.throw_again_dices = []
        self.default_color_dices()
        if self.turn == 3:
            self.keep_dice()
            
    def disable_button_dices(self):
        for i, button in enumerate(self.buttons):
             button.config(state = 'disabled')            
            
    def default_color_dices(self):
        for i, button in enumerate(self.buttons):
             button.config(bg = DEFAULT_BUTTON_COLOUR)        
        
    def keep_dice(self):
        self.roll_button.config(state = 'disabled')
        self.default_color_dices()
        self.disable_button_dices()
        self.currentScorecard.update_possible_scores(self.dice.current_throw)
        self.display_possible_scores()
        
    def display_possible_scores(self):
        for i, category in enumerate(self.categories_button):
            category.config(text=str(self.currentScorecard.possiblescores[i]))     
        
    def display_scores(self):
        for i, category in enumerate(self.categories_button):
            category.config(text=str(self.currentScorecard.scores[i]))
            
    def choose_category(self, index):
        self.currentScorecard.update_category(index)
        self.display_scores()
        self.categories_button[index].config(state = 'disabled')
        self.categories_button[index].config(bg = CATEGORY_FILLED_COLOUR)
                
        
        
        


root = tk.Tk()
root.geometry('400x600')
root.configure(background='darkgreen')
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