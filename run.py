# Sets -> An unordered collection of unique elements.
# Since unordered collections we can't do indexing or slicing
# Sets are mutable -> add or remove elements
# Set elements must be immutable, so only immutable data types—such as strings, numbers, and tuples—can be stored in a set.

set1 = {1,2,3,2,4,5,2}
print(set1) #Only One copy of duplicate values will be stored in sets
print(type(set1))
print(len(set1))

# Adding new values
set1.add(100)
print(set1)

# Creating empty sets
# empty_set = {} #creates empty dictionary
empty_set = set() #creates empty set
print(type(empty_set))

# Set Methods
set2 = {1,2,3,4,5,6}
set2.add(10) #adds a value
print(set2)
set2.remove(2) #removes a value
print(set2)
set2.pop() #removes a random value from a set
print(set2)
set2.clear() # empty all the set elements
print(set2)

# Union & intersection
# Union -> collection of all unique values in both sets
# Intersection -> collection of all common values in both sets
A = {1,2,3,4,5}
B = {3,4,5,8,9,10}
print(A.union(B)) #{1,2,3,4,5,8,9,10}
print(A.intersection(B)) #{3,4,5}