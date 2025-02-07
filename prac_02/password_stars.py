MIN_LENGTH = 6  # Set the minimum password length

def main():
    get_password()


def get_password():
    password = input("Enter a password: ")  # Ask for password
    while len(password) < MIN_LENGTH:  # Check if the password is too short
        print("Password too short. Must be at least", MIN_LENGTH, "characters.")
        password = input("Enter a password: ")  # Ask again
    print(password)


def print(password):
    print("*" * len(password))  # Print asterisks equal to the password length


main()  # Call main() to run the program
