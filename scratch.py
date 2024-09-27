

# Example 1
# Create variables of different data types and then
# print the variable names, data types, and values.

# a = "Her name is "  # string
# b = "Isabella"      # string
# c = a + b           # string plus string makes string

# print(f"a: {type(a)} {a}")
# print(f"b: {type(b)} {b}")
# print(f"c: {type(c)} {c}")
# print()

# d = False  # boolean
# e = True   # boolean

# print(f"d: {type(d)} {d}")
# print(f"e: {type(e)} {e}")
# print()

# f = 15     # int
# g = 7.62   # float
# h = f + g  # int plus float makes float

# print(f"f: {type(f)} {f}")
# print(f"g: {type(g)} {g}")
# print(f"h: {type(h)} {h}")
# print()

# i = "True"   # string because of the surrounding quotes
# j = "2.718"  # string because of the surrounding quotes

# print(f"i: {type(i)} {i}")
# print(f"j: {type(j)} {j}")

#the TYPE in there defines which type of object is, this is why the results shows
#<class 'bla bla bla'>

# Example 2
# The input function always returns a string.
# k = input("Please enter a number: ")        # string
# m = input("Please enter another number: ")  # string
# n = k + m          # string plus string makes string
# print(f"k: {type(k)} {k}")
# print(f"m: {type(m)} {m}")
# print(f"n: {type(n)} {n}")
# print()
# # The int and float functions convert a string to a number.
# p = int(input("Please enter a number: "))          # int
# q = float(input("Please enter another number: "))  # float
# r = p + q                     # int plus float makes float
# print(f"p: {type(p)} {p}")
# print(f"q: {type(q)} {q}")
# print(f"r: {type(r)} {r}")

# Example 3
# Given the distance that a cable will span and the distance
# it will sag or dip in the middle, this program computes the
# length of the cable.
# Get user input and convert it from
# strings to floating point numbers.
# span = float(input("Distance the cable must span in meters: "))
# dip = float(input("Distance the cable will sag in meters: "))
# # Use the numbers to compute the cable length.
# length = span + (8 * dip**2) / (3 * span)
# # Print the cable length in the
# # console window for the user to see.
# print(f"Length of cable in meters: {length:.2f}")

#span means percorrer
#dip means ceder

# Example 4
# Compute the total price of a pizza.
# The base price of a large pizza is $10.95
#price = 10.95
# Ask the user for the number of toppings.
#number_of_toppings = int(input("How many toppings? "))
# Compute the cost of the toppings.
#price_per_topping = 1.45
#toppings_cost = number_of_toppings * price_per_topping
# Add the cost of the toppings to the price of the pizza.
#price = price + toppings_cost
# Print the price for the user to see.
#print(f"Price: ${price:.2f}")

from datetime import datetime

# first_name = "Thalyta"
# print("Task completed")
# print(datetime.datetime.now())
# print()

# for x in range(0,10):
#     print(x)
# print("Task Completed")
# print(datetime.datetime.now())
# print()

#Print the current time and task name

# def print_time(task_name):
#     print("task_name")
#     print(datetime.now())
#     print()

# first_name = "Thalyta"
# print_time("First name assigned")

# for x in range(1,11):
#     print(x)
# print_time("Loop Completed")


def get_initial(name):
    initial = name[0:1].upper()
    return initial

first_name = input("Enter your first name: ")
# first_name_initial = get_initial(first_name)
last_name = input("Entes your last name: ")
# last_name_initial = get_initial(last_name)

# print("Your initials are: " + first_name_initial + "." + last_name_initial + ".")

print("Your initials: " + get_initial(first_name) + "." + get_initial(last_name) + ".")

#Sincerelly, I like this thing about printing the def program, but I think it is easily to have it before the print statement.


from datetime import datetime

#function to print the current date and time
def print_time(task_name):
    print(task_name)
    print(datetime.now())
    print()

#print timestamps to see how long sections of code take to run

first_name = "Thalyta"
print_time("Printed first name")

for x in range(0,10):
    print(x)
print_time("Completed for loop")

#Ask for someones name and return the initials

#this function will return the first initial of a name
def get_initials(name, force_uppercase=True):
    if force_uppercase:
        initial = name [0:1].upper()
    else:
        initial = name[0:1]
    return initial

first_name = input("What is your first name? ")
first_name_initial = get_initials(first_name)

middle_name = input("What is your middle name? ")
middle_name_initial = get_initials(middle_name)

last_name = input("What is your last name? ")
last_name_initial = get_initials(last_name)

print("Your initials are: " + first_name_initial + "." + middle_name_initial + "." + last_name_initial + ".")