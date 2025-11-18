#DAY 2 of Python
# Conditional Statements:

# 1. if and else
age = 21
# Nesting example
if age != None: #if age not equal to none
    if(age>=18):
        print("You are eligible for vote.")
    else:
        print("You must be 18 years old to vote.")

# 2. elif
num1 = 10
num2 = 20
num3 = 30
if((num1>num2) and (num3 <num1)):
    print("Greater number is:",num1)
elif((num2>num1) and (num2>num3)):
    print("Greater number is:",num2)
else:
    print("Greater number is:",num3)

# 3. Match Catch
color = input("Enter a color: ")
match color:
    case "Green":
        print('You can go now.')
    case "Yellow":
        print("Please slow down.")
    case "Red":
        print("Stop please.")
    case _:
        print("Wrong Color!")

# Another Example
person_age = 18
if person_age<=13:
    print("It's a child.")
elif person_age > 13 and person_age < 18:
    print("It's a teenager.")
else:
    print("Adult hai saahab!")

# Another example of Nesting
username = input("Enter username: ")
password = input("Enter password: ")

if(username == "admin" and password == "123"):
    print("Successfull login.")
else:
    if(username != "admin"):
        print("Wrong username.")
    else:
        print("Wrong password.")

# Loops

#1. While loop
times = 1
while(times<=5):
    print("Jai Shree Ram",times)
    times+=1;

# while loop in reverse order
i = 5
while(i>=1):
    print(i)
    i-=1

# print multiplication table of any number n
number = int(input("Enter a number: "))
iteration = int(input("Enter iteration: "))
start = 1
while(start<=iteration):
    print(number,"X",start,"=",number*start)
    start+=1

# Break & Continue Keywords
t = 1
while (t <= 10):
    print(t)
    if t == 8:
        break
    t +=1

print("Continue Keyword")
q = 1
while(q <= 10):
    if q == 5:
        q += 1
        continue
    print(q)
    q += 1

# Print all the odd numbers from 1 to 10
s = 1
while(s<=10):
    if(s%2 != 0):
        print(s)
    else:
        s+=1
        continue
    s+=1

# 2. For loop
string = "hello"
for value in string:
    print(value)

# Count number of i in this word "Artificial Intelligence"
word = "Artificial Intelligence"
count = 0
for i in word:
    if (i=="i"):
        count +=1
print("Number of i:",count)

# Print Vowel count of a given string
text = input("Enter a text: ") 
text_vowel_count = 0
for i in text:
    if(i == "I" or i == "A" or i == "O" or i == "U" or i == "E"):
        text_vowel_count += 1
print("Total vowel count is:",text_vowel_count)


# In keyword 
data = 'hello'
if 'o' in data:
    print("It exists brother.")


# range function
for i in range(5):
    print(i)

for i in range(3,6):
    print(i)

for i in range(1,10,2):
    print(i)

# Print sum of first 'n' natural numbers
container = int(input("Enter a number: "))
sum_of = 0
for i in range(1,container+1):
    sum_of += i
print("Sum of first",container,"numbers is:",sum_of)


# Functions in python
def hello():
    print("Hello Brother")
hello()

# Functions with parameters
def user(name,age,course):
    print("Hello",name,"Your age is",age,"& You are pursuing",course)
user("Rohit",21,"BCA")

# Function to calculate avg of 3 numbers
def avg(a,b,c):
    result = (a+b+c) / 3
    #f stands for f-string / formatted string that lets you insert variables directly inside a string using {}.
    print(f"The sum of {a,b,c} is {result}") 
avg(10,20,30)

# Function with return statements
def sum(a,b):
    return a+b
print(f"Sum of a & b is: {sum(10,20)}.")

# Functions with default parameter values
def greet(name,course="BCA",college="GGSIPU"):
    print(f"Hello {name},You are pursuing {course} in {college}.")
greet("Rohit")
greet("Manya","BBA","Dr.Ambedkar university")

# Lambda Function
avg = lambda a,b,c: (a+b+c)/3
print(int(avg(10,20,30)))


# WAF to print factorial of 'n'.
def factorial(num,start):
    result = 1
    while(start <= num):
        result *= start
        start += 1  
    return result
        
number = int(input("Enter a number:"))
start = 1
data = factorial(number,start)
print(f"Factorial of {number} is {data}.")