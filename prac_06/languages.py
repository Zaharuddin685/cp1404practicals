from programming_language import ProgrammingLanguage

# Create ProgrammingLanguage objects
python = ProgrammingLanguage("Python", "Dynamic", True, 1991)
ruby = ProgrammingLanguage("Ruby", "Dynamic", True, 1995)
visual_basic = ProgrammingLanguage("Visual Basic", "Static", False, 1991)

# Store them in a list
languages = [python, ruby, visual_basic]

# Print each language to check the __str__ method
for language in languages:
    print(language)

print("\nThe dynamically typed languages are:")
for language in languages:
    if language.is_dynamic():
        print(language.name)