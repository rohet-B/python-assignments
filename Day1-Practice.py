# Calculate area of a circle
import math 
radius = float(input("Enter value of radius: ")) 
area = math.pi*(radius**2) 
print(area)

# Converts Celsius to Fahrenheit 
temp = input("Enter the temperature") 
celsius = float(temp) 
formula = (celsius * (9/5))+32 
print(formula)

# Swapping 2 numbers
num1 = int(input("Enter first num: ")) 
num2 = int(input("Enter second num: ")) 
print("Num1 was: ",num1) 
print("Num2 was: ",num2) 
temp = num1 
num1 = num2 
num2 = temp 
print(num1) 
print(num2) 

# Take a decimal number as input (like 45.78) and output its integer part (45) and fractional part (.78)
decimal_num = float(input("Enter a float num: "))
print(int(decimal_num))
print(decimal_num-int(decimal_num))