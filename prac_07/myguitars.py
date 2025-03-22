import csv
from guitar import Guitar


def read_guitar_data(file_name):
    """Read guitar data from a CSV file and return a list of Guitar objects."""
    guitars = []
    try:
        with open(file_name, 'r') as file:
            reader = csv.reader(file)
            for row in reader:
                name, year, cost = row
                guitar = Guitar(name, int(year), float(cost))
                guitars.append(guitar)
    except FileNotFoundError:
        print(f"{file_name} not found, starting with an empty list.")
    return guitars


def display_guitars(guitars):
    """Display all guitars with their details."""
    for guitar in guitars:
        print(guitar)


def add_new_guitar(guitars):
    """Prompt the user to enter details for a new guitar and add it to the list."""
    print("\nEnter details of the new guitar:")
    name = input("Name: ")
    year = int(input("Year: "))
    cost = float(input("Cost: "))
    new_guitar = Guitar(name, year, cost)
    guitars.append(new_guitar)
    print(f"{new_guitar} added.")


def write_guitars_to_file(file_name, guitars):
    """Write the list of guitars to the specified file."""
    with open(file_name, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])
    print(f"All guitars have been written to {file_name}.")


def main():
    """Main function to run the program."""
    file_name = 'guitars.csv'

    # Step 1: Read the existing guitars from the file
    guitars = read_guitar_data(file_name)

    # Step 2: Ask user if they want to add a new guitar
    add_new = input("\nDo you want to add a new guitar? (yes/no): ").strip().lower()
    if add_new == 'yes':
        add_new_guitar(guitars)

    # Step 3: Sort guitars by year (oldest to newest)
    guitars.sort()  # This works because we've defined the __lt__ method for comparison

    # Step 4: Display all guitars
    print("\nHere are all the guitars:")
    display_guitars(guitars)

    # Step 5: Write all guitars (old and new) back to the file
    write_guitars_to_file(file_name, guitars)


if __name__ == '__main__':
    main()
