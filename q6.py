#Question 6:Write a python program to print negative numbers in a list.


numbers = [1, -2, 3, -4, 5, -6, 7, 8, -9]


print("Method 1: Using a for loop")
for num in numbers:
    if num < 0:
        print(num)