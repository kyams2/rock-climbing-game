"""
UNIT TEST 1 NARRATIVE OF CURRENT CODE (NO INPUT DATA)

Currently, have completed the coding for the first class out of three. This is the Player class.
This class has two functions with it (excluding def __init__):

The def move_player function has set each key in "w, a, s, d" to a specific direction that the character would be moving in. 
"w" makes the character move up, "s" is down, "a" is left, and "d" is right. After defining the letter to the general direction, 
it is crucial to assign which specific direction it will me moving. Underneath each "if" or "elif" statement, this is where I 
assigned each specific direction with "self.row" or "self.column" and it should check out.

The get_energy function is coded for the character to receive or lose energy. "if" the character is resting/stopped, 
it will gain two energy points but if the character is moving/not resting, the character will lose one energy point.
"""
