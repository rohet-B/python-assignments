# Question (Product Store): Design and create an online store for products(name,price)
# Track total products being created
# Create a staic method to calculate discount on each product based on a % parameter.

class Products:
    tracking_products = 0

    def __init__(self,name,price):
        self.name = name
        self.price = price
        # We write Products.tracking_products += 1 inside the constructor (__init__) because the constructor is automatically executed every time a new product object is created. This makes it the correct place to update the total product count. A class method does not run automatically; it only runs when we explicitly call it, so using it for counting would require manual calls and could miss some creations. Therefore, the constructor handles the counting when products are created, while the class method is better used to access or display the class-level tracking data.
        Products.tracking_products += 1 #If we use self instead of Products, a separate instance attribute tracking_products will be created for each object, instead of updating the class-level counter.

    def get_info(self):
        print(f"Price of {self.name} is Rs.{self.price}")

    @classmethod
    def track_products(cls):
        print(f"Total Products in store = {cls.tracking_products}")
    
    @staticmethod
    def discount(amnt,disc_percent):
        return (amnt*(disc_percent/100))
        

p1 = Products("Phone",35_000)
p2 = Products("Laptop",55_000)
p1.get_info()
p2.get_info()
Products.track_products()
print(f"Discount price is: {Products.discount(100,10)}")


# Question: Create a BankAccount class with attributes account_number, owner_name, and balance. Add methods to deposit,
# withdraw and check balance. (Classes & Object)
class BankAccount:
    # balance = 0
    # Using balance = 0 inside the BankAccount class creates a class variable, which means the same balance value would be shared by all bank account objects. However, in a real bank system, each account must have its own separate balance. That is why balance should be an instance variable, created using self.balance inside the constructor. When we assign self.balance = balance in __init__, Python creates a unique balance for each account object.
    def __init__(self,account_number,owner_name,balance):
        self.account_number = account_number
        self.owner_name = owner_name
        self.balance = balance

    def deposit(self,amnt):
        self.balance += amnt
        print(f"Your available balance is {self.balance}")
    
    def withdraw(self,amnt):
        self.balance -= amnt
        print(f"Your available balance is {self.balance}")


    def check_balance(self):
        print(f"Your total balance is {self.balance}")
    

BA1 = BankAccount(1000,"Namo Narayan",11_000)
BA1.check_balance()
BA1.deposit(11_000)
BA1.withdraw(20_000)
BA1.check_balance()


# Question: Create a class Book with the followning attributes:
# title, author, list of reviews
# And add methods to : add a new review, count reviews, display all reviews (Class & Objects)
# Question: Create a class Book with the followning attributes:
# title, author, list of reviews
# And add methods to : add a new review, count reviews, display all reviews (Class & Objects)

class Book:
    # Because the book should start with no reviews, and reviews should be added using a method, not provided from outside.
    def __init__(self,title,author): 
        self.title = title
        self.author = author
        self.list_of_reviews=[]

    def review(self,review):
        self.list_of_reviews.append(review)

    def count_review(self):
        print(f"There are {len(self.list_of_reviews)} reviews for the book {self.title}.")

    def display_review(self):
        if(len(self.list_of_reviews) == 0):
            print(f"No review is done for book {self.title}")
        else:
            count = 1
            for r in self.list_of_reviews:
                print(f"{count}: {r}")
                count +=1

B1 = Book("Do Epic Shit","Ankur Warikoo")
B1.count_review()
B1.display_review()
B1.review("Helped me to developed reading habit.")
B1.review("Motivational Book")
B1.count_review()
B1.display_review()

B2 = Book("Meditations","Marcus Aurelius")
B2.count_review()
B2.display_review()
B2.review("Book that shows a new perspective.")
B2.review("This book helps me to learn from each person around you.")
B2.review("It may be complicated to understand but it's worth it.")
B2.count_review()
B2.display_review()


# Question: Create a class Student with private attributes: _name, _roll_no and _marks.
# Provide getter and setter methods with validation (e.g. marks cannot be negative, roll number has to be between 1 & 100
# & name cannot be empty) (Encapsulation)
class Student:
    def __init__(self,name,roll_no,marks):
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    def get_marks(self):
        return f"{self.__name}, your marks is {self.__marks}."

    def update_marks(self,marks):
        if marks < 0:
            print("Marks can't be negative.")
        else:
                self.__marks = marks 
                print("Marks updated.")

    def get_rollNum(self):
         return f"{self.__name}, your roll number is {self.__roll_no}."
    
    def update_rollNum(self,new_rollNum):
        if new_rollNum > 0 and new_rollNum <= 100:
            self.__roll_no = new_rollNum
        else:
            print("Roll number must be between 1 and 100.")

    def get_name(self):
        return f"Name is {self.__name}."
    
    def update_name(self,name):
        if len(name) == 0:
            print("Name can't be empty.")
        else:
            self.__name = name
              

S1= Student("Rohit",3,78)    
print(S1.get_name())
print(S1.get_marks())
print(S1.get_rollNum())

