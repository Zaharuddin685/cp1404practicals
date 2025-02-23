def main():
    numbers = []  # Initialize an empty list

    # Prompt the user to input 5 numbers
    for i in range(5):
        number = float(input(f"Number: "))  # Convert the input to a float
        numbers.append(number)  # Add the number to the list

    # Output the required information with rounded numbers for first, last, smallest, and largest
    print(f"The first number is {round(numbers[0])}")
    print(f"The last number is {round(numbers[-1])}")
    print(f"The smallest number is {round(min(numbers))}")
    print(f"The largest number is {round(max(numbers))}")
    print(f"The average of the numbers is {sum(numbers) / len(numbers):.1f}")  # Average with one decimal place

main()
