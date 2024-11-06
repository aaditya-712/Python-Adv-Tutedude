numbers = [10,20,30,40,50,60,70]
#           0  1  2  3  4  5  6

#list slicing
# numbers[n:n+1:interval]

print(numbers[0:5])     #[10, 20, 30, 40, 50]
print(numbers[:4])      #[10, 20, 30, 40]
print(numbers[3:7])     #[40, 50, 60, 70]
print(numbers[3:])      #[40, 50, 60, 70]

#interval
print(numbers[0:5:2])       #[10, 30, 50]