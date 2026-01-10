# Assignment Problems 

# Q1 Write a program that takes salary as input. Using conditional statements, calculate the final tax rate based on these rules:
# if salary < 30,000 -> 5 %
# if salary is 30,000-70,000 -> 15 %
# if salary > 70,000 -> 25 %
salary = int(input("Enter your salary: "))
if salary < 30000:
    print(f"You have to pay 5% tax on your salary that is {salary*(5/100)}")
elif salary >= 30000 and salary <=70000:
    print(f"You have to pay 15% tax on your salary that is {salary*(15/100)}")
else:
    print(f"You have to pay 25% tax on your salary that is {salary*(25/100)}")

# Q2 Write a function that takes two integers a and b and prints all even numbers between them(inclusive).
def even_no(start,end):
    for i in range(start,end+1):
        if(i%2==0):
            print(i)
even_no(1,6)

# Q3 Write a function that prints the digits of a number,n.
# For eg: n=312, there are 3 digits in it 3, 1 and 2 & we need to print them.
def print_digits(number):
    count = 0
    single_digits = ''
    while number > 0:
        # Rightmost digit find out
        single_digits += str(number % 10)
        # Count the number of digits
        count += 1
        # remove rightmost digit using interger division or normal division with int() type conversion
        number = number // 10
    print(f"There are {count} digits in it and they are: ", end = '')
    for i in reversed(single_digits):
        print(i, end=' ')
print_digits(1396702023)

# Q4 WAF to return the count of the number of digits in a number n.
def count_num(number):
    count = 0
    for i in str(number):
        count += 1
    print(f"Total number of digits in {number} is {count}.")
count_num(1396702023)    

# Q5 WAF to return the sum of digits of a number, n.
def sum_of_digits(n):
    sum = 0
    for i in str(n):
        digits = int(i) % 10
        sum += digits
    return sum
data = sum_of_digits(7678562717)
print(f"Sum of digits: {data}.")

# Q6 WAP to print all numbers from 1 to 100 that are divisible by both 3 and 5.
print("Numbers divisible by 3 and 5 from 1 to 100 are:")
for i in range(1,100+1):
    if i % 3 == 0 and i % 5 == 0:
        print(i)

# Q7 Design a program to continuously input a number n from user & print if it is positive or negativve until the user enters "Quit".
while(True):
    n = input("Enter a number: ")

    if n == "Quit":
        print("Quiting the app.")
        break
    else:
        num = int(n)
        if num < 0:
            print ("Negative Number.")
        elif num > 0:
           print("Positive Number.")
        elif num == 0:
            print("Neither positive nor negative.")

# Q8 Let's create a simple calculator that performs arithmetic operations. Create a function calculator (a, b operation) that performs addition, subtraction,
# multiplication or division based on the operation parameter. [Operation parameter can have values +, -, * & /]
def calculator(a,b,operation):
    if(operation == '+'):
        print(f"The sum of 2 numbers: {a + b}")
    elif(operation == '-'):
        print(f"The subtraction of 2 numbers: {a - b}")
    elif(operation == '*'):
        print(f"The multiplication of 2 numbers: {a * b}")
    elif operation == '/':
        print(f"The division of 2 numbers: {a / b}")
    else:
        print("Invalid operation.")

calculator(30,5,"/")

# Q9 Write a function is_prime(n) that returns true if n is a prime number and False otherwise, using a loop.
def is_prime(n):
    # a non-prime number n always get divided by atleast one number in range(2,n-1)
    # since n will be divisible by 1 always and by itself therefore we took that range
    for i in range(2,n-1):
        if (n%i == 0):
            return False
    # if not found any divisible number
    return True
data = is_prime(4)
print(data)

# Q10 Create a "Number Guessing Game". Given a secret number (already decided by you), wirte a program that asks the user to guess it and prints:
# Too high -> if the guess is above the number
# Too low -> if the guess is below
# Correct! -> if the guess match.
def guess_game(number):
    print(f"Hint: The number lies between {number - 10} and {number +10}")
    guess = int(input("Enter a guess number: "))
    while(guess != number):
        if(guess > number):
            print("Too High")
        else:
            print("Too low")
        guess = int(input("Enter your guess again: "))
    # if your guess is equal to number then loop exists and it'll be print
    print("Correct !")

number = 13
guess_game(number)