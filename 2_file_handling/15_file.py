#1:
file1 = open('15_my_file.txt', 'r')
#open('Directory', 'mode')
#mode: r - read, w - write, a - append, r+ - read and write

#read() => to read whole file
reading_file = file1.read()
print(reading_file)

#read(7) => to read specific letters
# print(file1.read(7))

#readline() => to read specific line
# print(file1.readline())

#readlines() => convert lines to list
# print(file1.readlines())
# file1.close()


#2:
# with open('15_my_file.txt', 'r') as file1:
#     reading_file = file1.read()
#     print(reading_file)