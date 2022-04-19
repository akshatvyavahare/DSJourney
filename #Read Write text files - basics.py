# Read text files

# there are 2 ways we can do it

# Method 1
x = r"C:\Users\aksha\Desktop\TextDocument.txt"        # here we have assigned the variable X to the file path - please replace the file path with yours

file = open(x, "r")                                   # we specify the open file function and read the file

print(file.read())

file.close()

# Method 2

with open(x, "r") as file:

      print(file.read())

# the out put of # 1 and # 2 will be the same

# Write text files

with open(x, "w") as file:                            # here the "r" is replaced with a "w", which means we are indicating in the code to write and not just read the file

      file.write("Hey this is the new sentence added to the file using Python. \n")             # this will replace all the content in the txt file 
      file.write("Hey this is the new sentence added to the file using Python. 2\n")
      file.write("Hey this is the new sentence added to the file using Python. 3\n")

with open(x, "r") as file:

      print(file.read())                              # the out put is the 3 statements mentioned above

# Append text files

with open(x, "a") as file:                            # here the "w" is replaced with a "a", which means we are indicating in the code to append and not just read the file

      file.write("Line 2. \n")                        # this will add all the content in the txt file and not replace as it did in the earlier part where we used the write function
      file.write("Line 3. 2\n")
      file.write("These lines were added to the file using the append function. 3\n")

with open(x, "r") as file:

      print(file.read())                              # the out put is the 3 statements mentioned above