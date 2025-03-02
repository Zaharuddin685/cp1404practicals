FILENAME = "wimbledon.csv"

def read_wimbledon_data(filename):
    """Read Wimbledon data from file and return a list of (champion, country)."""
    with open(filename, "r", encoding="utf-8-sig") as file:
        lines = file.readlines()[1:]  # Skip header
        data = []
        for line in lines:
            parts = line.strip().split(",")  # Use comma instead of tab
            if len(parts) >= 3:  # Ensure there are enough columns
                champion = parts[2]  # Champion's name
                country = parts[1]   # Champion's country
                data.append((champion, country))
        return data

def process_winners(data):
    """Count the number of wins per player and collect unique countries."""
    winners = {}  # Dictionary to store player -> win count
    countries = set()  # Set to store unique countries

    for champion, country in data:
        winners[champion] = winners.get(champion, 0) + 1
        countries.add(country)

    return winners, countries

def display_results(winners, countries):
    """Display the processed winners and country data."""
    print("Wimbledon Champions:")
    for player, wins in sorted(winners.items()):
        print(f"{player} {wins}")

    print("\nThese", len(countries), "countries have won Wimbledon:")
    print(", ".join(sorted(countries)))

def main():
    """Main function to run the program."""
    data = read_wimbledon_data(FILENAME)
    winners, countries = process_winners(data)
    display_results(winners, countries)

main()
