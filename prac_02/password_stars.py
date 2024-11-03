MINIMUM_LENGTH = 5
password = input("Enter a password: ")

while len(password) < MINIMUM_LENGTH:
    print(f"Password must be at least {MINIMUM_LENGTH} characters long".format(MINIMUM_LENGTH))
    password = input("Enter a password: ")

asterisks = "*" * len(password)
print(asterisks)