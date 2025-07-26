from stats import get_book_text, get_number_of_words, count_characters, print_the_results

import sys

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]  # Get the first command line argument
    print_the_results(filepath)