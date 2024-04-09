def main():
    book_path = "books/frankenstein.txt"
    book_content = read_book(book_path)
    print(book_content)

def read_book(book_path):
    with open(book_path) as f:
        return f.read()

main()
