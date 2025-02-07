"""
CP1404/CP5632 - Practical
Broken program to determine score status
"""
import random


def main():
    score = float(input("Enter score: "))
    result = get_result(score)  # Call the function to get the result
    print(result)  # Print the result
    random_score = random.uniform(0,100)
    print(f"Your random score is {random_score:.2f}.")
    print(get_result(random_score))

def get_result(score):
    """Returns the result based on the score."""
    if score < 0 or score > 100:
        return "invalid score"
    elif score < 50:
        return "Bad"
    elif score < 90:
        return "Passable"
    elif score >= 90:
        return "Excellent"

# Call the main function to run the code
main()
