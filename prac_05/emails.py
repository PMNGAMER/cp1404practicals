def get_name_from_email(email):
    """Extract a guessed name from the email address."""
    name_part = email.split('@')[0]
    name_parts = name_part.split('.')
    guessed_name = " ".join(name_parts).title()
    return guessed_name


def main():
    """Main function to input emails and names, and store them in a dictionary."""
    emails_to_names = {}

    email = input("Email: ")
    while email != "":
        name = get_name_from_email(email)
        confirmation = input(f"Is your name {name}? (Y/n) ").lower()

        if confirmation != "" and confirmation != "y":
            name = input("Name: ")

        emails_to_names[email] = name
        email = input("Email: ")

    # Print the results
    for email, name in emails_to_names.items():
        print(f"{name} ({email})")


if __name__ == "__main__":
    main()
