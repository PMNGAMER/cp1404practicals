import wikipedia
from wikipedia.exceptions import DisambiguationError, PageError
import warnings
from bs4 import GuessedAtParserWarning

# Suppress BeautifulSoup parser warning
warnings.filterwarnings("ignore", category=GuessedAtParserWarning)

def main():
    wikipedia.set_lang("en")  # Set language to English
    print("Welcome to the Wikipedia Search Tool!")

    while True:
        query = input("Enter a page title or search phrase (or press Enter to quit): ").strip()
        if not query:
            print("Thank you for using the Wikipedia Search Tool. Goodbye!")
            break

        try:
            # Try to fetch the page
            page = wikipedia.page(query, auto_suggest=True)
            print(f"\nTitle: {page.title}")
            print(f"Summary: {page.summary[:500]}...")  # Display the first 500 characters
            print(f"URL: {page.url}\n")
        except DisambiguationError as e:
            print("We need a more specific title. Try one of the following options:")
            print(e.options)
        except PageError:
            print(f"No page found for \"{query}\". Try a different query!")
        except Exception as ex:
            print(f"An unexpected error occurred: {ex}")

if __name__ == "__main__":
    main()
