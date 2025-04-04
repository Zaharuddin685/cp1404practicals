from silver_service_taxi import SilverServiceTaxi

def main():
    # Create a SilverServiceTaxi
    fancy_taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Start fare and drive 18 km
    fancy_taxi.start_fare()
    fancy_taxi.drive(18)

    # Check output
    print(fancy_taxi)
    print(f"Fare: ${fancy_taxi.get_fare():.2f}")

    # Assert test
    expected_fare = 18 * 1.23 * 2 + 4.50
    assert abs(fancy_taxi.get_fare() - expected_fare) < 0.01, "Fare calculation failed"

main()


