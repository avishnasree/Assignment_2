#Question 5:Write a python program to print positive numbers in a list


# Method 1: Using a for loop
numbers = [-2, 3, -4, 5, -6, 7, 8]

print("Positive numbers in the list:")
for num in numbers:
    if num > 0:
        print(num)
