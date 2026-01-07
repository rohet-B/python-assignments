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