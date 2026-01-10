# File I/O (Input/Output)
# It means reading data from files and writing data to files using python.

# File Operations:

# 1. Opening a file
# We use open() function
# file = open("file_name.format","mode")

# 2. Reading from a file
# We use read() function
# data = file.read()

# 3. Writing to a file
# We use write() function + whenever want to write in file we have to open it in any write modes
# file.write("data")

# 3. Closing a file
# WE do this explicitely to avoid any unexpected changes in the file.
# We use close() function
# file.close()


# Create sample.txt file and perform above operation
file = open("sample.txt","r") # returns file object
data = file.read()
print(type(data))
print(data)

file2 = open("sample.txt","w") # since w is only for writing we can't read the file for writing and reading we have to use "r+"
file2.write("Anything that is imagined \n can be programmed.")
file2.close()


# types of mode
# "r" (Read) -> Opens file for reading(default) + Error if file doesn't exist.
# "w" (Write) -> Creates new file + overwrites existing file (truncates file first)
# "x" (Create & Write) -> Creates new file & open for writing + if file exsists it doesn't truncate but threw an error
# "a" (Append) -> Adds content at the end of the file + Creates new file if not exists
# "b" (BInary mode) -> For images, videos etc.

# in this modes pointer's place important role
# "r+" (Write & Read) -> File must exist + Since pointer starts at the beginning of file, new content are added at first + OVerwrites existing content for the numbers of chracters written, not the whole file 
file3 = open("sample.txt","r+")
file3.write("Hello ") # Writing to a file moves the file pointer forward, and further operations start from that position. 
print(file3.read())
file3.close()

# "w+" (Write & Read) -> OVerwrites existing file + Creates new file if not exists
file4 = open("sample.txt","w+")
file4.write("Mother's Son") # Since, it overwrites the entire file the pointer moves forward and reading operations then start from that poistion and prints nothing
print(file4.read())

# "a+" (Append + Read) -> adds to end of file + if file not exists creates a new one
file5 = open("sample.txt","a+")
file5.write(" Then we get mother's love.") #here also pointer appends at end of file and moves ahead then for reading pointer starts from that poistion where it stopped.
print(file5.read())

# Now what mode when to use a graph was provided in fundamentals pdf refer to it.

# WE have more functions to read and write in a file.
# For Read operation:
# 2. readline() -> Reads one line at a time + readline() keeps the newline character (\n) at the end of the line it reads from a file and that extra newline causes a gap when the values are printed.
f1 = open("sample.txt","r")
line1 = f1.readline()
line2 = f1.readline()
f1.close()
# print(f"Line 1: {line1}Line 2: {line2}")
print(line1)
print(line2) #Here a space or gap will occur after line1 

# 3. readlines(): Reads all lines into a list.
f = open("sample2.txt","r")
lines = f.readlines()
print(lines)
f.close()

# For write operation:
# 2. writelines(): Writes multiple lines at once.
f = open("sample.txt","w")
lines = f.writelines(["Line 1 \n","Line 2 \n"])
print(lines)
f.close()

# With keyword
# with automatically takes care of opening and closing a resource + You don’t need to manually close the file.
with open("sample.txt","r") as f:
    content = f.read()
    print(content)

# Deleting a file
# To delete a file we use the remove function
# Since file deletion is handled by the operating system, we need to import the os module.
import os
os.remove("sample2.txt")


# Exception Handling
# Allows you to manage errors (exception) that occurs while a program is running so that program continues to run without any program crashes.
# Specific Errors / Exception examples:
# 1. Dividing by zero - ZeroDivsionError
# 2. Using an undefined variable - NameError
# 3. Opening a missing file - FileNotFoundError
# 4. Wrong data type - TypeError
# 5. Incorrect input value - ValueError
# There are many exceptions that we can read in w3schools.

# Syntax
try:
    pass
    # program that can cause problem
except:
    # Note: Multiple except block can be created.
    pass 
    #code that runs if error occurs

