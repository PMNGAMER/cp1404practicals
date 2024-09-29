"""total = 0
count = 0

age = int(input("Enter the age: "))

while age >= 0:
    total += age
    count += 1
    age = int(input("Enter the age: "))

print(total)
print(total / count)"""

"""
get number of gifts
get number of students
display number of gifts // number of students
display number of gift % number of students
"""

"""num_of_gifts = int(input("Enter the Number of Gifts: "))
num_of_students = int(input("Enter the Number of Students: "))

print(num_of_gifts // num_of_students)
print( num_of_gifts % num_of_students)"""

"""GST = 0.09
item_price = float(input("Enter your Item Price :"))
gst_confirmation = input("Does your Item Contain GST? (Enter Yes or No): ").strip().lower()

if gst_confirmation == 'yes':
    final_price = item_price + (item_price * GST)
else:
    final_price = item_price
print(f"Your Final Price is {final_price:.2f}")"""

"""user_number = int(input("Enter Your Number: "))
for i in range(1, user_number + 1):
    print(i)

i = 1
while i <= user_number:
    print(i)
    i += 1"""

"""SECRET_NUMBER = 9

guess_number = int(input("Enter the Secret Number: "))
while guess_number < 1 or guess_number > 10:
    print("Your Number must be from 1 to 10")
    guess_number = int(input("Enter the Secret Number: "))
else:
    while guess_number != SECRET_NUMBER:
        print("Try Again!")
        guess_number = int(input("Enter the Secret Number: "))
    else:
        print("Wow! You guessed it right !!!")

"""

"""user_name = input("Enter Your Name: ").upper().strip()
while user_name == "":
    print("Your user name cannot be blank. Please reenter your name")
    user_name = input("Enter Your Name: ").upper().strip()

salary = float(input("Enter Your Salary: "))
while salary < 0:
    print("Your Salary Cant be less than 0. Please reenter your Salary.")
    salary = float(input("Enter Your Salary: "))
else:
    print(f"Your Username is {user_name} and earn a salary of ${salary}")"""


"""num_of_ages = int(input("How many ages are there? : "))
total = 0
for i in range(1, num_of_ages + 1):
    input_ages = int(input(f"Enter age {i}: "))
    total += input_ages

average = total / num_of_ages
print(f"The total is {total} and the average is {average}")
"""

for i in range(1,4):
    for j in range(2, 10, 3):
        print(i, "-", j + i)