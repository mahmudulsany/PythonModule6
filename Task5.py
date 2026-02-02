#A function that gets a list of integers as a parameter.
#Function returns a 2nd list which is same as the original list except that all uneven numbers have been removed.
def remove_odd(numbers):
    new_list = []
    for x in numbers:
        if x % 2 == 0:
            new_list.append(x)
    return new_list

#The  program where you create a list.
my_list = [1, 2, 3, 4, 5, 6, 7]

#Call the function.
result = remove_odd(my_list)

#Print out both the original and cut-down list.
print(f"The original list: {my_list}")
print(f"The cut-down list: {result}")

