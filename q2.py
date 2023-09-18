#Question 2: Python program to find smallest number in a list.

# Sample list of numbers
numbers = [4, 2, 7, 1, 9, 5]

minimum = numbers[0]

for num in numbers:
    if num < minimum:
        minimum = num

print("The smallest number is:", minimum)
