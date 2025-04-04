from unreliable_car import UnreliableCar

def main():
    # Create an UnreliableCar with 30% reliability
    test_car = UnreliableCar("Unreliable", 1000, 30)

    drive_attempts = 100
    success_count = 0
    total_distance = 0

    for i in range(drive_attempts):
        distance_driven = test_car.drive(1)  # try driving 1km each time
        if distance_driven > 0:
            success_count += 1
            total_distance += distance_driven

    print(f"Tried to drive {drive_attempts} times with 30% reliability.")
    print(f"Number of successful drives: {success_count}")
    print(f"Total distance actually driven: {total_distance}km")

    # Rough check: should be around 30 successful drives
    if 20 <= success_count <= 40:
        print("Test passed: behavior is statistically valid.")
    else:
        print("Test failed: unexpected success rate.")

main()

