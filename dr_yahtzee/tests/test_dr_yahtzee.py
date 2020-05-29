import unittest
import dr_yahtzee.classes as y

class Test_package(unittest.TestCase):  
    
    def test_dice(self):
        """
        Tests whether the manual_set input is the same as the output.
        """
        test_diceset = [1,2,3,4,5]
        diceset = y.Dice()        
        diceset.manual_set(test_diceset)
        self.assertEqual(diceset.current_throw, test_diceset)

    def test_category(self):
        test_dicesets = [
                            [1, 1, 1, 1, 1],
                            [1, 2, 3, 4, 5],
                            [5, 2, 3, 1, 4],
                            [1, 2, 3, 4, 4],
                            [2, 2, 6, 6, 6],
                            [6, 6, 4, 5, 3]       
                        ]
        test_categories = [     y.Category('Aces', 1),
                                y.Category('Twos', 2),
                                y.Category('Threes', 3),
                                y.Category('Fours', 4),
                                y.Category('Fives', 5),
                                y.Category('Sixes', 6),
                                y.Category('Three of a kind', 3),
                                y.Category('Four of a kind', 4),
                                y.Category('Full house'),
                                y.Category('Small straight'),
                                y.Category('Large straight'),
                                y.Category('Yahtzee', 5),
                                y.Category('Chance')                               
                          ]           
        test_scores = [
                        #1      2       3       4       5       6      TK      FK      FH      SS      LS       YZ      CH
                        [5,	 	0,	 	0,	 	0,	 	0,	 	0,	 	5,	 	5,	 	0,	 	0,	 	0,		50,		5],
                        [1,	 	2,	 	3,	 	4,	 	5,	 	0,	 	0,	 	0,	 	0,	 	30,		40,		0,		15],
                        [1,	 	2,	 	3,	 	4,	 	5,	 	0,	 	0,	 	0,	 	0,	 	30,		40,		0,		15],
                        [1,	 	2,	 	3,	 	8,	 	0,	 	0,	 	0,	 	0,	 	0,	 	30,	 	0,		0,		14],
                        [0,	 	4,	 	0,	 	0,	 	0,	 	18,	 	22,	 	0,	 	25,	 	0,	 	0,		0,		22],
                        [0,	 	0,	 	3,	 	4,	 	5,	 	12,	 	0,	 	0,	 	0,	 	30,	 	0,		0,		24]
                    ]

        
        for i, test_diceset in enumerate(test_dicesets):
            for j, test_category in enumerate(test_categories):
                # loops over the different dicesets and categories and assesses whether the 
                # result is valid.
                test_category.score(test_diceset)
                self.assertEqual(test_category.possible_points, test_scores[i][j])
                
            
        
    def test_update_category(self):
        """
        Tests whether the scorecard updates correctly.
        """
        scorecard = y.Scorecard('UnitTest')
        diceset = [1,2,3,4,5]
        result = ['40', '0']
        index_small_straight = 9
        index_large_straight = 10
        for i in result:
            # test first time whether large straight is possible based on diceset
            # test second time whether large straight is possible, which should not be possible
            scorecard.categories[index_large_straight].score(diceset)            
            scorecard.update_category(index_large_straight)
            self.assertEqual(scorecard.scores[index_large_straight], i)
        # test whether another category (small straight) is possible           
        scorecard.categories[index_small_straight].score(diceset)
        scorecard.update_category(index_small_straight)
        self.assertEqual(scorecard.scores[index_small_straight], '30')
      
if __name__ == '__main__':
    unittest.main()       