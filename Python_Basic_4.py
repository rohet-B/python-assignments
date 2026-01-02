# Object Oriented Programming 
# 1. Using classes to make objects making programs modular, reusable and easier to maintain 
# 2. Attributes/Properties are variables & Methods are functions defined inside a class.
# 3. A student can have many variables (Full name, Address, DOB, Attendance, Marks etc) now declaring them again again for each
# individual student would take much time therefore we create  a class that contains this we just give information to create a single student object.

# Creating a class
class Student:
    subject = "Full Stack Development" #Default value for subject property

# Creating objects
stu1 = Student()
print(stu1)
print(stu1.subject) #Using dot operator to access student's information

# CONSTRUCTOR:
# Constructor is a special method also known as __init__() method
# Constructor used to initialize newly created objects with initial values.
# Whenever we create an object of a class, python automatically calls the __init__() method single time.

class Pen:
    def __init__(self,name):
        # Self is a parameter that stores current instance of the class or It Refers to current object of the class
        # Self is compulsory to write
        print("Constructor Was called ...")
        self.name = name

    # Every instance method must have self    
    def writing(self):

        print("Writing hard.")
        # OR
        # return "Writing"

pen1 = Pen("Uniball")
print(pen1.name)
pen2 = Pen("Flair")
print(pen2.name)

# Instance method calling
pen2.writing()
# OR
# print(pen2.writing())


# Types of Constructor
# 1. Default Constructor - Constructor with no parameters except self.
# 2. Parameterized Constructor - Takes Parameters to initialize values uniquely for each object.

# Python doesn’t support constructor overloading directly (like Java/C++) i.e. having multiple constructors in the same class. 
# However if written 2 constructors then whichever is written last will execute.
# The arguments used to create an object must match the parameters of the last constructor, otherwise an error occurs.