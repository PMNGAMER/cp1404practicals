from guitar import Guitar


def main():
    """Program to store and display details of guitars entered by the user."""
    guitars = []
    print("My guitars!")

    # Get guitar details from the user
    while True:
        name = input("Name: ")
        if not name:  # Exit loop if the name is blank
            break
        year = int(input("Year: "))
        cost = float(input("Cost: $"))
        new_guitar = Guitar(name, year, cost)
        guitars.append(new_guitar)
        print(f"{new_guitar} added.\n")

    # Display all guitars with formatted output
    print("\nThese are my guitars:")
    for i, guitar in enumerate(guitars, 1):
        vintage_string = " (vintage)" if guitar.is_vintage() else ""
        print(f"Guitar {i}: {guitar.name:>20} ({guitar.year}), worth ${guitar.cost:10,.2f}{vintage_string}")


# For testing purposes, add sample guitars directly
main()
