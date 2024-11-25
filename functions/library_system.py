DATABASE_FILE = "./database/books.txt"

def initialize_database():
    """
    Initialize the database file if it doesn't exist.
    """
    with open(DATABASE_FILE, 'a') as db:
        pass  # Ensure the file exists
 


def add_book(title, author):
    """
    Add a new book to the library.
    :param title: The title of the book
    :param author: The author of the book
    """
    # TODO: Append the book's title and author to the database file
def add_book(title, author, new_book):
    if title in list_books:
        if author in list_books:
            add_book.append(new_book)
            if new_book in list_books:
                return new_book


def search_book(title):
    """
    Search for a book by title.
    :param title: The title of the book to search for
    :return: A dictionary with the book's details if found, else None
    """
    # TODO: Implement logic to search for a book in the database file
    if title in[]:
        if list_books == search_book:
            print(f"found:{list_books[title]} by {list_books['author']}")
        else:
            print("book not found")




def list_books():
    """
    List all books in the library.
    :return: A list of dictionaries with each book's details
    """
    # TODO: Read all books from the database file and return them as a list of dictionaries
    if list_books == list_books:
        details = list_books
        return list_books



