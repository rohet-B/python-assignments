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