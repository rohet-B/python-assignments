# Create a sample file with content:
# This is a demo file
# to store some words
# for the Python activity
# that is to be solved by us.

# Question: Search word python word and at which line it exists in this above content:
data = True
count = 0
with open("sample.txt","r") as f:

    # To access each line we have to read again and again 
    # data = f.readline()
    # print(data)

    # data = f.readline()
    # print(data)

    # Using loop to access each line: 
    while data:
        data = f.readline()
        count += 1
        # print(data)
        if("Python" in data):
            print(f"Word found in line {count}.")
            break

        # when the file has no more lines left to read data becomes an empty string (data == "")
        # In python empty string means false:
        # print(bool(""))
        # print(bool("Hello"))

# Question: create a program that:
# 1. Opens a file "names.txt" in write mode
# 2. Writes 5 names (one per line) entered by the user
# 3. Then open the same file in read mode and prints all names
with open("names.txt","w") as f:
    content = f.writelines(["Namo\n","Rohit\n","Manjari\n","Atul Sir\n","Hitesh Sir"])

with open("names.txt","r") as f:
    data = f.read()
    print(data)

# Question: Create a program that:
# 1. opens a file "log.txt" in append mode
# 2. adds a new log entry (like "Program run successfully")
# 3. opens the file in read mode and prints all logs
with open("log.txt","a") as f:
    f.write("Program run successfully")

with open("log.txt","r") as f:
    print(f.read())


# Question: Create a program that:
# 1. Has a list of numbers: [5,10,15,20,25]
# 2. uses a list comprehension to create a new list with only numbers greater than 15
# 3. prints the new list
l1 = [num*5 for num in range(1,6)]
l2 = [num for num in l1 if num>15]
print(l2)


# Question: Create a python dictionary of 3 cities and their populations.
# 1. save it to "cities.json".
# 2. Then load the JSON and print each city and its population.
# 3. Asks the user for a new city & its population - update this info in the json file.
import json
d1 = {
    "New Delhi":1_00_000,
    "East Delhi":50_000,
    "West Delhi":50_000
}

with open("cities.json","w") as f:
    json.dump(d1,f,indent=4)

with open("cities.json","r") as f:
    data = json.load(f)
    print(data)


new_city = input("Enter a new city: ")
new_population = int(input("Enter the population of new city: "))

with open("cities.json","r") as f:
    data = json.load(f)
    # print(data)
    data.update(
        {
            new_city:new_population
        }
    )


with open("cities.json","w") as f:
    json.dump(data,f,indent=4)


with open("cities.json","r") as f:
    data = json.load(f)
    print(data)


# Question: Write a program that tries to open "data.txt" in read mode. If the file does not exist, catch the exception and print "File Not Found!".
try:
    with open("data.txt","r") as f:
        print(f.read())
except:
    print("File not found!")
else:
    print("File found successfully.")