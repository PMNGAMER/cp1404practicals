"""
CP1404/CP5632 Practical
Data file -> lists program
"""

FILENAME = "subject_data.txt"


def main():
    data = load_data()  # Load the data as a list of lists
    display_subject_details(data)  # Display the subject details


def load_data():
    """Read data from file formatted like: subject,lecturer,number of students."""
    data = []  # List to hold the subjects data
    input_file = open(FILENAME)
    for line in input_file:
        line = line.strip()  # Remove the \n
        parts = line.split(',')  # Separate the data into its parts
        parts[2] = int(parts[2])  # Convert the number of students to an integer
        data.append(parts)  # Add each line (as a list) to the data list
    input_file.close()
    return data


def display_subject_details(data):
    """Display details of each subject in a formatted way."""
    for subject in data:
        subject_code, lecturer, student_count = subject
        print(f"{subject_code} is taught by {lecturer} and has {student_count} students")


main()
