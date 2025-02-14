"""
CP1404/CP5632 - Practical
Answer the following questions:
1. When will a ValueError occur?
A ValueError will occur if the user enters something that cannot be converted to an integer (e.g., a letter, special character, or an empty input).
The int() function will raise this error when it tries to convert an invalid input to an integer.

2. When will a ZeroDivisionError occur?
A ZeroDivisionError will occur when the user enters 0 as the denominator.

3. Could you change the code to avoid the possibility of a ZeroDivisionError?
Yes, you could check if the denominator is 0 before performing the division.
"""

try:
    numerator = int(input("Enter the numerator: "))
    denominator = int(input("Enter the denominator: "))

    # Check for division by zero
    if denominator == 0:
        print("Cannot divide by zero!")
    else:
        fraction = numerator / denominator
        print(fraction)

except ValueError:
    print("Numerator and denominator must be valid numbers!")

print("Finished.")
