import random

# CONSTANTS for the range of numbers
MIN_NUMBER = 1
MAX_NUMBER = 45
NUMBERS_PER_PICK = 6


def generate_quick_pick():
    """Generate a single quick pick (a sorted list of 6 unique random numbers)."""
    # Generate a list of 6 unique random numbers between MIN_NUMBER and MAX_NUMBER
    pick = random.sample(range(MIN_NUMBER, MAX_NUMBER + 1), NUMBERS_PER_PICK)
    pick.sort()  # Sort the list in ascending order
    return pick


def main():
    # Ask the user for how many quick picks they want to generate
    num_picks = int(input("How many quick picks? "))

    # Generate and print the required number of quick picks
    for _ in range(num_picks):
        pick = generate_quick_pick()
        # Print the quick pick with each number aligned to the right, making sure they all align neatly
        print(" ".join(f"{num:2}" for num in pick))


main()
