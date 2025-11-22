# Strings
single_char = 'A'
word = "One Python"
print (len(single_char))
print (len(word))

# Concatenation
print(single_char + " " + word)

# Accessing Single characters using indexing values
print(word[0])

# Accessing using for loop
for char in word:
    print(char)

# Strings are immutable
word[0] = "M"
print(word) # Will threw error

# Slicing -> when we need a part from string
# string[start : stop-1 : step]
word = "Python"
print(word[0])
print(word[0:4])
print(word[0:4:2])
print(word[1::2])

# Negative indexing value start from -1
print(word[-6:-3])
print(word[-6:])
print(word[-6])
print(word[-1])
print(word[-6:-1])

# How to reverse a string in python
print(word[::-1])

# String Formatting or Dynamic String
# We can do it using 2 ways:
# 1. format() fn
name = "Rohit"
age = 21
# Normal formatting
text = "My name is {} and I am {} years old.".format(name,age)
print(text)
print("This is an example of: {}.".format("format () function"))

# index based formatting
print("The coordinate of this place is: {1},{0}".format("x","y"))

# value based formatting
print("Name:{n},Age:{a}".format(n="Namo",a=21))

# 2. f-string (python 3.6 +)
print(f"Hello my name is {name} and my age is {age}.")

# Lists -> Mutable Sequence of values
# Items in a list are ordered, changeable (mutable), can contain duplicates and Heterogeneous (can contain different data types) 
marks = [99,89,65,65,92,71, "abc", 100.88]
print(len(marks))
print(marks)
print(marks[0])

# Lists are mutable (Modify Elements)
marks[0]=100
print(marks)

# Slicing on lists
print(marks[1::2])
print(marks[0:4])

# Lists methods are basically functions but in python list and tuple
# are classes and classes functions are known as methods therefore we can say they are functions.
# BUt only usable with the lists
list1 = [1,2,3,4,5]

list1.append(6) #add one element at the end

list1.insert(1,"Rohit") #insert element at particular index with value

# list1.sort() #arranges in increasing or decreasing order but only one type of data must exist 
# since in list1 hetereogenous types of data exists it'll threw error
list2 = [10,9,8,7,6,5,14]
list2.sort() # be default increasing order
list2.sort(reverse=True) # in decreasing order
print(list2)

list3 = ['a','z','d']
list3.reverse() # reverses order
print(list3)

# Using loops with lists
list4 = ["Rohit","Umang","Namo","Rudraksh"]
for i in list4:
    print(i)


# Tuples -> immutable sequence of values
# Tuples are ordered (Items have a defined order and can be accessed by index), immutable, allows dupliates and heterogeneous.
# Since they are immutable they are faster as compare to Lists.

tuple1 = (1,2,3,4,5,"Rohit")
print(tuple1)
print(type(tuple1))
print(len(tuple1))

# Tuple are immutable
# tuple1[2]="Namo"
# print(tuple1)

# We can't create single value tuple 
tuple2 = (1)
tuple3 = ("Rohit")
print(type(tuple2))
print(type(tuple3))

# To create single value tuple
tuple4 = ("Rohit",)
print(type(tuple4))

# Slicing and indexing are same like in lists

# Loop on tuples
t5 = (1,2,3)
sum = 0
for i in t5:
    sum += i

print(sum)


# Tuple Methods
t6 = (1,6,3,4,5,6,7)
print(t6.index(6)) #returns 1st occurence index of given value
print(t6.count(6)) #counts total occruences of given value

# Dictionary -> Unordered, mutable collection of key value pairs where key are always unique.
dict = {
    "name":"Rohit",
    "sub":["Web Development","AI/ML","DSA"],
    "cgpa":9.0,
    967:"Center Code"
}
print(type(dict))
print(dict)

# Accessing Particular values
print(dict["name"])
print(dict[967])

# Modifying data
dict["cgpa"] = 9.6

print(dict)


# Dictionary Methods
print(dict.keys()) # returns all keys
print(list(dict.values())) # returns all values and we are additionally typecasting it to lists data types
print(dict.items()) #returns (key,val) pairs
dict.update(
    {
        "city":"Delhi"
    }
) #adds new item to dict
print(dict)

# Difference between them:
print(dict["sub"]) #returns value according to key but if key is incorrect it throws error
print(dict.get("sub")) #returns value according to key  but if key is incorrect it throws None


