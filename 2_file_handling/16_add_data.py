# r - read
# w - write
# a - append


file1 = open('16_add_data.txt', 'w')
writing_file = file1.write("Hello, Good morning")
print(writing_file)
file1.close()

file1 = open('16_add_data.txt', 'r')
reading_file = file1.read()
print(reading_file)

#limitation to the write mode is that
# the existing data gets erased when new data is introduced
# To avoid this we use append mode


