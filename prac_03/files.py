name = input("Enter your name: ")

name_file = open('name.txt', 'w')
name_file.write(name)
name_file.close()

name_file = open('name.txt', 'r')
name = name_file.read().strip()
name_file.close()

print(f"Hi {name}!")

file = open('numbers.txt', 'r')

number_one = int(file.readline())
number_two = int(file.readline())

total = number_one + number_two

file.close()

print("The sum of the first two numbers is: ", total)