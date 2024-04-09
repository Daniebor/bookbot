def main():
    book_path = "books/frankenstein.txt"
    book_content = read_book(book_path)
    word_count = count_words(book_content)
    characters_count = count_characters(book_content)
    print(characters_count)

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

main()
