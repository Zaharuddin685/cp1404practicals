"""
CP1404/CP5632 Practical
Testing code using assert and doctest
"""

import doctest
from prac_09.car import Car


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
    Format a phrase to be a sentence starting with a capital
    and ending with a single full stop.

    >>> format_sentence("hello")
    'Hello.'
    >>> format_sentence("It is an ex parrot.")
    'It is an ex parrot.'
    >>> format_sentence("wHaT a MeSs")
    'What a mess.'
    """
    phrase = phrase.strip()
    if not phrase.endswith('.'):
        phrase += '.'
    return phrase[0].upper() + phrase[1:-1].lower() + '.'


def run_tests():
    """Run the tests on the functions."""
    # assert test with no message - used to see if the function works properly
    assert repeat_string("Python", 1) == "Python"
    # fixed test: should now pass
    assert repeat_string("hi", 2) == "hi hi"

    # test Car odometer default
    car = Car()
    assert car._odometer == 0, "Car does not set odometer correctly"

    # test Car fuel default
    default_car = Car()
    assert default_car.fuel == 0, "Default fuel should be 0"

    # test Car with specified fuel
    specific_fuel_car = Car(fuel=10)
    assert specific_fuel_car.fuel == 10, "Car does not set fuel correctly when specified"


run_tests()

# Run doctests
doctest.testmod()
