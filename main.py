def main():
    book_path = "books/frankenstein.txt"
    book_content = read_book(book_path)
    word_count = count_words(book_content)
    characters_count = count_characters(book_content)
    print_report(book_path, word_count, characters_count)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()
    
def count_words(text):
    words = text.split()
    return len(words)

def count_characters(text):
    letter_count = {}
    lower_case_text = text.lower()
    for character in lower_case_text:
        if character in letter_count:
            letter_count[character] += 1
        else:
            letter_count[character] = 1

    return letter_count

def print_report(book, word_count, character_count):
    print(f"--- Begin report of {book} ---")
    print(f"{word_count} words found in the document")

    character_count_sorted = convert_dic_to_list(character_count)
    character_count_sorted.sort(reverse=True, key=sort_on)

    for character in character_count_sorted:
        if character["character"].isalpha():
            print(f"the '{character["character"]}' character was found {character["count"]} times")
            
    print("--- End of report ---")


def convert_dic_to_list(dictionary):
    dic_list = []
    for item in dictionary:
        dic_list.append({"character": item, "count": dictionary[item]})
    return dic_list

def sort_on(dict):
    return dict["count"]


main()
