#Question 3:Write a python program to print even numbers in a list.


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

print("Even numbers in the list:")
for num in numbers:
    if num % 2 == 0:
        print(num,)
