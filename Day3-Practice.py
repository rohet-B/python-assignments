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