from guitar import Guitar


def main():
    """Program to collect and display guitars."""
    print("My guitars!")

    guitars = []

    # User input loop
    while True:
        name = input("Name: ").strip()
        if name == "":
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))

        guitar = Guitar(name, year, cost)
        guitars.append(guitar)
        print(f"{guitar} added.\n")

    # Test data (for efficiency, comment out user input and use these)
    # guitars.append(Guitar("Gibson L-5 CES", 1922, 16035.40))
    # guitars.append(Guitar("Line 6 JTV-59", 2010, 1512.9))
    # guitars.append(Guitar("Fender Stratocaster", 2014, 765.4))

    # Display guitars
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_label = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_label}")


if __name__ == "__main__":
    main()
