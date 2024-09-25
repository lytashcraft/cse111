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
price = 10.95
# Ask the user for the number of toppings.
number_of_toppings = int(input("How many toppings? "))
# Compute the cost of the toppings.
price_per_topping = 1.45
toppings_cost = number_of_toppings * price_per_topping
# Add the cost of the toppings to the price of the pizza.
price = price + toppings_cost
# Print the price for the user to see.
print(f"Price: ${price:.2f}")