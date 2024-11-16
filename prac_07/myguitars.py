import csv
from guitar import Guitar


def read_guitars(filename="guitars.csv"):
    """Read guitars from a CSV file and return a list of Guitar objects."""
    guitars = []
    with open(filename, 'r') as file:
        reader = csv.reader(file)
        for row in reader:
            # Each row is in the format: name, year, cost
            name = row[0]
            year = int(row[1])
            cost = float(row[2])
            guitar = Guitar(name, year, cost)
            guitars.append(guitar)
    return guitars


def display_guitars(guitars):
    """Display each guitar in the list."""
    print("Guitars:")
    for guitar in guitars:
        print(guitar)

def save_guitars(guitars, filename="guitars.csv"):
    """Save the list of Guitar objects to a CSV file."""
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        for guitar in guitars:
            writer.writerow([guitar.name, guitar.year, guitar.cost])

def add_new_guitars():
    """Prompt the user to enter new guitars and return them as a list."""
    print("Enter your new guitars (leave name blank to finish):")
    new_guitars = []
    name = input("Name: ")

    # Continue looping as long as the user enters a name
    while name.strip() != "":
        try:
            year = int(input("Year: "))
            cost = float(input("Cost: $"))
            new_guitar = Guitar(name, year, cost)
            new_guitars.append(new_guitar)
        except ValueError:
            print("Invalid input. Please enter numbers for year and cost.")

        # Prompt for the next guitar's name (or leave blank to finish)
        name = input("Name: ")

    return new_guitars

def main():
    """Main function to read, display, and sort guitars."""
    # Read guitars from file
    guitars = read_guitars()

    # Display unsorted guitars
    print("Unsorted Guitars:")
    display_guitars(guitars)

    # Add new guitars entered by the user
    new_guitars = add_new_guitars()
    guitars.extend(new_guitars)

    # Filter out any empty or invalid entries before sorting
    guitars = [guitar for guitar in guitars if guitar.name and guitar.year and guitar.cost]

    # Sort guitars by year (using the _lt_ method in Guitar class)
    guitars.sort()

    # Display sorted guitars
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)

    save_guitars(guitars)
    print("\nGuitars have been saved to guitars.csv")


if __name__ == "__main__":
    main()
