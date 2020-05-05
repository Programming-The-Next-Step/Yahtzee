
<h1>Yahtzee</h1>
<h2>Introduction</h2>

*Yahtzee* is a chance and strategic dice game. In this game participants can score points by rolling five dice. The players of the game have to decide whether they want to combine the dice into a score, or whether they roll the dice again. The dice can be rolled up to three times in one turn. The scoring categories (see: [Upper Section Categories](https://en.wikipedia.org/wiki/Yahtzee#Upper_section) and [Lower Section Categories](https://en.wikipedia.org/wiki/Yahtzee#Lower_section)) have varying point values, some of which are fixed and others have to be calculated. The winner of the game is the one with most points.
<br/>
According to [MoSCoW](https://en.wikipedia.org/wiki/MoSCoW_method) method: 

*Must have* – short on time| *Should have* – goal  | *Could have* – extra time  | *Won’t have* n/a  
--------------|-------------------|-------------------|-------------------
The functionality to roll 5 dice and to present the result of each dice roll (numeric)  | Players fill in scorecard at possible category  | Easy mode Yahtzee, where the computer helps to play the game (giving percentages of the possible chances of obtaining a category with an extra roll)| multiplayer game online
Being able to roll the dice up to three times in one turn  | Calculate the scores automatically based on category of choice and dice values  | Randomize the player who is starting the game  |
Select the dice that you want to keep, and select the dice to roll again  |Visual representation of the (sorted) dice (as real dice)  ||
Scorecard presentation  | multiplayer game (offline)||
One-player game (offline)  |||
An instruction at the start of the game|||



<h2>Implementation</h2>
I will start with making the must haves. I am using Python for this project, because I think it is more flexible to use when making a game.
<br/><br/>
The packages I will definitely use:

 - Numpy: for the basic array operations   
 - Random: for creating the random dice rolls 
- Pygame: a package used for visualization of games
- Os: to load images from local drive on computer

<h2>Flowchart</h2>

 - Function to present instruction of the game
 - Function to roll the 5 Dice
 - Function to present Dice
 - Function in which player can select the dice that should be rolled again and which      should be left on the ‘table’.
 - Function to roll again with selected dice, if applicable
 - Function to assign result to Category
 - Function to calculate scores in ScoreCard
 - Function to present updated ScoreCard
 - Function to clean all results and start new turn (switch turn for more players)