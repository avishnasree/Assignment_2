#Question 10:Write a python program to create a list and use the following functions-append() and extend() len()

my_list = []

my_list.append(1)
my_list.append(2)
my_list.append(3)

extension_list = [4, 5, 6]
my_list.extend(extension_list)

list_length = 0
for _ in my_list:
    list_length += 1

print( my_list)
print("Length of List:", list_length)