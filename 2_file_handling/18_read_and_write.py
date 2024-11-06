# r+ : read and write

file = open('18_file.txt', 'r+')
writing_file = file.write("welcome")
print(writing_file)
file.close()

file = open('18_file.txt', 'r+')
reading_file = file.read()
print(reading_file)
file.close()