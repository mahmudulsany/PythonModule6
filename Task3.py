#A function that gets the quantity of gasoline in US gallons and returns the number converted to liters.
def gasoline(gallons):
    liter= gallons*3.785
    return liter

#The program asks for a volume in gallons from the user.
V_gallon=0
while V_gallon>=0:
    V_gallon= float(input("Enter volume in gallons: "))

#Converts the value to liters.
    if V_gallon>=0:
        liter=gasoline(V_gallon)
        print(f"The gallon's volume in liter is {liter:.3f}")

#Conversions continue until the user inputs a negative value.
    else:
        print("Quit")


