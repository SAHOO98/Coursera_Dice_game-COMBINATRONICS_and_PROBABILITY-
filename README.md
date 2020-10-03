# Coursera_Dice_game-COMBINATRONICS_and_PROBABILITY-
Simulation of dice game explained below. For the course visit [here](https://www.coursera.org/learn/combinatorics). This program helps us to choose the best outcome.  
## The Question is as follows:
### Question Preview
In this series of three programming tasks, we will implement together a program that will play optimally in a tricky dice game! You program will be given a list of dices and will decide who chooses the dice first (you or your opponent).
When the dices are chosen, we will simulate 10000 throws. Each time your number is greater, you get $1 from your opponent. Conversely, each time your number is smaller, you pay $1 to your opponent. Your ultimate goal is to implement a program that always wins in such a simulation.
### First task:
Implement a function that takes two dices as input and computes two values: the first value is the number of times the first dice wins (out of all possible 36 choices), the second value is the number of times the second dice wins. We say that a dice wins if the number on it is greater than the number on the other dice
### Second task:
Now, your goal is to check whether among the three given dices there is one that is better than the remaining two dices.
Implement a function that takes a list of dices and checks whether there is dice (in this list) that is better than all other dices. We say that a dice is better than another one, if it wins more frequently (that is, out of all 36 possibilities, it wins in a cases, while the second one wins in b cases, and a>b). If there is such a dice, return its (0-based) index. Otherwise, return -1.
### Third task:
You are now ready to play!
Implement a function that takes a list of dices (possibly more than three) and returns a strategy. The strategy is a dictionary:
If, after analyzing the given list of dices, you decide to choose a dice first, set strategy["choose_first"] to True and set strategy["first_dice"] to be the (0-based) index of the dice you would like to choose
If you would like to be the second one to choose a dice, set strategy["choose_first"] to False. Then, specify, for each dice that your opponent may take, the dice that you would take in return. Namely, for each i from 0 to len(dices)-1, set strategy[i] to an index j of the dice that you would take if the opponent takes the i-th dice first.

## Test Cases:
test0 = [[1, 1, 6, 6, 8, 8], [2, 2, 4, 4, 9, 9], [3, 3, 5, 5, 7, 7]]  
test1 = [[3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [4, 4, 4, 4, 0, 0], [5, 5, 5, 1, 1, 1]]  
test2 = [[1, 1, 2, 4, 5, 7], [1, 2, 2, 3, 4, 7], [1, 2, 3, 4, 5, 6]]  
test3 = [[4, 4, 4, 4, 0, 0], [7, 7, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]  
test4 = [[1, 1, 4, 6, 7, 8], [2, 2, 2, 6, 7, 7], [3, 3, 3, 5, 5, 8]]  
test5 = [[1, 2, 3, 4, 5, 6],[1, 1, 2, 4, 5, 7],[1, 2, 2, 3, 4, 7]]  
test6 = [[4, 4, 4, 4, 0, 0], [3, 3, 3, 3, 3, 3], [6, 6, 2, 2, 2, 2], [5, 5, 5, 1, 1, 1]]  

I've added classes for for future uses.   
**Dice class**:- Generalised Dice class for handling anything related to Dice.    
**Oracle class**:- For coming up with the final strategy of wining.  
The orginal file, on which i was evaluted is also uploaded here as **First.py**  
