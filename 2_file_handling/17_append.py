# Append mode
file1 = open('16_add_data.txt', 'a')
appending_file = file1.write("\nWelcome to append.")
file1.close()

file1 = open('16_add_data.txt', 'r')
reading_file = file1.read()
print(reading_file)
file1.close()