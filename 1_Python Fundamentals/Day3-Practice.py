# Ques: Suppose we have a list = [1,2,3,4,10,8] we want to find out index of a list item.
list = [1,2,3,4,10,8]
num = 10
idx = 0
# Linear Searching
for items in list:
    if(items == num):
        print(f"The number {num} exists at index {idx}.")
        break
    idx += 1

# Ques Given a list of tuples with info(name,subject):
    # list all unique course
    # list students enrolled in BCA
    # Create Dictionary (student,set of courses)
info = [
    ("Rohit","BCA"),
    ("Namo","BCA"),
    ("Umang","BCOM"),
    ("Manya","BBA"),
    ("Chirag","BBA"),
    ("Piyush","Math"),
    ("Shivam","Hindi"),
    ("Manjeet","BCA"),
    ("Rohit","Artificial Intelligence"),
    ("Rohit","Full Stack Developer"),
    ("Rohit","Tutoring"),
    ("Rohit","Guitar Playing")
]

all_sub = set()
stu_info = {}

for i in info:
    all_sub.add(i[1])

# All Unique Course are:
print(all_sub)

# Students in BCA
for name,course in info:
    if(course == "BCA"):
        print(name,course)
    
# Create Dictionary (student, set of course)

# Algorithm 1 
# 1. Getting Unique Students
unique_stu = set()
for name in info:
    unique_stu.add(name[0])
# print(unique_stu)

# 2.Creating dictionary with empty list for each students
unique_stu_info = {}
for name in unique_stu:
    unique_stu_info[name] = [] # creates dictionary keys with empty list[]

for each_stu in unique_stu_info:
    for subjects in info:
        if each_stu == subjects[0]:
            unique_stu_info[each_stu].append(subjects[1])
    
# print (f"See Here:\n{unique_stu_info}")

# OR 

# Algorithm 2
# if name not exist in dictionary then add it with an empty set and then add the correspondance subject of name in the empty set
# else if key already exists then only add the subject in the set
dict = {}
for name,course in info:
    if(dict.get(name) == None):
        dict.update({name:set()})
        dict[name].add(course)
    else:
        dict[name].add(course)
        
print (f"See Here:\n{dict}")


# Question: Ask the user for a string and check whether it is palindrome or not
str = input("Enter a string to check whether it's palindrome or not: ")
if (str == str[::-1]):
    print("Yes, it's a palindrome.")
else:
    print("No, it's not.")

# Question: Given a list of integers comput the average of all numbers in the list.
data1 = [1,2,3,4,5]
avg = 0
for i in data1:
    avg += i
avg = avg / len(data1)
print(avg)


# Question: Input 2 lists of integers from user. Merge them into one list and sort the result
list1 = []
list2 = []

print("Enter 5 elements you want to add in list 1: ")
for i in range(5):  
    data = int(input())
    list1.append(data)

print("Enter 5 elements you want to add in list 2: ")
for i in range(5):  
    data = int(input())
    list2.append(data)


result = list1 + list2 
# print(result)
# OR

list1 += list2
# print(list1)

# OR

# The extend() function is used to add all elements of one list to another list.
# list1.extend(list2) # adding elements of list2 to the end of list1
# print(list1)

# Question: Given a tuple of integers, create
# A tuple of all even numbers and a tuple of all odd numbers
t1 = (1,2,3,4,5,6,7,8)
even = []
odd = []
for i in t1:
    if(i % 2 == 0):
        even.append(i)
    else:
        odd.append(i)
print(tuple(even))
print(tuple(odd))


# Question: Create a dictionary where keys = student names and values = makrs
# Write a menu based program where user presses a key (A - ADD Student,B - Update Marks,C - Search for a student,D - Display all students) 
# according to the operation they want to perform on dictionary.

stu_dict = {
    "Rohit":99
}
while (1):
    print("Please select an option: ")
    print("Press A to add a student")
    print("Press B to update marks")
    print("Press C to search for a student")
    print("Press D to display all students and marks")
    option = input("")
    data = stu_dict.keys()

    if(option == "A"):
        name = input("Enter the student name: ")
        if name in stu_dict:
            print("Student already exists")
            name = input("Enter the student name again: ")
            
        marks = input("Enter the student marks: ")
        stu_dict.update(
            {
                name:marks
            }
        )
    elif (option == "B"):
        update_stu = input("Enter the name of student whose marks you want to update: ")
        update_marks = int(input("Enter the new marks"))
        if update_stu in stu_dict:
            stu_dict.update({
                    update_stu:update_marks
                })
    elif (option == "C"):
        search_stu = input("Enter a student name you want to search: ")
        if search_stu in stu_dict:  
            print(f"Student name is {search_stu} and marks {stu_dict.get(search_stu)}")
        else:
            print("Student doesn't exists.")
    else:
        print(list(stu_dict.items()))


# Question: Given a list of words:
# words = ["apple","banana","kiwi","cherry","mango"]
# Create a dictionary that maps each word to its length
# {"apple":5, "banana":6, "kiwi":4, ...}
words = ["apple","banana","kiwi","cherry","mango"]
empty_dict = {}
data = empty_dict.keys()

for fruit in words:
    if fruit not in data:
        empty_dict.update(
            {
                fruit:len(fruit)
            }
        )
print(empty_dict)

# Question: Write a program that takes a string from the user and prints the number of spaces in string.
string = input("Enter a string to find out spaces: ")
num = 0
for space in string:
    if(space == " "):
        num += 1
print(f"Number of spaces in the string are: {num}")

# Question: Write a program to Check if two lists have no elements in common.
list1 = [1, 2, 3]
list2 = [4, 5, 6, 7]

# isdisjoing() -> returns True if sets have no common elements

# if set(list1).isdisjoint(set(list2)):
#     print("Both list has no common elements")
# else:
#     print("Lists have common elements")

# OR

no_common = True

for i in list1:
    if i in list2:   # check if i exists in list2
        no_common = False
        break
    
if no_common:
    print("No common elements")
else:
    print("Lists have common elements")

# Question: Given a list,print all elements that appear more than once in the list use sets
my_list = [1,2,3,4,5,11,11,1,4,100]

seen = set()
duplicate = set()

for item in my_list:
    if item not in seen:
        seen.add(item)
    else:
        duplicate.add(item)

print("Duplicate elements are: ",duplicate)

# Question: Ask the user for a string and print 
# All unique characters
# The count of unique characters

user = input("Enter a string: ")

unique = []
duplicate = []

for char in user:
    if char not in unique:
        if char == " ":
            continue
        unique.append(char)
    else:
        duplicate.append(char)

print(f"All unique Characters: {unique} and the count of unique characters is {len(unique)}")

# OR

# .replace(" ", "") → removes all spaces
unique_char = set(user.replace(" ","")) #old_character, new_character
print("All unique characters:", unique_char)
print("Count of unique characters:", len(unique_char))