"""Programming Language class for CP1404 Practical.

Estimated time: 30 minutes
Start time: [Your Start Time]
End time: [Your End Time]
"""

class ProgrammingLanguage:
    """Represent details of a programming language."""

    def __init__(self, name, typing, reflection, year):
        """Initialize a ProgrammingLanguage instance with name, typing, reflection, and year."""
        self.name = name
        self.typing = typing
        self.reflection = reflection
        self.year = year

    def is_dynamic(self):
        """Return True if the programming language is dynamically typed, otherwise False."""
        return self.typing == "Dynamic"

    def __str__(self):
        """Return a string representation of the programming language details."""
        return f"{self.name}, {self.typing} Typing, Reflection={self.reflection}, First appeared in {self.year}"
