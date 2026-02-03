
#The function calculates and returns the unit price of the pizza per square meter.
    price_per_sq_m= price/(3.1416*((diameter_cm/100)/2)**2)
    return price_per_sq_m

#The main program asks the user to enter the diameter and price of two pizzas.
diameter_cm = float(input("Enter the diameter of 1st pizza (cm): "))
price= float(input("Enter the price of 1st pizza (€): "))
Pizza_01=price_size(diameter_cm, price)

diameter_cm = float(input("Enter the diameter of 2nd pizza (cm): "))
price= float(input("Enter the price of 2nd pizza (€): "))
Pizza_02=price_size(diameter_cm, price)

#Tells the user which pizza provides better value for money.
if Pizza_01<Pizza_02:
    print("Pizza_01 is value for money.")
elif Pizza_01>Pizza_02:
    print("Pizza_02 is value for money.")
else:
    print("Both Pizza_01 and Pizza_02 are equal.")
