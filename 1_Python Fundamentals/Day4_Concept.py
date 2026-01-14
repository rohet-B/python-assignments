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
# 1. Class Attributes or Variable -> Belong to the class, shared by all objects + defined outside any method in the class
class Student2:
    college = "ABC COLLEGE" #class attribute

stu1 = Student2()
print(stu1.college)
print(Student2.college) # Class Attribute can also be accessed with class name.

# 2. Instance Attributes or Variable -> Belong to individual object + defined inside the __init__ method using self + Each object gets its own copy + Has high priority than class attribute
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


# OOP Pillars
# 1. Encapsulation -> Bundling of data (variables) and methods (functions) into a single unit (class) + also Controlling access to that data (variable) for Data Hiding
# To implement encapsulation, we use access modifiers. Python has 3 access levels:
# a. Public Members Or Public Attribute  -> Accessible everywhere (inside class & outside class), written like normal variables
class Smartphone:
    def __init__(self,name):
        self.name = name # public variable
sp1=Smartphone("REDMI NOTE 14 PRO + 5G")
print(sp1.name)

# b. Protected  Members Or Protected Attribute -> Indicated by a single underscore _ + Still accessible from outside (not truly protected) + Python does not truly enforce protection this is only a naming convention, not a strict access rule
# + They are meant for internal use within the class and it's subclass + However, Python follows idea of  "we are all responsible users" so we should not access it outside.
class BankAccount:
    def __init__(self,name,balance):
        self.name = name #Public Variable
        self._balance = balance #Protected Variable
acc1 = BankAccount("Rohit",100_000)
print(acc1.name)
print(acc1._balance) # Still accessible but not suggested to do

# c. Private Attribute -> Indicated by a double underscore __ + Python does name mangling: the variable name becomes _ClassName__variable
# + Can't accessed directly from outside + But Still accessible by using name mangling
class BankAccount:
    def __init__(self,name,balance):
        self.name = name #Public Variable
        self.__balance = balance #Pvt Variable
acc2 = BankAccount("Namo",100_000)
# print(acc2.__balance) #Directly not accessible the balance
print(acc2._BankAccount__balance) # Accessible through name mangling, Since python follows the idea of "we are all responsible users" it is suggessted not to access the pvt variables outside using name mangling

# Getters & Setters
# Since, python suggested not to use name mangling for accessing pvt variables, we can use getter to read data and setters to update data.
class BankAccount:
    def __init__(self,name,balance):
        self.name = name 
        self.__balance = balance 
    def get_salary(self):
        return (f"Total balance is {self.__balance}") # note: getter should use return rather than print
    def set_salary(self,new_balance):
        self.__balance = new_balance
        
acc2 = BankAccount("Namo",100_000)
print(acc2.get_salary())
acc2.set_salary(999)
print(acc2.get_salary())


# 2. Inheritance enables code reuse, clean & maintainable design, polymorphism
class Employee:
    start_time = "9AM"
    end_time = "5PM"

class Teacher(Employee):
    def __init__(self,subject):
        self.subject = subject
    
t1 = Teacher("Data Science")
print(f"{t1.subject} starts at {t1.start_time} and ends at {t1.end_time}.")

# Types of Inheritance
# 1. Single Inheritance
class Parent1:
    def display(self):
        print("Parent Class")
class Child1(Parent1):
    pass
    # In Python, pass means “do nothing”. It is used when a statement is required syntactically, but you don’t want to write any code yet.
c1 = Child1()
c1.display()

# 2. Multilevel inheritance -> A child inherits from a parent, and another class inherits from the child. 
class Employee:
    start_time = "9AM"
    end_time = "5PM"

class AdminStaff(Employee):
    def __init__(self,role):
        self.role = role

class Accountant(AdminStaff):
    def __init__(self,salary,role):
        super().__init__(role)
        # super() keyword is used to call parent class's method from child class.
        # Super() Auto knows the current obj + python passes self implicitly
        self.salary = salary
acc1 = Accountant(50_000,"CA")
print(acc1.salary,acc1.role,acc1.start_time,acc1.end_time)

# 3. Multiple Inheritance -> A child inherits from more than one parent class.
# MRO (Method Resolution Order) is the order in which Python searches classes when looking for a method or attribute, especially in multiple inheritance. 
# It determines which parent class’s method gets called first. In your example, TA inherits from Teacher and Student, and the MRO of TA is [TA, Teacher, Student, object]. 
# When super().__init__(salary) is called, Python automatically follows the MRO and executes Teacher.__init__ to set the salary. Since Student is further down the MRO, we call Student.__init__(self, gpa) directly and pass self explicitly to set the GPA. 
# Finally, self.name = name sets the attribute unique to TA. This ensures that all parent constructors are properly executed, giving the TA object all three attributes: name, salary, and gpa.

class Teacher:
    def __init__(self,salary):
        self.salary = salary

class Student:
    def __init__(self,gpa):
        self.gpa = gpa

class TA(Teacher,Student):
    def __init__(self,salary,gpa,name):
        super().__init__(salary) 
        Student.__init__(self,gpa) #Here, you are calling the method directly using the class name + Python does NOT know which object you mean + So you must pass self explicitly
        self.name = name
ta = TA(50_000,7.5,"Namo")
print(ta.name,ta.salary,ta.gpa)


# 3. Abstraction -> Hiding Internal Details & showing only essential features + Abstraction is implemented with abstract classes & Methods
# Abstract Classes:
# Can't be instantiated or Can't used to create objects + can contain normal & abstract methods + usually acts as a blueprint for child classes
# + abstract classes are part of abc module + abc module helps us to create abstract classes

# Abstract Methods:
# Methods declared inside abstract classes but not implemented (Children override this abstract methods)

from abc import ABC,abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass

class Lion(Animal):
    def make_sound(self):
        print("Roar")
        
class Cow(Animal):
    def make_sound(self):
        print("MOO")
        
l1 = Lion()
c1 = Cow()

l1.make_sound()
c1.make_sound()


# 4. Polymorphism
# Ability of a single function or method & operator to behave differently.
# Idea is that: Same method name works differently for different objects + Same Operator behvaes differently depending on operand types
# So it enables operator Overloading and Function (Method) Overriding.
# In python 4 types of polymorphism exisits:  

# 1. Operator Overloading: Same ‘+’ operator being used for 2 different operations
print(10+12)
print("Rohit "+"Biswash")

# 2. Function Overriding:
# When child class provides its own version of a method that already exists in parent class + It's a Runtime Polymorphism (which method to call based on the object is created and used during runtime)
# + When overriding a method or function, the method name and parameter structure should be consistent.
class Animal:
    def sound(self):
        print("Some Generic Sound will be made")
class Dog (Animal):
    def sound(self):
        print("Bark")

A1 = Animal()
A1.sound()

D1 = Dog()
D1.sound()

# 3. Duck Typing 
# Works on the idea: "If it looks like a duck and quacks like a duck, it must be a duck."
# Here different classes can have the same method name, and Python focuses on behavior rather than the object’s type (whether an animal, robot, human etc)
class Dog:
    def speak(self):
        print("Bark")
class Cat:
    def speak(self):
        print("Meow")
class Robot:
    def speak(self):
        print("Beep Boop")

def make_it_speak(entity):
    entity.speak()

d = Dog()
c = Cat()
r = Robot()

for e in [r,c,d]:
    make_it_speak(e)


# 4. Function Polymorphism: Same function works with different types of arguments.
print(len("Python"))
print(len([1, 2, 3]))