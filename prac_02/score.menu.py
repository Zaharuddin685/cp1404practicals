def main():
    score = ask_for_score()  # Get the initial score
    display_menu()
    users_choice = input(">>> ").upper()

    while users_choice != "Q":
        if users_choice == "G":
            score = get_valid_score()  # Get a valid score and update the score variable
        elif users_choice == "P":
            print(show_result(score))  # Show the result based on the score
        elif users_choice == "S":
            show_stars(score)  # Show stars based on the score
        else:
            print("Invalid choice")

        display_menu()  # Display the menu again
        users_choice = input(">>> ").upper()  # Ask for the next choice

    print("Farewell")  # Farewell message when the user quits


def ask_for_score():
    score = float(input("Enter a score (0-100): "))  # Asking for the score
    return score


def display_menu():
    print("\nMenu:")
    print("(G)et a valid score")
    print("(P)rint result")
    print("(S)how stars")
    print("(Q)uit")


def get_valid_score():
    score = float(input("Enter a score (0-100): "))  # Asking for the score
    while score < 0 or score > 100:
        print("Invalid score. Please enter a score between 0 and 100.")
        score = float(input("Enter a score (0-100): "))  # Asking again if invalid
    return score  # Return the valid score after input is correct


def show_result(score):
    """Returns the result based on the score."""
    if score < 0 or score > 100:
        return "Invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    else:
        return "Excellent"


def show_stars(score):
    print("*" * int(score))  # Print a number of stars based on the score


# Call main to run the program
main()
