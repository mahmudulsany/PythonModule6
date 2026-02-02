#Modify the function above so that it gets the number of sides on the dice as a parameter.
#With the modified function you can for example roll a 21-sided role-playing dice.
#The difference to the last exercise is that the dice rolling in the main program continues
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.

import random
def dice_roll(sides):
    dice_side=random.randint(1,sides)
    return dice_side
max_dice_num= int(input("Enter the maximum number of sides: "))
result=0
while result!= max_dice_num:
    result=dice_roll(max_dice_num)
    print(f"The rolling result is {result}")