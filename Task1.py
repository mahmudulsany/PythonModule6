#A function that returns a random dice roll between 1 and 6.
#The function should not have any parameters.
import random
def dice_roll():
    dice = random.randint(1, 6)
    return dice

#Then program rolls the dice until the result is 6.
result=0
while result!=6:
    result=dice_roll()

#The main program should print out the result of each roll.
    print(f"Result: {result}")