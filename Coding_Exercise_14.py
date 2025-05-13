file = open("test.txt")
# print(file.readline())

line = file.readline()
count = 1
while line != "":
    # print(line)
    line = file.readline()
    count = count + 1

print("Total number of lines:", count)
