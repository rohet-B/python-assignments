# File I/O (Input/Output)
# It means reading data from files and writing data to files using python.

# File Operations:

# 1. Opening a file
# We use open() function
# file = open("file_name.format","mode")

# 2. Reading from a file
# We use read() function
# data = file.read()

# 3. Writing to a file
# We use write() function + whenever want to write in file we have to open it in any write modes
# file.write("data")

# 3. Closing a file
# WE do this explicitely to avoid any unexpected changes in the file.
# We use close() function
# file.close()


# Create sample.txt file and perform above operation
file = open("sample.txt","r") # returns file object
data = file.read()
print(type(data))
print(data)

file2 = open("sample.txt","w") # since w is only for writing we can't read the file for writing and reading we have to use "r+"
file2.write("Anything that is imagined \n can be programmed.")
file2.close()


# WE have more functions to read and write in a file.
# For Read operation:
# 2. readline() -> Reads one line at a time + readline() keeps the newline character (\n) at the end of the line it reads from a file and that extra newline causes a gap when the values are printed.
f1 = open("sample.txt","r")
line1 = f1.readline()
line2 = f1.readline()
f1.close()
# print(f"Line 1: {line1}Line 2: {line2}")
print(line1)
print(line2) #Here a space or gap will occur after line1 


# types of mode
# "r" (Read) -> Opens file for reading(default) + Error if file doesn't exist.
# "w" (Write) -> Creates new file or overwrites existing file
# "a" (Append) -> Adds content at the end of the file
# "r+" (Read & Write) -> File must exist
# "w+" (Write & Read) -> OVerwrites existing file.
# "a+" (Append + Read) -> Reads + adds to end of file.
# "b" (BInary mode) -> For images, videos etc.