S1.update_name("Rohit Biswash")
print(S1.get_name())


# Question: Create a class Shape with a method area().
# Create sublcasses Circle, Rectangle and Triangle that override the area() method. (Function Overriding)
# Question: Create a class Shape with a method area().
# Create sublcasses Circle, Rectangle and Triangle that override the area() method.

class Shape():
    def area(self):
        pass

class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius

    def area(self):
        return 3.14 * self.radius * self.radius
    
class Rectangle(Shape):
    def __init__(self,length,breath):
        self.length = length
        self.breath = breath
    
    def area(self):
        return self.length*self.breath
    
class Triangle(Shape):
    def __init__(self,base,height):
        self.base = base
        self.height = height
    
    def area(self):
        return ((1/2)*self.base*self.height)


# Question: Create a base class Vehicle with attributes like brand and model.
# Create 2 sublclasses Car and Bike that add extra attributes -seats (in Car) & engine_cc(in bike). (Inheritance)
class Vehicle():
    def __init__(self,brand,model):
        self.brand = brand
        self.model = model

class Car(Vehicle):
    def __init__(self,brand,model,seats):
        super().__init__(brand,model)
        self.seats = seats

class Bike(Vehicle):
    def __init__(self,brand,model,engine_cc):
        Vehicle.__init__(self,brand,model)
        self.engine_cc = engine_cc

V1 = Vehicle("Producer","XYZ")
print(f"Vehicle {V1.brand} will produce {V1.model} model.")

C1 = Car("Maruti Suzuki","Alto A10",5)
print(f"The Brand is {C1.brand} and model is {C1.model} has {C1.seats} seats.")

B1 = Bike("Royal Enfield","Continental GT 650",349)
print(f"The Brand is {B1.brand} and model is {B1.model} has {B1.engine_cc}cc.")


# Question: Create an abstract class Employee with an abstract method calculate_salary()
# Create subclasses Intern, FullTimeEmployee and ContractEmployee that implement the method differently.(Abstraction)
from abc import ABC,abstractmethod

class Employee(ABC):
    @abstractmethod
    def calculate_salary(self):
        pass

class Intern(Employee):
    def __init__(self,salary,month):
        self.salary = salary
        self.month = month

    def calculate_salary(self):
        print (f"Your total salary for {self.month} months is {self.salary*self.month}.")
        
class FullTimeEmployee(Employee):
    def __init__(self,salary,extra_hours):
        self.salary = salary
        self.extra_hours = extra_hours

    def calculate_salary(self):
        if self.extra_hours > 0 and self.extra_hours <= 2:
            self.extra_hours = self.extra_hours * 3000
        elif self.extra_hours > 2 and self.extra_hours <= 4:
            self.extra_hours = self.extra_hours * 6000
        else:
            print("No extra hours working.")

        print (f"Your total salary for 12 months is {self.salary*12}, Additionally extra working hours income is {self.extra_hours}")

class ContractEmployee(Employee):
    def __init__(self,contract_Time):
        self.contract_Time = contract_Time
    
    def calculate_salary(self):
        if self.contract_Time <= 3:
            self.salary = 15_000
        elif self.contract_Time <=6:
            self.salary = 30_000
        else:
            print("Contract time must be between 3 to 6 months.")
        
        print(f"Your total salary for 12 months is {self.salary}.")

I1 = Intern(6_000,2)
I1.calculate_salary()

F1 = FullTimeEmployee(2000,3)
F1.calculate_salary()

C1 = ContractEmployee(4)
C1.calculate_salary()


# Question: Create a class Person that allows the constructor to work with:
# name only, name + age, name + age + address 
# As direct constructor overloading (multiple coonstructors) are not allowed but we have to 
# use default parameters to simulate constructor overlaoding. (Constructor Overloading (with Default Parameters))
class Person:
    def __init__(self,name,age=18,address="South Avenue, New Delhi"):
        self.name = name
        self.age = age
        self.address = address

    def get(self):
        print(f"Your name is {self.name} and your age is {self.age}, Your address is at {self.address}.")
    
P1 = Person("Rohit",21,"Narmada Apartments")
P1.get()


# Question: Create a class Player with:
# a class variable player_count + instance variables name and level
# Track how many players were created. (Instance & Class Attributes)

class Player:
    player_count = 0

    def __init__(self,name,level):
        self.name = name
        self.level = level
        Player.player_count += 1
    
    @classmethod
    def total_players(cls):
        print(f"Total players created {cls.player_count}.")

P1 = Player("Rohit","Level 1")
P2 = Player("Rohit","Level 2")
P1.total_players()


# Question: Create the following classes: Herbivore, Carnivore, Omnivore with some attributes and methods. Then create a class Bear that inherits from all 
# the above classes to showcase how multiple inheritance works. (Multiple Inheritance)

class Herbivore:
    food_type = "Plants"
    hunting_skill = False

    def eat_plants(self):
        print("Eats plants")

class Carnivore:
    food_type2 = "Meat"
    hunting_skill = True

    def eat_meat(self):
        print("Eats meat")

