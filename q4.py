#Question 4:Write a python program to print odd numbers in a list.

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Odd numbers in the list:")
for num in numbers:
    if num % 2 != 0:
        print(num)
