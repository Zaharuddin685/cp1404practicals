from guitar import Guitar

def main():
    """Test the Guitar class methods for get_age() and is_vintage()."""
    # Create test guitars
    guitar1 = Guitar("Gibson L-5 CES", 1922, 16035.40)
    guitar2 = Guitar("Another Guitar", 2013, 999.99)

    # Expected values based on the year 2022 (update if needed)
    expected_age1 = 2022 - 1922  # 100
    expected_age2 = 2022 - 2013  # 9
    expected_vintage1 = True
    expected_vintage2 = False

    # Test get_age()
    print(f"{guitar1.name} get_age() - Expected {expected_age1}. Got {guitar1.get_age()}")
    print(f"{guitar2.name} get_age() - Expected {expected_age2}. Got {guitar2.get_age()}")

    # Test is_vintage()
    print(f"{guitar1.name} is_vintage() - Expected {expected_vintage1}. Got {guitar1.is_vintage()}")
    print(f"{guitar2.name} is_vintage() - Expected {expected_vintage2}. Got {guitar2.is_vintage()}")

if __name__ == "__main__":
    main()
