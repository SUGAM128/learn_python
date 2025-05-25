file = open("read.txt", "r")
# print(file.readable())
for files in file.readlines():
    print(files)