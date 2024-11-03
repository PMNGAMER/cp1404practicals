from programming_language import ProgrammingLanguage

# Create ProgrammingLanguage instances
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Print each language to test __str__ method
print(python)
print(ruby)
print(visual_basic)

# List of ProgrammingLanguage objects
languages = [python, ruby, visual_basic]

# Print names of dynamically typed languages
print("The dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)
