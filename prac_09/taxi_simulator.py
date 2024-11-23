from taxi import Taxi
from silver_service_taxi import SilverServiceTaxi

def main():
    """Taxi simulator program."""
    taxis = [
        Taxi("Prius", 100),
        SilverServiceTaxi("Limo", 100, 2),
        SilverServiceTaxi("Hummer", 200, 4)
    ]
    bill = 0
    current_taxi = None

    print("Let's drive!")
    menu = "q)uit, c)hoose taxi, d)rive"
    print(menu)

    while True:
        choice = input(">>> ").lower()

        if choice == "q":
            # Quit the program
            print(f"Total trip cost: ${bill:.2f}")
            print("Taxis are now:")
            display_taxis(taxis)
            break
        elif choice == "c":
            # Choose a taxi
            print("Taxis available:")
            display_taxis(taxis)
            try:
                taxi_choice = int(input("Choose taxi: "))
                if 0 <= taxi_choice < len(taxis):
                    current_taxi = taxis[taxi_choice]
                else:
                    print("Invalid taxi choice")
            except ValueError:
                print("Invalid input; please enter a number")
        elif choice == "d":
            # Drive the taxi
            if current_taxi is None:
                print("You need to choose a taxi before you can drive")
            else:
                try:
                    distance = float(input("Drive how far? "))
                    current_taxi.start_fare()
                    distance_driven = current_taxi.drive(distance)
                    trip_cost = current_taxi.get_fare()
                    bill += trip_cost
                    print(f"Your {current_taxi.name} trip cost you ${trip_cost:.2f}")
                except ValueError:
                    print("Invalid input; please enter a number")
        else:
            # Invalid option
            print("Invalid option")

        print(f"Bill to date: ${bill:.2f}")
        print(menu)

def display_taxis(taxis):
    """Display a list of available taxis with their index."""
    for i, taxi in enumerate(taxis):
        print(f"{i} - {taxi}")

if __name__ == "__main__":
    main()
