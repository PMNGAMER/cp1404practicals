from silver_service_taxi import SilverServiceTaxi

def main():
    """Test the SilverServiceTaxi class."""

    # Create a SilverServiceTaxi with fanciness of 2
    taxi = SilverServiceTaxi("Hummer", 200, 2)

    # Display the initial details
    print(taxi)

    # Drive the taxi 18 km
    taxi.drive(18)

    # Calculate the fare
    fare = taxi.get_fare()

    # Display the details and fare
    print(taxi)
    print(f"Fare: ${fare:.2f}")

    # Assert the fare is as expected
    assert abs(fare - 48.78) < 0.01, f"Expected fare to be $48.78, got ${fare:.2f}"

if __name__ == "__main__":
    main()
