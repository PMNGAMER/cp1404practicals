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


def main():
    """Main function to read, display, and sort guitars."""
    # Read guitars from file
    guitars = read_guitars()

    # Display unsorted guitars
    print("Unsorted Guitars:")
    display_guitars(guitars)

    # Sort guitars by year (using the _lt_ method in Guitar class)
    guitars.sort()

    # Display sorted guitars
    print("\nGuitars sorted by year (oldest to newest):")
    display_guitars(guitars)


if __name__ == "__main__":
    main()
