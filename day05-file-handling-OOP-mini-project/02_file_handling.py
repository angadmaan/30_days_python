# To Read from a file 
 
f = open("file.txt")

data = f.read() 
print(data)
f.close()

# To Write to a file

st = "Hey man, howdy!"

f = open("write.txt", "w")

f.write(st)

f.close()


# Modes for opening file

# 1. r - open for reading 
# 2. w - open for writing
# 3. a - open for appending
# 4. + - open for updating
# 5. rb - open for read in binary mode
# 6. rt - open for read in text mode

# To append in a file

st = "Hey man, howdy!"

f = open("write.txt", "a")

f.write(st)

f.close()

# # readline function

f = open("file.txt", "r")

line1 = f.readline()
print(line1)

line2 = f.readline()
print(line2)

line3 = f.readline()
print(line3)

f.close()

# readline with while loop 

f = open("file.txt", "r")

line = f.readline()

while line != "":
    print(line)
    line = f.readline()

f.close()


