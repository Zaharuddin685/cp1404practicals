MIN_LENGTH = 6  # Set the minimum password length

password = input("Enter a password: ")  # Ask for password

while len(password) < MIN_LENGTH:  # Check if the password is too short
    print("Password too short. Must be at least", MIN_LENGTH, "characters.")
    password = input("Enter a password: ")  # Ask again

print("*" * len(password))  # Print asterisks equal to the password length