class Omnivore:
    food_type3 = "Plants and Meat"
    diet_type = "Mixed"

    def eat_both(self):
        print("Eats both plants and meat")

class Bear(Herbivore,Carnivore,Omnivore):
    def __init__(self,special):
        self.special = special

    def info(self):

        if self.special == True:
            print(f"This special bear eats {self.food_type} for 6 months and {self.food_type2} for next 6 months. In short it has {self.diet_type} diet type.")
        else:
            print("Information regarding Bears:")
        
            # Herbivore.eat_plants()
            # Carnivore.eat_meat()
            # Omnivore.eat_both()

            # Here you directly called methods from the parent classes using the class names, such as Herbivore.eat_plants(), which are instance methods and require an object (or self) to be called.
            # Therefore self is used
            self.eat_plants()
            self.eat_meat()
            self.eat_both()

        
B1 = Bear(False)
B1.info()


# Mini Project - OOP Chat System
# Create a Chat System using OOPs concepts. We have to create classes:
# User, Message and ChatRoom
# And we have to implement functions:
# sending messages, viewing chat history and user joining & leaving the chatroom. 

# To solve this problem suppose there is a Place where this things will work so first place is chatRoom where user and message will work.
# Now once 2 Classes are created and attributes are defined now create ChatRoom function of add_user and then join_chatroom function of User
# TO understand their workings, similarly for each operation make it one by one.

class ChatRoom:
    def __init__(self,name):
        self.name = name
        # A chatroom must contains it's active users and messages they share
        self.users = []
        self.messages = []
    
    def add_user(self,user):
        self.users.append(user)
        
    def remove_user(self,user):
        self.users.remove(user)

    def broadcast(self,sender,message):
        message = Message(sender,message) #Sending sender & message info to Message class
        self.messages.append(message)
        print(message)
    
    def show_chat_history(self):
        print(f"\nChat History of {self.name}:")
        for msg in self.messages:
            print(msg)
            print()

class User:
    def __init__(self,username):
        self.username = username
        self.chatroom = None # Is user is participated in any room or not -> At first not
    
    def join_chatroom(self,chatroom):
        if self.chatroom is not None:
            print(f"{self.username} is already in a chatroom.")
        else:
            self.chatroom = chatroom
            chatroom.add_user(self)
            # Next, when someone later writes code like room = ChatRoom("Python"), Python will create a real chatroom object using the ChatRoom blueprint. That object will have a name, an empty users list, and an empty messages list. Similarly, when someone writes u1 = User("Rohit"), Python will create a real user object with a username and chatroom = None, meaning the user is not in any room yet.
            # Now, when u1.join_chatroom(room) is called, Python enters the join_chatroom method. Inside this method, self refers to the user (u1), and chatroom refers to the chatroom object (room) that was passed in. Since the user is not already in any chatroom, the code sets self.chatroom = chatroom, meaning the user now remembers which chatroom they are in. Then chatroom.add_user(self) runs, which tells the chatroom to store this user inside its users list. At this point, the relationship is created from both sides: the user knows its chatroom, and the chatroom knows its user.    
            print(f"{self.username} joined {chatroom.name}")

    def leave_chatroom(self):
        if self.chatroom is None:
            print(f"{self.username} is not in any chatroom.")
        else:
            room_name = self.chatroom.name
            # chatroom.remove_user(self)
            # VS
            self.chatroom.remove_user(self)
            # In join_chatroom, the chatroom object is available as a parameter named chatroom, so we directly call chatroom.add_user(self) to tell that chatroom to add the current user. However, in leave_chatroom, there is no chatroom parameter, because the user is already inside a chatroom and that information is stored in self.chatroom. So to remove the user, we must first access the chatroom the user is currently in using self.chatroom, and then call its remove_user method.
            self.chatroom = None
            print(f"{self.username} left {room_name}")

    def send_message(self,message):
        if self.chatroom == None:
            print(f"{self.username} cannot send a message (not in a chatroom).")
        else:
            self.chatroom.broadcast(self, message)
            # In the line self.chatroom.broadcast(self, message), the first self is the sender. Inside the send_message method, self refers to the current User object (the person sending the message).


class Message():
    message_counter = 1

    def __init__(self,sender,message):
        self.sender = sender
        self.message = message
        self.messageId = Message.message_counter 
        Message.message_counter += 1 # when new object is created increase the value of message_counter

    # __str__() is used to decide how an object should describe itself in words when we try to display it. When we want to see an object, Python needs a readable form that humans can understand, not a technical or memory-based representation.
    def __str__(self):
        return f"({self.messageId}) {self.sender.username}: {self.message}"

room1 = ChatRoom("Python Code")

u1 = User("Rohit")
u2 = User("Namo")
u3 = User("Charlie")

u1.join_chatroom(room1)
u2.join_chatroom(room1)

u1.send_message("Hello Everyone")
u2.send_message("Hi brother")

room1.show_chat_history()

u1.leave_chatroom()
u2.leave_chatroom()