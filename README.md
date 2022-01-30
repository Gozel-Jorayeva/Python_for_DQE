# Python_for_DQE
Python homework 

# Let's import Python's random module to generate random numbers
import random

# here is used random.sample() method to generate a list of unique random numbers (without duplicates)
random_numbers = random.sample(range(0, 1000), 100)

# iterating over "random_numbers"
for i in range(len(random_numbers)):
    # only iterate through the next numbers after i
    for j in range(i + 1, len(random_numbers)):
        # if current number is bigger than next (put them in ascending order)
        if random_numbers[i] > random_numbers[j]:
            # swap current and next numbers
            random_numbers[i], random_numbers[j] = random_numbers[j], random_numbers[i]

# creating list called "even" to add into it all even numbers from the sorted "random_numbers" list
even = []
# creating list called "odd" to add into it all odd numbers from the sorted "random_numbers" list
odd = []

# for all numbers from "random_numbers" list
for i in random_numbers:
    # try numbers one by one
    try:
        # if number from "random_numbers" list is divided to 2, and remainder is 0
        if i % 2 == 0:
            # then add that number to "even" list
            even.append(i)
    # if happens some another action/behaviour
    except:
        # raise an error
        raise NotImplementedError
    # try each number from "random_numbers" list
    try:
        # if number from "random_numbers" list is divided to 2, and remainder is 1
        if i % 2 == 1:
            # then add that number to "odd" list
            odd.append(i)
    # if happens some another action/behaviour
    except:
        # raise an error
        raise NotImplementedError

# print to console the text with paragraph(\n) and all random numbers from "random_numbers" list
print("""
1. Create list of 100 random numbers from 0 to 1000
2. Sort list from min to max
100 sorted random numbers are:\n""", random_numbers)


# Average is the arithmetic mean and calculated by adding a group of numbers and
# then dividing by the count of those numbers
# to find the average of even numbers:
# 1. all numbers inside the even list are added to each other
# 2. and their sum is divided to quantity of those numbers from the "even" list
# 3. and the result is assigned to "avg_even" variable
avg_even = sum(even) / len(even)
# sum of "odd" list divided to count of "odd" list and result assigned to "avg_odd" variable
avg_odd = sum(odd) / len(odd)
print(
    "\n3. Calculate average for even and odd numbers",
    "\nAverage for even numbers is:", avg_even,
    "\nAverage for odd numbers is:", avg_odd)

# check what even numbers are inside the "even" list
# print("\nEven numbers are:\n", even)
# check what odd numbers are inside the "odd" list
# print("\nOdd numbers are:\n", odd)


# Count how many odd numbers are in the "odd" list
# odd_count = len(odd)
# Count how many even numbers are in the "even" list
# even_count = len(even)


# Check that odd and even numbers addition is 100
# print("\nEven", even_count, "+ odd", odd_count, "=", even_count + odd_count)
