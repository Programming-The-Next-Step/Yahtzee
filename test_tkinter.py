#tkinter
import tkinter as tk 
import classes as c
import numpy as np



class TEST(tk.Frame):
    def __init__(self, parent):
        super().__init__()
        self.parent = parent

        self.dice_frame = tk.Frame(root, bg = 'white', height = 150) 
        self.choice_frame = tk.Frame(root, bg = 'white', height = 100)
        self.scorecard_frame = tk.Frame(root,  height = 350)
        self.us_frame = tk.Frame(self.scorecard_frame)
        self.us_left_frame = tk.Frame(self.us_frame, bg = 'darkgreen')
        self.us_right_frame = tk.Frame(self.us_frame, bg = 'green')
        self.ls_frame = tk.Frame(self.scorecard_frame)
        self.ls_left_frame = tk.Frame(self.ls_frame, bg = 'darkgreen')
        self.ls_right_frame = tk.Frame(self.ls_frame, bg = 'green')
        
        self.dice_frame.pack(side = TOP, fill = BOTH)
        self.scorecard_frame.pack(side = TOP, fill = BOTH, expand = True) 
        self.choice_frame.pack(side = BOTTOM, fill = BOTH)
        self.us_frame.pack(side = LEFT, fill = BOTH, expand = True) 
        self.us_left_frame.pack(side = LEFT, fill = BOTH, expand = True)
        self.us_right_frame.pack(side = RIGHT, fill = BOTH, expand = True)
        self.ls_frame.pack(side = RIGHT, fill = BOTH, expand = True) 
        self.ls_left_frame.pack(side = LEFT, fill = BOTH, expand = True)
        self.ls_right_frame.pack(side = RIGHT, fill = BOTH, expand = True)
        
        self.Scorecards = []
        self.currentScorecard = c.Scorecard()
        self.dice = c.Dice()
        self.throw_again_dices = []
        
        self.dice_button1 = tk.Button(self.dice_frame, text=str(self.dice.current_throw[0]), command=lambda: self.choose_dice(1))
        self.dice_button2 = tk.Button(self.dice_frame, text=str(self.dice.current_throw[1]), command=lambda: self.choose_dice(2))
        self.dice_button3 = tk.Button(self.dice_frame, text=str(self.dice.current_throw[2]), command=lambda: self.choose_dice(3))
        self.dice_button4 = tk.Button(self.dice_frame, text=str(self.dice.current_throw[3]), command=lambda: self.choose_dice(4))
        self.dice_button5 = tk.Button(self.dice_frame, text=str(self.dice.current_throw[4]), command=lambda: self.choose_dice(5))
        
        self.dice_button1.pack(side = LEFT, fill = BOTH, expand = True)
        self.dice_button2.pack(side = LEFT, fill = BOTH, expand = True)
        self.dice_button3.pack(side = LEFT, fill = BOTH, expand = True)
        self.dice_button4.pack(side = LEFT, fill = BOTH, expand = True)
        self.dice_button5.pack(side = LEFT, fill = BOTH, expand = True)     
        
        self.roll_button = tk.Button(self.choice_frame, text="Roll again", command=lambda: self.testt())
        self.roll_button.pack(side = LEFT, fill = BOTH, expand = True)

           
    def choose_dice(self, number):
         if number in self.throw_again_dices:
             self.throw_again_dices.remove(number)
         else:
             self.throw_again_dices.append(number)
    
    def update_buttontext(self):
        self.dice_button1.config(text=str(self.dice.current_throw[0]))
        self.dice_button2.config(text=str(self.dice.current_throw[1]))
        self.dice_button3.config(text=str(self.dice.current_throw[2]))
        self.dice_button4.config(text=str(self.dice.current_throw[3]))
        self.dice_button5.config(text=str(self.dice.current_throw[4]))
        
    
    def testt(self):
        self.dice.roll(self.throw_again_dices)
        self.update_buttontext()        
        self.throw_again_dices = []
        








#create a blank frame
root = tk.Tk()
root.geometry('400x600')
root.configure(background='darkgreen')
app = TEST(root)
root.mainloop()
root.quit()