# Ex 1
try:
    print(10/0)
except: # Run when any error occurs
    print("You can't divide by zero.")

# Ex 2
try:
    pass
    # print(10/a)
except ZeroDivisionError: # When specific exception is written then this will run only when the mentioned exception occurs.
    print("You can't divide by zero.")


# "else" executes only if no exception happens
try:
    x = int(input("Enter a number: "))
except ValueError:
    print("Invalid input")
else:
    print("You entered:",x)


# "finally" always executes whether an exception occurs or not + mainly used for closing files & releasing resources.
try:
    f = open("data.txt")
    print(f.red())
except FileNotFoundError:
    print("File not found")
else:
    print("Executed completely")
finally:
    print("Code executed...")


# "raise": is used to manually trigger an exception
salary = int(input("Enter salary amount: "))
if salary>1_00_000:
    raise ValueError("Not a valid salary.")


# Custom Error (Not done by apna college as mam said she will teach it later when it is required.)
# In python we can define custom exceptions by creating a new class that is derived from Exception class.

class AgeError(Exception):
    pass

try:
    age = int(input("Enter age: "))
    if(age<18):
        raise AgeError("You are minor.")
        
except AgeError as e:
    print(e)
    
else:
    print("You are eligible to vote.")


# List Comprehensions
# It is a short and elegant way to create a lists in python.
# It replaces long "for" loops with one-line expressions.
# Syntax:
# [expression/output_we_want for item in iterable if condition (optional)]

# Without list comprehensions
squares = []
for i in range(6):
    squares.append(i*i)
print(squares)

# with list comprehensions
squares = [num*num for num in range(6)]
print(squares)

# Ex1: Create a list of numbers 1 to 5
nums = [x for x in range(1,6)]
print(nums)

# Ex2: Even numbers from 1 to 10
nums = [x for x in range(1,11) if x%2 == 0]
print(nums)

# List comprehension with if-else
# [Output/expression_if_true if condition else expresssion_if_false for item in iterable]
# Ex3: Label numbers as "Even" or "Odd" from 1 to 5
labels = ["Even" if x%2==0 else "Odd" for x in range(1,6)]
print(labels)

# Ex4: Write a list of strings in uppercase using list comprehension.
word = ["hello","python","apnaCollege"]
words = [element.upper() for element in word]
print(words)


# JSON (JavaScript object Notation) Module 
# Lightweight data format used to exchange data between programs, APIs, websites etc. JSON format is very similar to python dictionaries.
# Python's "json" module allows you to read, write, encode & decode JSON Data.
# JSON uses key value pairs.
# In Python, we call ["data1","data2"] it a list, but in JSON, it is called an array.
# In python, we call {"key":"Value"} it a dictionary, but in JSON, it is called an object.

import json
# Converting Python to JSON
# we use "dumps()" to convert python dictionary or object into JSON String.

data = {
    "name":"Namo",
    "age":21,
    "dob":"7-1-2005",
    "marks":[85,90,95]
}
json_string = json.dumps(data)
print(type(json_string))
print(json_string)

# Converting JSON to python
# we use "loads()" to convert JSON string into python dictionary or object.
json_data = '{"name": "Namo", "age": 21, "dob": "7-1-2005", "marks": [85, 90, 95]}'
python_obj = json.loads(json_data)
print(python_obj["name"])
print(type(python_obj))


# Reading JSON from a file (json.load())
# jsonfile.txt contains this:
# {
#   "name": "Rohit",
#   "age": 21,
#   "skills": ["Python", "JavaScript"]
# }

with open("filename.txt","r") as f:
    data = json.load(f)
print(data["name"])

# Writing JSON to a file (json.dump())
data = {"name":"Namo","area":"shadipur"}
with open("data.json","w") as f:
    json.dump(data,f,indent=4,sort_keys=True)
    # indent=4 makes the JSON looks neat and readable.
    # sort_keys=True will sort the keys in ascending order A -> Z + It does not support descending order.