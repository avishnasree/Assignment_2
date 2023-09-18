#Question 7:Write a python program to covert Fahrenheit to Celsius.

fahrenheit = float(input("Enter temperature in Fahrenheit: "))

celsius = (fahrenheit - 32) * 5/9

print(f"{fahrenheit} degrees Fahrenheit is equal to {celsius:.2f} degrees Celsius")
