#A function that gets a list of integers as a parameter.
def sum(numbers):
    total = 0
    for x in numbers:
        total = total + x
    return total

#The function returns the sum of all the numbers in the list.
#The program where you create a list, call the function, and print out the value it returned.
list = [1, 2, 3, 4, 5, 6, 7]
result = sum(list)
print(result)

