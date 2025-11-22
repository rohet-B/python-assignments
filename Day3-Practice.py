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