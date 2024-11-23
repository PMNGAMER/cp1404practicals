from unreliable_car import UnreliableCar

def main():
    """Test the UnreliableCar class."""
    # Create a few UnreliableCar objects with varying reliability
    car1 = UnreliableCar("Mostly Reliable", 100, 90)  # High reliability
    car2 = UnreliableCar("Unreliable", 100, 20)       # Low reliability

    # Drive each car 50 km multiple times and display the results
    print(car1)
    for i in range(5):
        distance_driven = car1.drive(50)
        print(f"Attempt {i+1}: {car1.name} drove {distance_driven} km")
        print(car1)

    print(car2)
    for i in range(5):
        distance_driven = car2.drive(50)
        print(f"Attempt {i+1}: {car2.name} drove {distance_driven} km")
        print(car2)


if __name__ == "__main__":
    main()
