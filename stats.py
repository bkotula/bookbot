def get_book_text(path):
    with (open(path)) as f:
        return f.read()


def get_number_of_words(text):
    return len(text.split())


def count_characters(text):
    char_count = {}
    for char in text.lower():
        if char in char_count:
            char_count[char] += 1
        else:
            char_count[char] = 1
    return char_count

def sort_on(items):
    return items["num"]


def sort_counts(counts):
    dictionary_list = []
    for key, value in counts.items():
        char_to_count_dict = {"char": key, "num": value}
        dictionary_list.append(char_to_count_dict)
    dictionary_list.sort(key=sort_on, reverse=True)
    return dictionary_list

def print_the_results(filepath):
    text = get_book_text(filepath)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    num_words = get_number_of_words(text)

    print("----------- Word Count ----------")
    print(f"Found {num_words} total words")
    print("--------- Character Count -------")

    character_count = count_characters(text)
    sorted_counts = sort_counts(character_count)

    for count in sorted_counts:
        char = count['char']
        num = count['num']
        if char.isalpha():
            print(f"{char}: {num}")
    print("============= END ===============")

