# Create a sample file with content:
# This is a demo file
# to store some words
# for the Python activity
# that is to be solved by us.

# Question: Search word python word and at which line it exists in this above content:
data = True
count = 0
with open("sample.txt","r") as f:

    # To access each line we have to read again and again 
    # data = f.readline()
    # print(data)

    # data = f.readline()
    # print(data)

    # Using loop to access each line: 
    while data:
        data = f.readline()
        count += 1
        # print(data)
        if("Python" in data):
            print(f"Word found in line {count}.")
            break

        # when the file has no more lines left to read data becomes an empty string (data == "")
        # In python empty string means false:
        # print(bool(""))
        # print(bool("Hello"))