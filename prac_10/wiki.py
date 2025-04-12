"""
CP1404/CP5632 Practical
Wikipedia API program
"""

import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError

def main():
    while True:
        search_term = input("Enter page title: ").strip()
        if search_term == "":
            print("Thank you.")
            break

        try:
            page = wikipedia.page(search_term)
            print(page.title)
            print(page.summary)
            print(page.url)
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following, or a new search:")
            print(e.options)
        except PageError:
            print(f'Page id "{search_term}" does not match any pages. Try another id!')

if __name__ == "__main__":
    main()
