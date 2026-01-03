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


# Attributes in OOP
# They are variabls that belong to a class or an object.
# Types of Attributes:
# 1. Class Attributes -> Belong to the class, shared by all objects + defined outside any method in the class
class Student2:
    college = "ABC COLLEGE" #class attribute

stu1 = Student2()
print(stu1.college)
print(Student2.college) # Class Attribute can also be accessed with class name.

# 2. Instance Attributes -> Belong to individual object + defined inside the __init__ method using self + Each object gets its own copy + Has high priority than class attribute
class Student3():
    gpa = 5.0 #Class Attribute
    def __init__(self,name,gpa): #instance attributes
        self.name = name
        self.gpa = gpa
stu1 = Student3("Namo",8.8)
stu2 = Student3("Rohit",8.7)
print(stu1.name,stu1.gpa) # since instance attribute has high priority, it's value will print
print(stu2.name,stu2.gpa)


# Different Methods in OOP
# 1. Instance Methods -> Take self as first argument + can access both instance attributes and class attributes
class Dish:
    belong = "India"
    def __init__(self,name,type):
        self.name = name
        self.type = type
    
    def info(self): #instance method
        return f"Name: {self.name}, type: {self.type} and it's belong to {self.belong}."
food1 = Dish("Rajma Chawal","Veg")
# You can call an instance method
# 1. using object:
print(food1.info()) # When you write food1.info() python auto internally does Dish.info(food1)
# 2. Using Class name but you must pass the object explicitly
print(Dish.info(food1))

# 2. Class Methods -> Use @classmethod decorator + Take cls (class) as first parameter + can access class attributes only + used to work with class-level data
class Car:
    company = "Toyota"

    @classmethod
    def change_company(cls,name):
        cls.company = name

# You can call a Class method
# 1. using object:
c1 = Car()
c1.change_company("Audi")
print(c1.company)

# 2. Using Class Name:
Car.change_company("BMW")
print(Car.company) # BMW

# 3. Static Methods -> use @staticmethod decorator + Do not take self or cls as parameter + Behave like normal functions but belong to the class for logical grouping
class Math:
    @staticmethod
    def add(a,b):
        return a+b
# You can call a Staic method
# 1. using class name:
print(Math.add(10,20))
# Call static methods with the class name (best practice), though objects can also call them.
m = Math()
print(m.add(250,250))