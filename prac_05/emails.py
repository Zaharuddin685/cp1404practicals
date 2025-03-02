def extract_name(email):
    """Extracts a name from an email address."""
    name_part = email.split('@')[0]  # Get the part before '@'
    name = " ".join(name_part.split('.')).title()  # Replace dots with spaces and capitalize
    return name

def main():
    """Main function to collect emails and names, then display them."""
    email_to_name = {}

    email = input("Email: ")
    while email:
        suggested_name = extract_name(email)
        response = input(f"Is your name {suggested_name}? (Y/n) ").strip().lower()

        if response and response != 'y':  # If response is not empty and not 'y', ask for a name
            name = input("Name: ")
        else:
            name = suggested_name

        email_to_name[email] = name
        email = input("Email: ")  # Ask for the next email

    # Print stored emails and names
    print("\nStored Users:")
    for email, name in email_to_name.items():
        print(f"{name} ({email})")

if __name__ == "__main__":
    main()
