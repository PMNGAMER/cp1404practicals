"""
names = ["Ada", "Alan", "Bill", "John"]
print(", ".join(names))

name_to_remove = input("Who do you want to remove? : ")
while name_to_remove != "":
    try:
        names.remove(name_to_remove)
        print(f"Updated list: {', '.join(names)}")
    except ValueError:
        print(f"{name_to_remove} is not in the list.")

    name_to_remove = input("Who do you want to remove? (Press Enter to stop): ")

print(f"Final list: {', '.join(names)}")
"""
def main():
    numbers = get_numbers()  # Get numbers from user
    square_numbers(numbers)   # Square each number
    display_numbers(numbers)   # Display the squared numbers

def get_numbers():
    """Get a list of numbers from user input."""
    user_input = input("Enter numbers separated by commas: ")
    # Split the input string by commas and convert each to float
    numbers = [float(num.strip()) for num in user_input.split(",")]
    return numbers

def square_numbers(numbers):
    """Square each number in the list."""
    for i in range(len(numbers)):
        numbers[i] = numbers[i] ** 2  # Square the number

def display_numbers(numbers):
    """Display the squared numbers separated by '..'."""
    # Convert numbers to strings and join them with '..'
    output = "..".join(str(num) for num in numbers)
    print(output)

# Call the main function to execute the program
#if __name__ == "__main__":
    #main()

