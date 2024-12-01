import doctest
from car import Car

def repeat_string(s, n):
    """Repeat string s, n times, with spaces in between."""
    return " ".join([s] * n)

def is_long_word(word, length=5):
    """
    Determine if the word is as long or longer than the length passed in
    >>> is_long_word("not")
    False
    >>> is_long_word("supercalifrag")
    True
    >>> is_long_word("Python", 6)
    True
    """
    return len(word) >= length

def format_sentence(phrase):
    """
    Format a phrase as a sentence, starting with a capital letter
    and ending with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("this is a test")
    'This is a test.'
    """
    return phrase[0].capitalize() + phrase[1:].rstrip('.') + '.'

def run_tests():
    """Run the tests on the functions."""
    assert repeat_string("Python", 1) == "Python"
    assert repeat_string("hi", 2) == "hi hi"

    car = Car()  # Default value
    assert car.fuel == 0, "Default fuel should be 0"

    car = Car(fuel=20)  # Custom value
    assert car.fuel == 20, "Fuel should be set to 20"

run_tests()

# Run doctests
doctest.testmod()
